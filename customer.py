"""Módulo Customer: define la clase Customer y sus operaciones sobre JSON."""

from file_manager import FileManager

CUSTOMER_FILE = "data/customers.json"


class Customer:
    """Representa a un cliente y operaciones sobre archivo JSON."""

    def __init__(self, customer_id, name, email, phone):
        """Inicializa un cliente con ID, nombre, email y teléfono."""
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    @staticmethod
    def create_customer(customer):
        """Agrega un cliente al archivo JSON."""
        customers = FileManager.load_data(CUSTOMER_FILE)
        customers.append(customer.__dict__)
        FileManager.save_data(CUSTOMER_FILE, customers)

    @staticmethod
    def delete_customer(customer_id):
        """Elimina un cliente del archivo JSON por su ID."""
        customers = FileManager.load_data(CUSTOMER_FILE)
        customers = [
            c for c in customers if c["customer_id"] != customer_id
        ]
        FileManager.save_data(CUSTOMER_FILE, customers)

    @staticmethod
    def display_customer(customer_id):
        """Devuelve un cliente por su ID, o None si no existe."""
        customers = FileManager.load_data(CUSTOMER_FILE)
        for customer in customers:
            if customer["customer_id"] == customer_id:
                return customer
        return None
