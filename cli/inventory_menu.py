from db.tools import Session
from db.inventory import Inventory

class InventoryMenu:
    def __init__(self):
        self.session = Session()

    def run_menu(self):
        while True:
            print("\nInventory Menu:")
            print("1. Add Inventory")
            print("2. Add Inventory to Category")
            print("3. Find Inventory by ID")
            print("4. Remove Inventory from Category")
            print("5. Update Inventory")
            print("6. Return to Main Menu")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_inventory()
            elif choice == "2":
                self.add_inventory_to_category()
            elif choice == "3":
                self.find_inventory_by_id()
            elif choice == "4":
                self.remove_inventory_from_category()
            elif choice == "5":
                self.update_inventory()
            elif choice == "6":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_inventory(self):
        name = input("Enter inventory name: ")
        quantity = int(input("Enter inventory quantity: "))
        unit_price = float(input("Enter inventory unit price: "))
        category_id = int(input("Enter category ID: "))
        supplier_id = int(input("Enter supplier ID: "))

        inventory = Inventory(
            name=name,
            quantity=quantity,
            _unit_price=unit_price,
            category_id=category_id,
            supplier_id=supplier_id
        )
        try:
            self.session.add(inventory)
            self.session.commit()
            print("Inventory added successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error adding inventory: {str(e)}")

    def add_inventory_to_category(self):
        inventory_id = int(input("Enter inventory ID: "))
        category_id = int(input("Enter category ID: "))
        inventory = self.session.query(Inventory).get(inventory_id)
        if inventory:
            try:
                inventory.category_id = category_id
                self.session.commit()
                print("Inventory added to category successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error adding inventory to category: {str(e)}")
        else:
            print("Inventory not found.")

    def find_inventory_by_id(self):
        inventory_id = int(input("Enter inventory ID: "))
        inventory = self.session.query(Inventory).get(inventory_id)
        if inventory:
            print(f"Inventory: {inventory.name} - Quantity: {inventory.quantity}, Unit Price: {inventory.unit_price}")
        else:
            print("Inventory not found.")

    def remove_inventory_from_category(self):
        inventory_id = int(input("Enter inventory ID: "))
        category_id = int(input("Enter category ID: "))
        inventory = self.session.query(Inventory).filter_by(id=inventory_id, category_id=category_id).first()
        if inventory:
            try:
                inventory.category_id = None
                self.session.commit()
                print("Inventory removed from category successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error removing inventory from category: {str(e)}")
        else:
            print("Inventory not found in the specified category.")

    def update_inventory(self):
        inventory_id = int(input("Enter inventory ID to update: "))
        inventory = self.session.query(Inventory).get(inventory_id)
        if inventory:
            new_name = input(f"Enter new name (current: {inventory.name}): ")
            new_quantity = int(input(f"Enter new quantity (current: {inventory.quantity}): "))
            new_unit_price = float(input(f"Enter new unit price (current: {inventory.unit_price}): "))
            new_category_id = int(input(f"Enter new category ID (current: {inventory.category_id}): "))
            new_supplier_id = int(input(f"Enter new supplier ID (current: {inventory.supplier_id}): "))
            try:
                inventory.name = new_name
                inventory.quantity = new_quantity
                inventory.unit_price = new_unit_price
                inventory.category_id = new_category_id
                inventory.supplier_id = new_supplier_id
                self.session.commit()
                print("Inventory updated successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error updating inventory: {str(e)}")
        else:
            print("Inventory not found.")
