import re

from entities.entity import Entity

from exception import LoginError, EmailIsAlreadyUsed, PhoneNumberFormatError, EmailFormatError, SignupError, \
    NotSameShopError, CartIsEmptyError, InvalidDiscountError, MinBillValueError


class User(Entity):
    def __init__(self, userId):
        tbl = User.select_tuples('User', ['userId'], [userId])[0]
        self._first_name = tbl[0]
        self._last_name = tbl[1]
        self.phone_number = tbl[2]
        self._email = tbl[3]
        self._password = tbl[4]
        self.userId = tbl[5]
        self.walletId = tbl[6]

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        User.update_tuple('User', 'first-name', value, f'"userId" = \'{self.userId}\'')
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        User.update_tuple('User', 'last-name', value, f'"userId" = \'{self.userId}\'')
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        User.check_email_format(value)
        if User.select_tuples('User', ['email'], [value]):
            raise EmailIsAlreadyUsed('Email is already used.')
        User.update_tuple('User', 'email', value, f'"userId" = \'{self.userId}\'')
        self._email = value

    def change_password(self, password):
        # TODO: hash password
        User.update_tuple('User', 'password', password, f'"userId" = \'{self.userId}\'')
        self._password = password

    @classmethod
    def add(cls, phone_number, password):
        cls.check_phone_number_format(phone_number)
        if cls.select_tuples('User', ['phone-number'], [phone_number]):
            raise SignupError('Phone number is already used.')
        cls.insert_tuple('User', ['phone-number', 'password'], [phone_number, password])
        userId = cls.get_user_id(phone_number)
        from entities.wallet import Wallet
        wallet = Wallet(userId)
        cls.update_tuple('User', 'walletId', wallet.walletId, f'"userId" = \'{userId}\'')
        return cls.get_user_id(phone_number)

    @classmethod
    def get_user_id(cls, phone_number):
        tbl = cls.select_tuples('User', ['phone-number'], [phone_number])
        userId = tbl[0][-2]
        return userId

    @classmethod
    def login(cls, phone_number, password):
        cls.check_phone_number_format(phone_number)
        this_user = cls.select_tuples('User', ['phone-number', 'password'], [phone_number, password])
        if not this_user:
            raise LoginError('Invalid username or password.')
        return this_user[0][5]

    @classmethod
    def check_phone_number_format(cls, phone_number: str) -> None:
        match = re.match(r'09\d{9}', phone_number)
        if not match or match.group() != phone_number:
            raise PhoneNumberFormatError

    @classmethod
    def check_email_format(cls, email: str) -> None:
        match = re.match(r'(\w+)([._])?(\w*)@(\w+)(\.(\w+))+', email)
        if not match or match.group() != email:
            raise EmailFormatError

    def add_address(self, cityId, lat, lon, street=None, alley=None, plaque=None):
        from entities.address import Address
        addressId = Address.add(self.userId, cityId, lat, lon)
        new_address = Address(addressId)
        if street is not None:
            new_address.street = street
        if alley is not None:
            new_address.alley = alley
        if plaque is not None:
            new_address.plaque = plaque

    def get_addresses(self):
        from entities.address import Address
        tbl = User.select_tuples('Address', ['userId'], [self.userId])
        for address in tbl:
            pl, al, st, ai, ui, li, ci = address
            yield Address(ai)

    def add_to_cart(self, foodId):
        from entities.food import Food
        if self.cart and Food(self.cart[0]).shopId != Food(foodId).shopId:
            raise NotSameShopError
        User.insert_tuple('IsInCart', ['userId', 'foodId'], [self.userId, foodId])

    def clear_cart(self):
        User.exe_query(f'DELETE FROM IsInCart WHERE userId = {self.userId};')

    @property
    def cart(self):
        tbl = User.select_tuples('IsInCart', ['userId'], [self.userId])
        return [x[1] for x in tbl]  # list of foodId

    def check_minimum_bill_value(self):
        tbl = User.exe_query('SELECT price, discount FROM Food JOIN IsInCart IIC ON Food.foodId = IIC.foodId '
                             f'WHERE IIC.userId = {self.userId};')
        bill_value = sum(x[0] * (100 - x[1]) / 100 for x in tbl)
        tbl = User.exe_query('SELECT "minimum-bill-value" FROM Shop JOIN Food F ON Shop.shopId = F.shopId '
                             'JOIN IsInCart IIC ON F.foodId = IIC.foodId '
                             f'WHERE IIC.userId = {self.userId};')
        if bill_value < tbl[0][0]:
            raise MinBillValueError

    def finalize_the_purchase(self, addressId, discount_code=None):
        if not self.cart:
            raise CartIsEmptyError
        self.check_minimum_bill_value()
        discountId = None
        if discount_code:
            tbl = User.exe_query(
                'SELECT DC.discountId FROM Discount JOIN DiscountCode DC ON Discount.discountId = DC.discountId '
                f'WHERE DC.userId = {self.userId};')
            if not tbl:
                raise InvalidDiscountError
            discountId = tbl[0][0]
        from entities.invoice import Invoice
        Invoice.add(addressId, self.walletId, discountId)

    @property
    def invoices(self):
        from entities.invoice import Invoice
        tbl = User.select_tuples('Invoice', ['userId'], [self.userId])
        return [Invoice(ii[5]) for ii in tbl]

    def comment(self, discountId, rate: int, text: str):
        from entities.comment import Comment
        commentId = Comment.add(rate, text)
        User.update_tuple('Invoice', 'commentId', commentId, f'discountId = {discountId}')

    def get_status(self, invoiceId):
        tbl = User.exe_query('SELECT name FROM Status JOIN Invoice I ON Status.statusId = I.statusId '
                             f'WHERE I.invoiceId = {invoiceId};')
        return tbl[0][0]

    def previous_foods(self, shopId):
        tbl = User.exe_query('SELECT F.foodId FROM Shop S JOIN Food F ON S.shopId = F.shopId '
                             'JOIN IsInInvoice III ON F.foodId = III.foodId '
                             'JOIN Invoice I ON III.invoiceId = I.invoiceId '
                             'JOIN Wallet W on I.walletId = W.walletId '
                             f'WHERE W.userId = {self.userId} AND S.shopId = {shopId};')
        return [x[0] for x in tbl]  # list of foodIds

    def search_shops(self, name='', addressId=None, categoryId=None):
        af = ''
        cf = ''
        if addressId is not None:
            from entities.address import Address
            from entities.location import Location
            li = Address(addressId).locationId
            loc = Location(li)
            af = f' AND ABS(lat - {loc.lat}) < 100 AND ABS(lon - {loc.lon}) < 100'
        if categoryId is not None:
            cf = f' AND C.categoryId = {categoryId}'
        tbl = User.exe_query("SELECT S.shopId FROM Shop S JOIN Address A ON S.addressId = A.addressId "
                             "JOIN Location L ON A.locationId = L.locationId "
                             "JOIN Food F On S.shopId = F.shopId "
                             "JOIN Category C ON F.categoryId = C.categoryId "
                             f"WHERE S.name LIKE '%{name}%'{af}{cf};")
        return [x[0] for x in tbl]  # list of shopIds

    def search_foods(self, name='', categoryId=None):
        cf = ''
        if categoryId is not None:
            cf = f' AND categoryId = {categoryId}'
        tbl = User.exe_query("SELECT foodId FROM Food "
                             f"WHERE name LIKE '%{name}%'{cf};")
        return [x[0] for x in tbl]  # list of foodIds

    def search_categories(self, name=''):
        tbl = User.exe_query("SELECT categoryId FROM Category "
                             f"WHERE name LIKE '%{name}%';")
        return [x[0] for x in tbl]  # list of categoryIds

    @property
    def favorite_shops(self):
        tbl = User.exe_query(f'SELECT shopId FROM Favorite WHERE userId = {self.userId};')
        return [x[0] for x in tbl]  # shopIds

    @property
    def comments(self):
        tbl = User.exe_query('SELECT Comment.commentId FROM Comment JOIN Invoice I on Comment.commentId = I.commentId '
                             'JOIN Wallet W on I.walletId = W.walletId '
                             f'WHERE W.userId = {self.userId};')
        return [x[0] for x in tbl]  # commentIds
