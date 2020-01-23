import re

from entities.comment import Comment
from entities.invoice import Invoice
from entities.entity import Entity
from entities.wallet import Wallet
from entities.address import Address
from entities.food import Food
from exception import LoginError, EmailIsAlreadyUsed, PhoneNumberFormatError, EmailFormatError, SignupError, \
    NotSameShopError, CartIsEmptyError, InvalidDiscountError


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
        wallet = Wallet(userId)
        cls.update_tuple('User', 'walletId', wallet.walletId, f'"userId" = \'{userId}\'')

    @classmethod
    def get_user_id(cls, phone_number):
        tbl = cls.select_tuples('User', ['phone-number'], [phone_number])
        userId = tbl[0][-2]
        return userId

    @classmethod
    def login(cls, phone_number, password):
        this_user = cls.select_tuples('User', ['phone-number', 'password'], [phone_number, password])
        if not this_user:
            raise LoginError('Invalid username or password.')
        return User(this_user[0][5])

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
        new_address = Address.add(self.userId, cityId, lat, lon)
        if street is not None:
            new_address.street = street
        if alley is not None:
            new_address.alley = alley
        if plaque is not None:
            new_address.plaque = plaque

    def get_addresses(self):
        tbl = User.select_tuples('Address', ['userId'], [self.userId])
        for address in tbl:
            pl, al, st, ai, ui, li, ci = address
            yield Address(ai, ui, ci, li, st, al, pl)

    def add_to_cart(self, foodId):
        if self.cart and Food(self.cart[0]).shopId != Food(foodId).shopId:
            raise NotSameShopError
        User.insert_tuple('IsInCart', ['userId', 'foodId'], [self.userId, foodId])

    def clear_cart(self):
        User.exe_query(f'DELETE FROM IsInCart WHERE userId = {self.userId};')

    @property
    def cart(self):
        tbl = User.select_tuples('IsInCart', ['userId'], [self.userId])
        return [x[1] for x in tbl]  # list of foodId

    def finalize_the_purchase(self, addressId, discount_code=None):
        if not self.cart:
            raise CartIsEmptyError
        discountId = None
        if discount_code:
            tbl = User.exe_query(
                'SELECT DC.discountId FROM Discount JOIN DiscountCode DC ON Discount.discountId = DC.discountId '
                f'WHERE DC.userId = {self.userId};')
            if not tbl:
                raise InvalidDiscountError
            discountId = tbl[0][0]
        Invoice.add(addressId, self.walletId, discountId)

    @property
    def invoices(self):
        tbl = User.select_tuples('Invoice', ['userId'], [self.userId])
        return [Invoice(ii[5]) for ii in tbl]

    def comment(self, discountId, rate: int, text: str):
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
