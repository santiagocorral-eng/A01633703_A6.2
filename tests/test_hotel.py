import unittest
from hotel import Hotel
from file_manager import FileManager

class TestHotel(unittest.TestCase):
 def setUp(self):
    FileManager.save_data("data/hotels.json",[])

 def test_create_hotel(self):
    hotel=Hotel("H1","Test Hotel","CDMX",10)
    Hotel.create_hotel(hotel)
    hotels=FileManager.load_data("data/hotels.json")
    self.assertEqual(len(hotels),1)

 def test_reserve_room(self):
    hotel=Hotel("H2","Hotel 2","MTY",2)
    Hotel.create_hotel(hotel)
    Hotel.reserve_room("H2")
    updated=Hotel.display_hotel("H2")
    self.assertEqual(updated["available_rooms"],1)

 def test_no_rooms_available(self):
    hotel=Hotel("H3","Hotel 3","GDL",1)
    Hotel.create_hotel(hotel)
    Hotel.reserve_room("H3")
    Hotel.reserve_room("H3")
    updated=Hotel.display_hotel("H3")
    self.assertEqual(updated["available_rooms"],0)

if __name__=="__main__":
    unittest.main()
