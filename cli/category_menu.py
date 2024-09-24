from db.tools import Session
from db.category import Category

class CategoryMenu:
    def __init__(self):
        self.session = Session()

    def run_menu(self):
        while True:
            print("\nCategory Menu:")
            print("1. Add Category")
            print("2. Find Category by ID")
            print("3. Get All Categories")
            print("4. Update Category")
            print("5. Delete Category")
            print("6. Return to Main Menu")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.add_category()
            elif choice == "2":
                self.find_category_by_id()
            elif choice == "3":
                self.get_all_categories()
            elif choice == "4":
                self.update_category()
            elif choice == "5":
                self.delete_category()
            elif choice == "6":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_category(self):
        name = input("Enter category name: ")
        description = input("Enter category description: ")

        category = Category(name=name, description=description)
        try:
            self.session.add(category)
            self.session.commit()
            print("Category added successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error adding category: {str(e)}")

    def find_category_by_id(self):
        category_id = int(input("Enter category ID: "))
        category = self.session.query(Category).get(category_id)
        if category:
            print(f"Category: {category.name} - {category.description}")
        else:
            print("Category not found.")

    def get_all_categories(self):
        categories = self.session.query(Category).all()
        if categories:
            print("All Categories:")
            [print(f"ID: {category.id}, Name: {category.name}, Description: {category.description}:") for category in categories]
        else:
            print("No categories found.")

    def update_category(self):
        category_id = int(input("Enter category ID to update: "))
        category = self.session.query(Category).get(category_id)
        if category:
            new_name = input(f"Enter new name (current: {category.name}): ")
            new_description = input(f"Enter new description (current: {category.description}): ")
            try:
                category.name = new_name
                category.description = new_description
                self.session.commit()
                print("Category updated successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error updating category: {str(e)}")
        else:
            print("Category not found.")

    def delete_category(self):
        category_id = int(input("Enter category ID to delete: "))
        category = self.session.query(Category).get(category_id)
        if category:
            try:
                self.session.delete(category)
                self.session.commit()
                print("Category deleted successfully.")
            except Exception as e:
                self.session.rollback()
                print(f"Error deleting category: {str(e)}")
        else:
            print("Category not found.")
