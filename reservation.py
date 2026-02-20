"""Clase Reservation.

Maneja reservas de clientes en hoteles con persistencia en JSON.
"""

from file_manager import FileManager
from hotel import Hotel

RESERVATION_FILE = "data/reservations.json"


class Reservation:
    """Representa una reserva de un cliente en un hotel."""

    def __init__(self, reservation_id, customer_id, hotel_id):
        """Inicializa una reserva con ID, cliente y hotel."""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    @staticmethod
    def create_reservation(reservation):
        """
        Agrega una reserva al archivo JSON y actualiza
        habitaciones disponibles del hotel.
        """
        try:
            reservations = FileManager.load_data(RESERVATION_FILE)
        except (IOError, OSError, ValueError) as error:
            print(
                f"Error al leer el archivo de reservas: {error}"
            )
            reservations = []

        reservations.append(reservation.__dict__)

        try:
            Hotel.reserve_room(reservation.hotel_id)
        except (ValueError, KeyError, RuntimeError) as error:
            print(f"Error al reservar habitación: {error}")

        try:
            FileManager.save_data(RESERVATION_FILE, reservations)
        except (IOError, OSError) as error:
            print(f"Error al guardar reservas: {error}")

    @staticmethod
    def cancel_reservation(reservation_id):
        """
        Cancela una reserva por su ID y actualiza
        habitaciones disponibles del hotel.
        """
        try:
            reservations = FileManager.load_data(RESERVATION_FILE)
        except (IOError, OSError, ValueError) as error:
            print(
                f"Error al leer el archivo de reservas: {error}"
            )
            return

        reservation_to_cancel = None

        for res in reservations:
            if res["reservation_id"] == reservation_id:
                reservation_to_cancel = res
                break

        if reservation_to_cancel:
            try:
                Hotel.cancel_reservation(
                    reservation_to_cancel["hotel_id"]
                )
            except (ValueError, KeyError, RuntimeError) as error:
                print(
                    "Error al cancelar habitación en hotel: "
                    f"{error}"
                )

            reservations.remove(reservation_to_cancel)
        else:
            print(
                f"No se encontró la reserva con ID "
                f"{reservation_id}."
            )

        try:
            FileManager.save_data(RESERVATION_FILE, reservations)
        except (IOError, OSError) as error:
            print(f"Error al guardar reservas: {error}")
