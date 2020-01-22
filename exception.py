class SnappFoodException(Exception):
    """ Base class of following exceptions. """
    pass


class FormatError(SnappFoodException):
    pass


class SignupError(SnappFoodException):
    pass


class LoginError(SnappFoodException):
    pass


class UsernameFormatError(FormatError):
    pass


class PhoneNumberFormatError(FormatError):
    pass


class EmailFormatError(FormatError):
    pass


class EmailIsAlreadyUsed(SnappFoodException):
    pass
