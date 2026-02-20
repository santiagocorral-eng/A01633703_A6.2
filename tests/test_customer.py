"""
Unit tests for Customer class.
"""

import os
import unittest
from customer import Customer
from file_manager import FileManager

TEST_FILE = "data/customers.json"


class TestCustomer(unittest.TestCase):
    """Test suite for Customer operations."""

    def setUp(self):
        """Prepare clean test environment."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_create_customer_success(self):
        """Positive test: customer is created correctly."""
        customer = Customer(
            "C001",
            "Juan Perez",
            "juan@email.com",
            "5551234567",
        )

        Customer.create_customer(customer)

        data = FileManager.load_data(TEST_FILE)
        self.assertEqual(len(data), 1)

    def test_delete_non_existing_customer(self):
        """Negative test: deleting non-existing customer."""
        Customer.delete_customer("INVALID")

    def test_display_non_existing_customer(self):
        """Negative test: display customer that does not exist."""
        result = Customer.display_customer("NOT_FOUND")
        self.assertIsNone(result)

    def test_invalid_json_file(self):
        """Negative test: corrupted JSON file handling."""
        os.makedirs("data", exist_ok=True)
        with open(TEST_FILE, "w", encoding="utf-8") as file:
            file.write("INVALID JSON")

        result = Customer.display_customer("C001")
        self.assertIsNone(result)

    def test_create_multiple_customers(self):
        """Positive test: multiple customers stored."""
        c1 = Customer("C001", "Juan", "a@mail.com", "111")
        c2 = Customer("C002", "Ana", "b@mail.com", "222")

        Customer.create_customer(c1)
        Customer.create_customer(c2)

        data = FileManager.load_data(TEST_FILE)
        self.assertEqual(len(data), 2)


if __name__ == "__main__":
    unittest.main()
