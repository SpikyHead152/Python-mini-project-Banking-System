"""
main.py

A simple CLI to interact with the Bank instance.

"""

from bank import Bank
from report import account_report, bank_report, all_accounts_report
from exceptions import AccountNotFoundError, InsufficientFundsError, InvalidAmountError

def main():
    bank = Bank()
    while True:
        print("\n--- Simple Banking Menu ---")
        print("1) Create account")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Transfer")
        print("5) Account summary")
        print("6) Bank summary")
        print("7) List all accounts")
        print("0) Exit")
        choice = input("Choose: ").strip()

        try:
            if choice == '1':
                name = input("Holder name: ").strip()
                if not name:
                    print("Name required.")
                    continue
                bal_input = input("Initial balance (press Enter for 0): ").strip()
                bal = float(bal_input) if bal_input else 0.0
                acc = bank.create_account(name, bal)
                print(f"Created: {acc.account_id}")

            elif choice == '2':
                aid = input("Account id: ").strip()
                amt = float(input("Amount to deposit: ").strip())
                acc = bank.get_account(aid)
                acc.deposit(amt, note='deposit via CLI')
                print("Deposit ok.")

            elif choice == '3':
                aid = input("Account id: ").strip()
                amt = float(input("Amount to withdraw: ").strip())
                acc = bank.get_account(aid)
                acc.withdraw(amt, note='withdraw via CLI')
                print("Withdraw ok.")

            elif choice == '4':
                src = input("From account id: ").strip()
                dst = input("To account id: ").strip()
                amt = float(input("Amount to transfer: ").strip())
                note = input("Optional note: ").strip()
                bank.transfer_between_accounts(src, dst, amt, note)
                print("Transfer ok.")

            elif choice == '5':
                aid = input("Account id: ").strip()
                acc = bank.get_account(aid)
                print(account_report(acc))

            elif choice == '6':
                print(bank_report(bank))

            elif choice == '7':
                print(all_accounts_report(bank))

            elif choice == '0':
                print("Bye.")
                break

            else:
                print("Invalid option, try again.")

        except AccountNotFoundError as e:
            print("Error:", e)
        except (InvalidAmountError, InsufficientFundsError, ValueError) as e:
            # ValueError covers float() parsing errors too
            print("Operation failed:", e)
        except Exception as e:
            # catch-all so the program doesn't crash during demo
            print("Unexpected error:", e)

if __name__ == '__main__':
    main()
