"""
Custom exceptions used in the banking system.
"""

class AccountNotFoundError(Exception):
    """Raised when an account id is missing from the bank."""
    pass

class DuplicateAccountError(Exception):
    """Raised when attempting to create an already existing account id."""
    pass

class InsufficientFundsError(Exception):
    """Raised when balance is not enough for withdrawal/transfer."""
    pass

class InvalidAmountError(Exception):
    """Raised when amount is invalid (<= 0)."""
    pass
