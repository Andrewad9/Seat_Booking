How It Works
  The program initializes the seat map with a set of available (True) and booked (False) seats.
  The user is prompted to input the number of seats they want to book (1-7).
  The system will attempt to book the seats row by row, trying to find contiguous seats in a row first. If enough seats are not available in one row, it will try to book from nearby rows.
  After booking, the updated seat map is displayed with the newly booked seats marked as unavailable.
  The process continues until the user opts to stop making bookings.
Edge Cases
  If a user requests more than the available number of seats, the system will attempt to book seats across multiple rows. If it can't find enough seats, the booking fails, and the system notifies the user.
  The program ensures that seat requests outside the range of 1-7 are rejected with appropriate messages.

OutPut Example :
Seat Availability:
Row 1: [O] [O] [O] [O] [O] [O] [O]
Row 2: [O] [O] [O] [O] [O] [O] [O]
Row 3: [O] [O] [O] [O] [O] [O] [O]
Row 4: [O] [O] [O] [O] [O] [O] [O]
Row 5: [O] [O] [O] [O] [O] [O] [O]
Row 6: [O] [O] [O] [O] [O] [O] [O]
Row 7: [O] [O] [O] [O] [O] [O] [O]
Row 8: [O] [O] [O] [O] [O] [O] [O]
Row 9: [O] [O] [O] [O] [O] [O] [O]
Row 10: [O] [O] [O]
Row 11: [O] [O] [O]

Enter the number of seats to book (1-7): 3
Successfully booked seats: Row 1, Seat 1, Row 1, Seat 2, Row 1, Seat 3

Seat Availability:
Row 1: [X] [X] [X] [O] [O] [O] [O]




To Run need python Installed,
python main.py
