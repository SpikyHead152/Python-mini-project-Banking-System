"""
bank.py

Bank: manages multiple Account objects.
Keep a dict self.accounts mapping id -> Account.
"""

from account import Account
from exceptions import AccountNotFoundError, DuplicateAccountError
from utils import make_id

class Bank:
    def __init__(self):
        self.accounts = {}   # { account_id: Account }

    def create_account(self, name, initial_balance=0.0):
        """
        Create a new account, generate a unique id and return the Account object.
        If collision happens (very unlikely) we regenerate until unique.
        """
        acct_id = make_id()
        while acct_id in self.accounts:
            acct_id = make_id()
        acc = Account(acct_id, name, initial_balance)
        self.accounts[acct_id] = acc
        return acc

    def get_account(self, account_id):
        """
        Retrieve account by id or raise AccountNotFoundError.
        """
        acc = self.accounts.get(account_id)
        if not acc:
            raise AccountNotFoundError(f"account {account_id} not found")
        return acc

    def transfer_between_accounts(self, from_id, to_id, amount, note=''):
        """
        Transfer amount from one account to another.
        Raises AccountNotFoundError if either id missing; other validations
        are handled by Account.transfer().
        """
        if from_id == to_id:
            raise ValueError("cannot transfer to same account")
        src = self.get_account(from_id)
        dst = self.get_account(to_id)
        src.transfer(dst, amount, note)

    def total_balance(self):
        """Return sum of all account balances (float)."""
        total = 0.0
        for a in self.accounts.values():
            total += a.balance
        return total

    def list_accounts(self):
        """Return list of Account objects."""
        return list(self.accounts.values())
