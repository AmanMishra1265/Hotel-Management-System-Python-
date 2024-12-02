class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms  # A dictionary where key is room number, value is availability status
        self.booked_rooms = {}

    def show_room_info(self):
        print("\n--- Hotel Room Information ---")
        for room_number, available in self.rooms.items():
            status = "Available" if available else "Booked"
            print(f"Room {room_number}: {status}")

    def book_room(self):
        room_number = int(input("Enter room number to book: "))
        if room_number in self.rooms and self.rooms[room_number]:
            self.rooms[room_number] = False
            self.booked_rooms[room_number] = {}
            name = input("Enter your name: ")
            self.booked_rooms[room_number]['Name'] = name
            self.booked_rooms[room_number]['Room Service Charges'] = 0
            print(f"Room {room_number} successfully booked for {name}.")
        else:
            print(f"Room {room_number} is either unavailable or already booked.")

    def provide_room_service(self):
        room_number = int(input("Enter room number for room service: "))
        if room_number in self.booked_rooms:
            print("1. Food")
            print("2. Laundry")
            choice = int(input("Choose service (1 or 2): "))
            if choice == 1:
                cost = 20
                print(f"Food service provided. Charges: ${cost}")
                self.booked_rooms[room_number]['Room Service Charges'] += cost
            elif choice == 2:
                cost = 15
                print(f"Laundry service provided. Charges: ${cost}")
                self.booked_rooms[room_number]['Room Service Charges'] += cost
            else:
                print("Invalid choice.")
        else:
            print("Room not booked or invalid room number.")

    def generate_bill(self):
        room_number = int(input("Enter room number to generate bill: "))
        if room_number in self.booked_rooms:
            print(f"\n--- Bill for Room {room_number} ---")
            name = self.booked_rooms[room_number]['Name']
            room_service_charges = self.booked_rooms[room_number]['Room Service Charges']
            print(f"Customer Name: {name}")
            print(f"Room Service Charges: ${room_service_charges}")
            total = room_service_charges + 50  # Adding a fixed room charge
            print(f"Total Amount: ${total}")
        else:
            print("Room not booked or invalid room number.")

class HotelManagementSystem:
    def __init__(self, hotel_name, room_count):
        rooms = {i: True for i in range(1, room_count + 1)}  # Initialize all rooms as available
        self.hotel = Hotel(hotel_name, rooms)

    def display_menu(self):
        while True:
            print("\n--- Hotel Management System ---")
            print("1. Show Room Information")
            print("2. Book a Room")
            print("3. Room Service")
            print("4. Generate Bill")
            print("5. Exit")
            choice = int(input("Choose an option: "))
            if choice == 1:
                self.hotel.show_room_info()
            elif choice == 2:
                self.hotel.book_room()
            elif choice == 3:
                self.hotel.provide_room_service()
            elif choice == 4:
                self.hotel.generate_bill()
            elif choice == 5:
                print("Thank you for using the Hotel Management System!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    hotel_name = input("Enter Hotel Name: ")
    room_count = int(input("Enter number of rooms: "))
    system = HotelManagementSystem(hotel_name, room_count)
    system.display_menu()
