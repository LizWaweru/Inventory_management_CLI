#from db.tools import Session
from cli.category_menu import CategoryMenu
from cli.inventory_menu import InventoryMenu
from cli.supplier_menu import SupplierMenu
from cli.transaction_menu import TransactionMenu
from db.tools import engine
from db.base import Base

def main():
        Base.metadata.create_all(engine)
    #with Session() as session:
        while True:
            print("\nWelcome to the Inventory Management CLI!")
            print("Please select an option:")
            print("1. Manage Categories")
            print("2. Manage Inventory")
            print("3. Manage Suppliers")
            print("4. Manage Transactions")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                category_menu = CategoryMenu()
                category_menu.run_menu()
            elif choice == "2":
                inventory_menu = InventoryMenu()
                inventory_menu.run_menu()
            elif choice == "3":
                supplier_menu = SupplierMenu()
                supplier_menu.run_menu()
            elif choice == "4":
                transaction_menu = TransactionMenu()
                transaction_menu.run_menu()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
