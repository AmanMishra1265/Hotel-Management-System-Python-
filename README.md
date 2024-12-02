

# Hotel Management System (Python)

## Overview
The **Hotel Management System** is a Python-based application designed to automate key hotel operations, including room bookings, room service requests, billing, and record-keeping. It simplifies hotel management by providing an easy-to-use console interface for both hotel staff and customers to manage reservations and services.

## Features
- **Room Information**: View the availability status of rooms (Available/Booked).
- **Booking a Room**: Allows customers to book available rooms.
- **Room Service**: Customers can request services such as food and laundry for their rooms.
- **Billing**: Generate a bill based on room service charges.

## Requirements
- Python 3.x or higher
- A basic understanding of Python programming concepts

## Installation Instructions
1. Clone the repository or download the project files to your local machine.
2. Open the project folder in your preferred IDE or text editor.
3. Run the Python script `hotel_management_system.py`.

## Usage
### Menu Options:
1. **Show Room Information**: Displays the list of rooms and their availability (Available or Booked).
2. **Book a Room**: Allows you to book a room by entering the room number and your name.
3. **Room Service**: Request room service, such as food or laundry, for a booked room.
4. **Generate Bill**: View the bill for a booked room, including room service charges.

### Example Workflow:
1. Run the application and enter the hotel name and number of rooms.
2. Choose option 1 to view room availability.
3. Choose option 2 to book a room.
4. Choose option 3 to request room service.
5. Choose option 4 to generate a bill for your booking.
6. Exit the system by selecting option 5.

## Sample Output
```
Enter Hotel Name: Sunshine Hotel
Enter number of rooms: 5

--- Hotel Management System ---
1. Show Room Information
2. Book a Room
3. Room Service
4. Generate Bill
5. Exit
Choose an option: 1

--- Hotel Room Information ---
Room 1: Available
Room 2: Available
Room 3: Available
Room 4: Available
Room 5: Available
```

```
Choose an option: 2
Enter room number to book: 1
Enter your name: John Doe
Room 1 successfully booked for John Doe.

Choose an option: 3
Enter room number for room service: 1
1. Food
2. Laundry
Choose service (1 or 2): 1
Food service provided. Charges: $20

Choose an option: 4
Enter room number to generate bill: 1

--- Bill for Room 1 ---
Customer Name: John Doe
Room Service Charges: $20
Total Amount: $70
```

## Code Structure
- **hotel.py**: Defines the `Hotel` class, managing room details, bookings, and room service.
- **hotel_management_system.py**: The main program that provides the user interface, allowing users to interact with the hotel management system.
  
## Possible Enhancements
- **User Authentication**: Implement a login system for customers and hotel staff.
- **Database Integration**: Store bookings and room service records in a database (e.g., SQLite or MySQL).
- **GUI**: Develop a graphical user interface using libraries like `Tkinter` for an improved user experience.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- This project is a basic implementation of hotel management functions. It is designed for educational purposes and can be extended with additional features such as check-out functionality, room categories, and more.
