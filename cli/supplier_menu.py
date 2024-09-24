from db.tools import Session
from db.supplier import Supplier

class SupplierMenu:
    def __init__(self):
        self.session = Session()

    def run_menu(self):
        while True:
            print("\nSupplier Menu:")
            print("1. Add Supplier")
            print("2. Find Supplier by ID")
            print("3. Get All Suppliers")
            print("4. Update Supplier")
            print("5. Delete Supplier")
            print("6. Return to Main Menu")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_supplier()
            elif choice == "2":
                self.find_supplier_by_id()
            elif choice == "3":
                self.get_all_suppliers()
            elif choice == "4":
                self.update_supplier()
            elif choice == "5":
                self.delete_supplier()
            elif choice == "6":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_supplier(self):
        name = input("Enter supplier name: ")
        email = input("Enter supplier email: ")
        phone = input("Enter supplier phone number: ")
        address = input("Enter supplier address: ")

        supplier = Supplier(name=name, email=email, phone=phone, address=address)
        try:
            self.session.add(supplier)
            self.session.commit()
            print("Supplier added successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error adding supplier: {str(e)}")

    def find_supplier_by_id(self):
        supplier_id = int(input("Enter supplier ID: "))
        supplier = self.session.query(Supplier).get(supplier_id)
        if supplier:
            print(f"Supplier: {supplier.name} - Email: {supplier.email}, Phone: {supplier.phone}, Address: {supplier.address}")
        else:
            print("Supplier not found.")

    def get_all_suppliers(self):
        suppliers = self.session.query(Supplier).all()
        if suppliers:
            print("All Suppliers:")
            [print(f"ID: {supplier.id}, Name: {supplier.name}, Email: {supplier.email}, Phone: {supplier.phone}, Address: {supplier.address}") for supplier in suppliers]
        else:
            print("No suppliers found.")

    def update_supplier(self):
        supplier_id = int(input("Enter supplier ID to update: "))
        supplier = self.session.query(Supplier).get(supplier_id)
        if supplier:
            new_name = input(f"Enter new name (current: {supplier.name}): ")
            new_email = input(f"Enter new email (current: {supplier.email}): ")
            new_phone = input(f"Enter new phone number (current: {supplier.phone}): ")
            new_address = input(f"Enter new address (current: {supplier.address}): ")
            try:
                supplier.name = new_name
                supplier.email = new_email
                supplier.phone = new_phone
                supplier.address =new_address
                self.session.commit()
                print("Supplier updated successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error updating supplier: {str(e)}")
        else:
            print("Supplier not found.")

    def delete_supplier(self):
        supplier_id = int(input("Enter supplier ID to delete: "))
        supplier = self.session.query(Supplier).get(supplier_id)
        if supplier:
            try:
                self.session.delete(supplier)
                self.session.commit()
                print("Supplier deleted successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error deleting supplier: {str(e)}")
        else:
            print("Supplier not found.")