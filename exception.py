class SnappFoodException(Exception):
    """ Base class of following exceptions. """
    pass


class FormatError(SnappFoodException):
    pass


class UsernameFormatError(FormatError):
    pass


class PhoneNumberFormatError(FormatError):
    pass


class EmailFormatError(FormatError):
    pass
