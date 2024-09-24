# Inventory Management CLI System
The Inventory Management System is a comprehensive application designed to manage products, suppliers, categories, inventories, and transactions. This system is built using Python and SQLAlchemy, providing CRUD operations for users keep track of stock levels. It allows business manage supplier information, and monitor transaction histories, providing a robust solution for inventory management.

## Models and relationships

The models represent real-world entities: Inventory, Category, Supplier and Transaction.

- Inventory-Transaction:One-to-many relationship. An inventory can have multiple transactions but a transaction is related to one inventory item.
- Category: One category can have many inventories.
- Supplier: One-to-many;A supplier can supply many inventories.
  Here a representation of the ERD relations: https://dbdiagram.io/d/Inventory_ERD-66f054a3a0828f8aa6a9bc54

## Features

- Add, update, and delete categories and suppliers
- Manage inventory items with detailed information
- Track transactions (stock in/out) for inventory items
- Search and filter functionalities for inventory and supplier records.

### Installation and set up

- Ensure you have installed Python 3.7 or higher

- Clone the repository:

```bash
   git clone https://github.com/crea-tivecoder/Inventory_management_CLI.git
   cd Inventory_management
```

- Install the required packages

```bash
pip install sqlalchemy
```

- Generating Pipenv
  Install any dependencies you'll need for your project, like SQLAlchemy and Alembic

```bash
pipenv install sqlalchemy alembic
```

### Generating Your Database

Once you're in your environment, you can start development.
Setting up your database.
`cd` into the `db` directory

- Run `alembic init migrations` to set up Alembic.
Modify line 63 in `alembic.ini` to point to the database you intend to create, then replace line 26 in `migrations/env.py` with the following:

```py
from models import Base
target_metadata = Base.metadata
```

Navigate to `db` and start creating the models.
Regularly run `alembic revision --autogenerate -m'<descriptive message>'` and
`alembic upgrade head` to track your modifications to the database and create checkpoints in case of any need to roll the modifications back.

Run `app.py` script to generate some test data.

### Generating Your CLI

A CLI is, simply put, an interactive script. You can run it with `python app.py`
or include the shebang and make it executable with `chmod +x`.

`print()` statements in the CLI script let the
user know the input message they would want to choose from.

### Usage menu

Run `python app.py` to run the application via the CLI.
The main menu allows the user to:

1.  Inventory menu

    - add inventory: Adds a new inventory item.
    - add Inventory to category: Associates an inventory with a category.
    - find inventory by id: Finds an inventory item by its ID.
    - update inventory: Modify the details of an existing inventory item
    - remove Inventory from category: Deletes an inventory from a category.

2.  Category menu
    - add category: Adds a new product category.
    - Update category: Modify a category's name or description
    -  find category by id: Finds and displays a category by ID
    - Delete category: Removes a category from the system

3.  Transaction menu
    - add transaction: Adds a new transaction (either stock-in or stock-out).
    - add transaction to Inventory: Associate a transaction with an inventory item.
    - remove transaction from inventory: Detach a transaction from an inventory item.
    - Get all transactions that belong to an inventory
    - update transaction: Modify transaction details.
    - find transaction by id: Retrieves transaction details by ID.

4.  Supplier menu
    - find supplier by id: Retrieves a supplier's details using its ID.
    - add supplier: Registers a new supplier.
    - get all supplier/stock/category: Lists all suppliers.
    - update supplier/stock/category: Updates suppliers and quantity
    - delete supplier/stock/category: Deletes supplier
