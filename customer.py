"""
Customer class: manages customers and persistence in JSON files.
"""

from file_manager import FileManager

CUSTOMER_FILE = "data/customers.json"


class Customer:
    """
    Represents a customer and operations over the JSON customer file.
    """

    def __init__(self, customer_id, name, email, phone):
        """Initialize a customer with ID, name, email and phone."""
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    @staticmethod
    def create_customer(customer):
        """Add a customer to the JSON file."""
        try:
            customers = FileManager.load_data(CUSTOMER_FILE)
        except (IOError, ValueError, TypeError) as error:
            print(f"Error loading customers: {error}")
            customers = []

        customers.append(customer.__dict__)

        try:
            FileManager.save_data(CUSTOMER_FILE, customers)
        except IOError as error:
            print(f"Error saving customers: {error}")

    @staticmethod
    def delete_customer(customer_id):
        """Delete a customer from the JSON file by ID."""
        try:
            customers = FileManager.load_data(CUSTOMER_FILE)
        except (IOError, ValueError, TypeError) as error:
            print(f"Error loading customers: {error}")
            return

        customers = [
            customer for customer in customers
            if customer["customer_id"] != customer_id
        ]

        try:
            FileManager.save_data(CUSTOMER_FILE, customers)
        except IOError as error:
            print(f"Error saving customers: {error}")

    @staticmethod
    def display_customer(customer_id):
        """Return a customer by ID or None if not found."""
        try:
            customers = FileManager.load_data(CUSTOMER_FILE)
        except (IOError, ValueError, TypeError) as error:
            print(f"Error loading customers: {error}")
            return None

        for customer in customers:
            if customer["customer_id"] == customer_id:
                return customer

        return None
