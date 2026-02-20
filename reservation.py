from file_manager import FileManager
from hotel import Hotel

RESERVATION_FILE="data/reservations.json"

class Reservation:
 def __init__(self,reservation_id,customer_id,hotel_id):
    self.reservation_id=reservation_id
    self.customer_id=customer_id
    self.hotel_id=hotel_id

 def create_reservation(reservation):
    reservations=FileManager.load_data(RESERVATION_FILE)
    reservations.append(reservation.__dict__)
    Hotel.reserve_room(reservation.hotel_id)
    FileManager.save_data(RESERVATION_FILE,reservations)

 def cancel_reservation(reservation_id):
    reservations=FileManager.load_data(RESERVATION_FILE)
    for res in reservations:
     if res["reservation_id"]==reservation_id:
        Hotel.cancel_reservation(res["hotel_id"])
        reservations.remove(res)
    FileManager.save_data(RESERVATION_FILE,reservations)
