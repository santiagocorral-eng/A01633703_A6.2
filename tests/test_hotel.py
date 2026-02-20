"""
Unit tests for Hotel class.
"""

import os
import unittest
from hotel import Hotel
from file_manager import FileManager

HOTEL_FILE = "data/hotels.json"


class TestHotel(unittest.TestCase):
    """Test suite for Hotel operations."""

    def setUp(self):
        """Prepare clean environment before each test."""
        os.makedirs("data", exist_ok=True)
        FileManager.save_data(HOTEL_FILE, [])

    def test_create_hotel(self):
        """Positive test: create a hotel."""
        hotel = Hotel("H1", "Test Hotel", "CDMX", 10)
        Hotel.create_hotel(hotel)

        hotels = FileManager.load_data(HOTEL_FILE)
        self.assertEqual(len(hotels), 1)

    def test_reserve_room(self):
        """Positive test: reserve a room successfully."""
        hotel = Hotel("H2", "Hotel 2", "MTY", 2)
        Hotel.create_hotel(hotel)

        Hotel.reserve_room("H2")
        updated = Hotel.display_hotel("H2")

        self.assertEqual(updated["available_rooms"], 1)

    def test_no_rooms_available(self):
        """Negative test: reserve when no rooms available."""
        hotel = Hotel("H3", "Hotel 3", "GDL", 1)
        Hotel.create_hotel(hotel)

        Hotel.reserve_room("H3")
        Hotel.reserve_room("H3")  # should not go below 0

        updated = Hotel.display_hotel("H3")
        self.assertEqual(updated["available_rooms"], 0)

    def test_reserve_non_existing_hotel(self):
        """Negative test: reserving non-existing hotel."""
        Hotel.reserve_room("INVALID_ID")

    def test_display_non_existing_hotel(self):
        """Negative test: display hotel that does not exist."""
        result = Hotel.display_hotel("NOT_FOUND")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
