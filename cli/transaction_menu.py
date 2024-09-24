from db.tools import Session
from db.transaction import Transaction

class TransactionMenu:
    def __init__(self):
        self.session = Session()

    def run_menu(self):
        while True:
            print("\nTransaction Menu:")
            print("1. Add Transaction")
            print("2. Add Transaction to Inventory")
            print("3. Find Transaction by ID")
            print("4. Remove Transaction from Inventory")
            print("5. Update Transaction")
            print("6. Return to Main Menu")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_transaction()
            elif choice == "2":
                self.add_transaction_to_inventory()
            elif choice == "3":
                self.find_transaction_by_id()
            elif choice == "4":
                self.remove_transaction_from_inventory()
            elif choice == "5":
                self.update_transaction()
            elif choice == "6":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_transaction(self):
        transaction_type = input("Enter transaction type ('in' or 'out'): ")
        quantity = int(input("Enter transaction quantity: "))
        inventory_id = int(input("Enter inventory ID: "))

        transaction = Transaction(
            transaction_type=transaction_type,
            quantity=quantity,
            inventory_id=inventory_id
        )
        try:
            self.session.add(transaction)
            self.session.commit()
            print("Transaction added successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error adding transaction: {str(e)}")

    def add_transaction_to_inventory(self):
        transaction_id = int(input("Enter transaction ID: "))
        inventory_id = int(input("Enter inventory ID: "))
        transaction = self.session.query(Transaction).get(transaction_id)
        if transaction:
            try:
                transaction.inventory_id = inventory_id
                self.session.commit()
                print("Transaction added to inventory successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error adding transaction to inventory: {str(e)}")
        else:
            print("Transaction not found.")

    def find_transaction_by_id(self):
        transaction_id = int(input("Enter transaction ID: "))
        transaction = self.session.query(Transaction).get(transaction_id)
        if transaction:
            print(f"Transaction: ID={transaction.id}, Type={transaction.transaction_type}, Quantity={transaction.quantity}, Date={transaction.transaction_date}")
        else:
            print("Transaction not found.")

    def remove_transaction_from_inventory(self):
        transaction_id = int(input("Enter transaction ID: "))
        inventory_id = int(input("Enter inventory ID: "))
        transaction = self.session.query(Transaction).filter_by(id=transaction_id, inventory_id=inventory_id).first()
        if transaction:
            try:
                self.session.delete(transaction)
                self.session.commit()
                print("Transaction removed from inventory successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error removing transaction from inventory: {str(e)}")
        else:
            print("Transaction not found in the specified inventory.")

    def update_transaction(self):
        transaction_id = int(input("Enter transaction ID to update: "))
        transaction = self.session.query(Transaction).get(transaction_id)
        if transaction:
            new_transaction_type = input(f"Enter new transaction type (current: {transaction.transaction_type}): ")
            new_quantity = int(input(f"Enter new quantity (current: {transaction.quantity}): "))
            new_inventory_id = int(input(f"Enter new inventory ID (current: {transaction.inventory_id}): "))
            try:
                transaction.transaction_type = new_transaction_type
                transaction.quantity = new_quantity
                transaction.inventory_id = new_inventory_id
                self.session.commit()
                print("Transaction updated successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error updating transaction: {str(e)}")
        else:
            print("Transaction not found.")