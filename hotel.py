"""Clase Hotel y operaciones para gestión de hoteles en archivo JSON."""
from file_manager import FileManager

HOTEL_FILE = "data/hotels.json"


class Hotel:
    """Representa un hotel con sus datos y operaciones sobre archivo JSON."""

    def __init__(self, hotel_id, name, location, total_rooms):
        """Inicializa un hotel con ID, nombre, ubicación y número
        total de habitaciones."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms

    @staticmethod
    def create_hotel(hotel):
        """Agrega un hotel al archivo JSON."""
        hotels = FileManager.load_data(HOTEL_FILE)
        hotels.append(hotel.__dict__)
        FileManager.save_data(HOTEL_FILE, hotels)

    @staticmethod
    def delete_hotel(hotel_id):
        """Elimina un hotel del archivo JSON por su ID."""
        hotels = FileManager.load_data(HOTEL_FILE)
        hotels = [
            h for h in hotels if h["hotel_id"] != hotel_id
        ]
        FileManager.save_data(HOTEL_FILE, hotels)

    @staticmethod
    def display_hotel(hotel_id):
        """Devuelve un hotel por su ID, o None si no existe."""
        hotels = FileManager.load_data(HOTEL_FILE)
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    @staticmethod
    def reserve_room(hotel_id):
        """Disminuye en 1 las habitaciones disponibles de un hotel."""
        hotels = FileManager.load_data(HOTEL_FILE)
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                if hotel["available_rooms"] > 0:
                    hotel["available_rooms"] -= 1
                else:
                    print("No rooms available.")
        FileManager.save_data(HOTEL_FILE, hotels)

    @staticmethod
    def cancel_reservation(hotel_id):
        """Aumenta en 1 las habitaciones disponibles de un hotel."""
        hotels = FileManager.load_data(HOTEL_FILE)
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel["available_rooms"] += 1
        FileManager.save_data(HOTEL_FILE, hotels)
