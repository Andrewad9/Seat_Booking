# Constants for the seat layout
ROWS = 11
SEATS_PER_ROW = 7

# Initial seat map, where 'True' means available and 'False' means booked
# Row 10 will have only 3 seats (index 10) and the rest will have 7 seats each
seats = [[True]*7 for _ in range(10)] + [[True]*3]

def display_seats():
    """
    Function to display the current seat availability.
    This will print the seat layout and show which seats are available (True) or booked (False).
    """
    print("\nSeat Availability:")
    for i, row in enumerate(seats):
        row_str = " ".join([f"[{'X' if seat == False else 'O'}]" for seat in row])
        print(f"Row {i + 1}: {row_str}")

def book_seats(num_seats):
    """
    Function to book a specified number of seats.
    The booking will prioritize filling a single row first, then spill over to nearby seats if needed.
    """
    booked_seats = []
    
    # Try to book the seats
    for i in range(ROWS):
        row = seats[i]
        available_seats = [index for index, seat in enumerate(row) if seat]  # List of available seat indices
        
        if len(available_seats) >= num_seats:
            # If there are enough seats in the row
            for j in range(num_seats):
                seat_index = available_seats[j]
                row[seat_index] = False  # Book the seat
                booked_seats.append(f"Row {i + 1}, Seat {seat_index + 1}")
            break
        else:
            # If there are not enough seats in the row, try to book the seats from nearby rows
            if available_seats:
                # Book seats in this row first
                for index in available_seats:
                    row[index] = False
                    booked_seats.append(f"Row {i + 1}, Seat {index + 1}")
                    num_seats -= 1
                    if num_seats == 0:
                        break
            if num_seats == 0:
                break
    
    # If there are still seats to be booked after trying all rows, return failure
    if num_seats > 0:
        print(f"Could not book {num_seats} seats. Not enough available seats.")
    else:
        print(f"Successfully booked seats: {', '.join(booked_seats)}")

    # Display the updated seat availability
    display_seats()

# Driver code
def main():
    display_seats()
    while True:
        try:
            num_seats = int(input("Enter the number of seats to book (1-7): "))
            if num_seats < 1 or num_seats > 7:
                print("Please enter a number between 1 and 7.")
                continue
            book_seats(num_seats)
            more_booking = input("Do you want to book more seats? (y/n): ")
            if more_booking.lower() != 'y':
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
