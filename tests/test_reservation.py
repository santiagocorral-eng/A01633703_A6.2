"""
Unit tests for Reservation class.
"""

import os
import unittest
from reservation import Reservation
from hotel import Hotel
from file_manager import FileManager

RESERVATION_FILE = "data/reservations.json"
HOTEL_FILE = "data/hotels.json"


class TestReservation(unittest.TestCase):
    """Test suite for Reservation operations."""

    def setUp(self):
        """Prepare clean test environment."""
        os.makedirs("data", exist_ok=True)
        FileManager.save_data(RESERVATION_FILE, [])
        FileManager.save_data(HOTEL_FILE, [])

        # create a hotel for reservation tests
        hotel = Hotel("H100", "Hotel Test", "CDMX", 5)
        Hotel.create_hotel(hotel)

    def test_create_reservation(self):
        """Positive test: create reservation successfully."""
        reservation = Reservation("R1", "C1", "H100")
        Reservation.create_reservation(reservation)

        data = FileManager.load_data(RESERVATION_FILE)
        self.assertEqual(len(data), 1)

    def test_cancel_reservation(self):
        """Positive test: cancel reservation."""
        reservation = Reservation("R2", "C1", "H100")
        Reservation.create_reservation(reservation)

        Reservation.cancel_reservation("R2")

        data = FileManager.load_data(RESERVATION_FILE)
        self.assertEqual(len(data), 0)

    def test_cancel_non_existing_reservation(self):
        """Negative test: cancel reservation that does not exist."""
        Reservation.cancel_reservation("INVALID_ID")

    def test_create_reservation_invalid_hotel(self):
        """Negative test: reservation with invalid hotel."""
        reservation = Reservation("R3", "C1", "INVALID")
        Reservation.create_reservation(reservation)

    def test_invalid_json_file(self):
        """Negative test: corrupted reservations JSON."""
        with open(RESERVATION_FILE, "w", encoding="utf-8") as file:
            file.write("INVALID JSON")

        Reservation.cancel_reservation("R1")


if __name__ == "__main__":
    unittest.main()
