"""
account.py

Account class:
- stores id, owner name, balance
- keeps a list of Transaction objects in `history`
- deposit(), withdraw(), transfer(), get_history()
"""

from transaction import Transaction
from exceptions import InsufficientFundsError, InvalidAmountError

class Account:
    def __init__(self, account_id, name, balance=0.0):
        """
        Create account.
        - account_id : string
        - name : account holder name
        - balance : starting balance (must be >= 0)
        """
        if balance < 0:
            raise ValueError("initial balance cannot be negative")
        self.account_id = account_id
        self.name = name
        self.balance = float(balance)
        self.history = []   # list of Transaction

    def deposit(self, amount, note=''):
        """
        Add money to account and record transaction.
        Raises InvalidAmountError for non-positive amount.
        """
        if amount <= 0:
            raise InvalidAmountError("deposit amount must be > 0")
        self.balance += amount
        t = Transaction('deposit', amount, note)
        self.history.append(t)

    def withdraw(self, amount, note=''):
        """
        Remove money if enough balance and record transaction.
        Raises InvalidAmountError or InsufficientFundsError.
        """
        if amount <= 0:
            raise InvalidAmountError("withdraw amount must be > 0")
        if amount > self.balance:
            raise InsufficientFundsError("not enough balance")
        self.balance -= amount
        t = Transaction('withdraw', amount, note)
        self.history.append(t)

    def transfer(self, target_account, amount, note=''):
        """
        Transfer money to another Account object.
        Records a transfer tx on both accounts with small notes.
        Raises InvalidAmountError or InsufficientFundsError.
        """
        if amount <= 0:
            raise InvalidAmountError("transfer amount must be > 0")
        if amount > self.balance:
            raise InsufficientFundsError("not enough balance to transfer")
        # debit self
        self.balance -= amount
        note_out = (f"to {target_account.account_id}. " + note).strip()
        tx_out = Transaction('transfer', amount, note_out)
        self.history.append(tx_out)

        # credit target
        target_account.balance += amount
        note_in = (f"from {self.account_id}. " + note).strip()
        tx_in = Transaction('transfer', amount, note_in)
        target_account.history.append(tx_in)

    def get_history(self):
        """Return a copy of transaction history (list of Transaction)."""
        return list(self.history)

    def __str__(self):
        """Simple printable representation."""
        return f"Account[{self.account_id}] {self.name} | Balance: Rs.{self.balance:.2f}"
