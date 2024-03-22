import hotel


hotel1 = hotel.Hotel("Hotel 1")
hotel1.add_room(101, 100)
hotel1.add_room(102, 200)
hotel1.add_room(103, 300)
hotel1.add_room(103, 400)

hotel1.add_guest("John", "Doe", "passport", "123456", "123456789")
hotel1.add_guest("Jane", "Doe", "passport", "123457", "123456788")
hotel1.add_guest("Jack", "Doe", "passport", "123456", "123456787")
hotel1.add_guest("Jack", "Doe", "driving license", "123456", "123456787")
hotel1.show_current_guests()
hotel1.show_guests_database()
hotel1.book_room(103, 1)
hotel1.show_available_rooms()
hotel1.show_booked_rooms()
hotel1.show_current_guests()




