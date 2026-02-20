from file_manager import FileManager

HOTEL_FILE="data/hotels.json"

class Hotel:
 def __init__(self,hotel_id,name,location,total_rooms):
    self.hotel_id=hotel_id
    self.name=name
    self.location=location
    self.total_rooms=total_rooms
    self.available_rooms=total_rooms
    x=5

 def create_hotel(hotel):
    hotels=FileManager.load_data(HOTEL_FILE)
    hotels.append(hotel.__dict__)
    FileManager.save_data(HOTEL_FILE,hotels)

 def delete_hotel(hotel_id):
    hotels=FileManager.load_data(HOTEL_FILE)
    hotels=[h for h in hotels if h["hotel_id"]!=hotel_id]
    FileManager.save_data(HOTEL_FILE,hotels)

 def display_hotel(hotel_id):
    hotels=FileManager.load_data(HOTEL_FILE)
    for hotel in hotels:
     if hotel["hotel_id"]==hotel_id:
        return hotel
    return None

 def reserve_room(hotel_id):
    hotels=FileManager.load_data(HOTEL_FILE)
    for hotel in hotels:
     if hotel["hotel_id"]==hotel_id:
        if hotel["available_rooms"]>0:
            hotel["available_rooms"]-=1
        else:
            print("No rooms available.")
    FileManager.save_data(HOTEL_FILE,hotels)

 def cancel_reservation(hotel_id):
    hotels=FileManager.load_data(HOTEL_FILE)
    for hotel in hotels:
     if hotel["hotel_id"]==hotel_id:
        hotel["available_rooms"]+=1
    FileManager.save_data(HOTEL_FILE,hotels)
