"""
transaction.py

Simple Transaction record used by Account.history.

Fields:
- kind: 'deposit' / 'withdraw' / 'transfer'
- amount: positive float
- note: optional short text
- time: timestamp string
"""

from utils import now

class Transaction:
    def __init__(self, kind, amount, note='', time=None):
        """
        Create a transaction entry.

        Raises ValueError if amount <= 0
        """
        if amount <= 0:
            raise ValueError("amount must be > 0")
        self.kind = kind
        self.amount = float(amount)
        self.note = note or ''
        # generate time if caller didn't pass one
        self.time = time if time else now()

    def as_dict(self):
        """Return a plain dict representation."""
        return {
            'kind': self.kind,
            'amount': self.amount,
            'note': self.note,
            'time': self.time
        }

    def __str__(self):
        """Readable single-line form for printing."""
        return f"[{self.time}] {self.kind.upper()}: Rs.{self.amount:.2f} — {self.note}"
