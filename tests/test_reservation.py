import unittest
from reservation import Reservation
from hotel import Hotel
from customer import Customer
from file_manager import FileManager

class TestReservation(unittest.TestCase):
 def setUp(self):
    FileManager.save_data("data/reservations.json",[])
    FileManager.save_data("data/hotels.json",[])
    FileManager.save_data("data/customers.json",[])

 def test_create_reservation(self):
    hotel=Hotel("H1","Test Hotel","CDMX",5)
    Hotel.create_hotel(hotel)
    customer=Customer("C1","Juan","juan@mail.com","123")
    Customer.create_customer(customer)
    res=Reservation("R1","C1","H1")
    Reservation.create_reservation(res)
    reservations=FileManager.load_data("data/reservations.json")
    self.assertEqual(len(reservations),1)
    updated=Hotel.display_hotel("H1")
    self.assertEqual(updated["available_rooms"],4)

 def test_cancel_reservation(self):
    hotel=Hotel("H2","Hotel 2","MTY",2)
    Hotel.create_hotel(hotel)
    customer=Customer("C2","Ana","ana@mail.com","321")
    Customer.create_customer(customer)
    res=Reservation("R2","C2","H2")
    Reservation.create_reservation(res)
    Reservation.cancel_reservation("R2")
    reservations=FileManager.load_data("data/reservations.json")
    self.assertEqual(len(reservations),0)
    updated=Hotel.display_hotel("H2")
    self.assertEqual(updated["available_rooms"],2)

if __name__=="__main__":
    unittest.main()
