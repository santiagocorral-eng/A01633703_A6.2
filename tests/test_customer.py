import unittest
from customer import Customer
from file_manager import FileManager

class TestCustomer(unittest.TestCase):
 def setUp(self):
    FileManager.save_data("data/customers.json",[])

 def test_create_customer(self):
    customer=Customer("C1","Juan Perez","juan@mail.com","1234567890")
    Customer.create_customer(customer)
    customers=FileManager.load_data("data/customers.json")
    self.assertEqual(len(customers),1)

 def test_display_customer(self):
    customer=Customer("C2","Ana Lopez","ana@mail.com","0987654321")
    Customer.create_customer(customer)
    c=Customer.display_customer("C2")
    self.assertEqual(c["name"],"Ana Lopez")

if __name__=="__main__":
    unittest.main()
