"""
report.py

Functions to format simple reports:
- account_report(account)
- bank_report(bank)
- all_accounts_report(bank)
"""

def account_report(account):
    """Return a multi-line string with account details and transactions."""
    lines = []
    lines.append(f"Account: {account.name} ({account.account_id})")
    lines.append(f"Balance: Rs.{account.balance:.2f}")
    lines.append("Transactions:")
    hist = account.get_history()
    if not hist:
        lines.append("  No transactions yet.")
    else:
        for tx in hist:
            lines.append(f"  {tx}")   # tx.__str__ is used
    return "\n".join(lines)

def bank_report(bank):
    """One-line stats for the bank plus totals."""
    total_acc = len(bank.accounts)
    total_bal = bank.total_balance()
    return f"Bank: {total_acc} accounts | Total balance: Rs.{total_bal:.2f}"

def all_accounts_report(bank):
    """List all accounts with id, name and balance (multi-line)."""
    lines = ["All accounts:"]
    if not bank.accounts:
        lines.append("  (none)")
    else:
        for a in bank.list_accounts():
            lines.append(f"  {a.account_id} | {a.name} | Rs.{a.balance:.2f}")
    return "\n".join(lines)
