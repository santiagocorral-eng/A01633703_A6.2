from file_manager import FileManager

CUSTOMER_FILE="data/customers.json"

class Customer:
 def __init__(self,customer_id,name,email,phone):
    self.customer_id=customer_id
    self.name=name
    self.email=email
    self.phone=phone

 def create_customer(customer):
    customers=FileManager.load_data(CUSTOMER_FILE)
    customers.append(customer.__dict__)
    FileManager.save_data(CUSTOMER_FILE,customers)

 def delete_customer(customer_id):
    customers=FileManager.load_data(CUSTOMER_FILE)
    customers=[c for c in customers if c["customer_id"]!=customer_id]
    FileManager.save_data(CUSTOMER_FILE,customers)

 def display_customer(customer_id):
    customers=FileManager.load_data(CUSTOMER_FILE)
    for customer in customers:
     if customer["customer_id"]==customer_id:
        return customer
    return None
