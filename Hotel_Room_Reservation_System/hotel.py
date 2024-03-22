class HotelErrorCode(Exception):
    pass

class Room:
    def __init__(self, room_number, room_price):
        self.room_number = room_number
        self.room_price = room_price
        self.is_available = True
        self.guest_system_id = 0


class Guest:
    def __init__(self, name, surname, id_kind, id_number, phone_number, guest_system_id):
        self.guest_system_id = guest_system_id
        self.name = name
        self.surname = surname
        self.id_kind = id_kind
        self.id_number = id_number
        self.phone_number = phone_number


class Hotel:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = {}
        self.guests = {}


    def add_room(self, room_number, room_price):
        print(f"Adding room: {room_number} with price: {room_price}")
        if room_number in self.rooms:
            print("Room already exists")
        else:
            self.rooms[room_number] = Room(room_number, room_price)
            print(f"Room: {room_number} added with price: {room_price}")


    def add_guest(self, name, surname, id_kind, id_number, phone_number):
        print(f"Adding guest: {name} {surname} with ID: {id_kind}: {id_number} and phone number: {phone_number}")
        guest_system_id = len(self.guests) + 1
        if any(guest.id_number == id_number and guest.id_kind == id_kind for guest in self.guests.values()):
            print("Guest already exists")
        else:
            self.guests[guest_system_id] = Guest(name, surname, id_kind, id_number, phone_number, guest_system_id)
            print(f"Guest {name} {surname} added with ID: {id_kind}: {id_number} and phone number: {phone_number}")

    def show_rooms(self):
        print(f"Showing all rooms in: {self.hotel_name}")
        for room_number, room in self.rooms.items():
            print(f"Room number: {room.room_number}, price: {room.room_price}, availability: {room.is_available}")

    def show_available_rooms(self):
        print(f"Showing available rooms in {self.hotel_name}")
        for room_number, room in self.rooms.items():
            if room.is_available:
                print(f"Room number: {room.room_number}, price: {room.room_price}, availability: {room.is_available}")

    def show_booked_rooms(self):
        print(f"Showing booked rooms in {self.hotel_name}")
        for room_number, room in self.rooms.items():
            if not room.is_available:
                print(f"Room number: {room.room_number}, price: {room.room_price}, availability: {room.is_available}")

    def show_current_guests(self):
        print(f"Showing all guests in {self.hotel_name}")
        hotel_empty = True
        for guest in self.guests.values():
            if any(room.guest_system_id == guest.guest_system_id for room in self.rooms.values()):
                hotel_empty = False
                print(f"System ID: {guest.guest_system_id} Name: {guest.name}, Surname: {guest.surname}, ID: {guest.id_kind} {guest.id_number}, phone number: {guest.phone_number}")
        if hotel_empty:
            print("Hotel is empty")

    def show_guests_database(self):
        print(f"Showing guests database in {self.hotel_name}")
        for guest_system_id, guest in self.guests.items():
            print(f"System ID: {guest.guest_system_id}Name: {guest.name}, Surname: {guest.surname}, ID: {guest.id_kind} {guest.id_number}, phone number: {guest.phone_number}")

    def book_room(self, room_number, guest_system_id):
        print(f"Booking room: {room_number} for guest: {guest_system_id}")
        if room_number in self.rooms:
            room = self.rooms[room_number]
            if room.is_available:
                room.is_available = False
                room.guest_system_id = guest_system_id
                print(f"Room: {room_number} booked for guest ID: {guest_system_id}")
            else:
                print(f"Room: {room_number} is not available")
        else:
            print(f"Room: {room_number} not found")

    def room_checkout(self, room_number):
        print(f"Checking out room {room_number}")
        if room_number in self.rooms:
            room = self.rooms[room_number]
            if not room.is_available:
                room.is_available = True
                room.guest_id = 0
            else:
                print(f"Room {room_number} is already available")
        else:
            print(f"Room: {room_number} not found")





