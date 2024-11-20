class Movie:
    def __init__(self, title, show_time, total_seats):
        self.title = title
        self.show_time = show_time
        self.total_seats = total_seats
        self.seats_available = total_seats
        self.seat_numbers = list(range(1, total_seats + 1))  # List of seat numbers

    def view_available_seats(self):
        return self.seat_numbers


class Booking:
    def __init__(self, movie):
        self.movie = movie

    def book_ticket(self, seat_numbers):
        if all(seat in self.movie.seat_numbers for seat in seat_numbers):
            for seat in seat_numbers:
                self.movie.seat_numbers.remove(seat)
            self.movie.seats_available -= len(seat_numbers)
            print(f"Successfully booked seat(s) {seat_numbers} for {self.movie.title} at {self.movie.show_time}.")
            self.print_ticket(seat_numbers)
        else:
            print("One or more selected seats are not available. Please choose different seats.")

    def cancel_ticket(self, seat_numbers):
        for seat in seat_numbers:
            if seat not in self.movie.seat_numbers:  # Only add back seats that were booked
                self.movie.seat_numbers.append(seat)
        self.movie.seat_numbers.sort()  # Keep seat numbers in order
        self.movie.seats_available += len(seat_numbers)
        if self.movie.seats_available > self.movie.total_seats:
            self.movie.seats_available = self.movie.total_seats
        print(f"Canceled seat(s) {seat_numbers}. Seats are now available for {self.movie.title}.")

    def view_available_seats(self):
        print(f"Seats available for {self.movie.title}: {self.movie.view_available_seats()}")

    def print_ticket(self, seat_numbers):
        print("\n--- Ticket ---")
        print(f"Movie: {self.movie.title}")
        print(f"Show Time: {self.movie.show_time}")
        print(f"Seat Numbers: {seat_numbers}")
        print("----------------\n")


# Example Usage
movie = Movie("The Grand Adventure", "7:00 PM", 10)  # Reduced number of seats for testing
booking_system = Booking(movie)

# Viewing available seats
booking_system.view_available_seats()

# Booking tickets
booking_system.book_ticket([1, 2, 3])
booking_system.view_available_seats()

# Trying to book already booked seats
booking_system.book_ticket([1, 4])  # Should give an error for seat 1

# Canceling tickets
booking_system.cancel_ticket([2])
booking_system.view_available_seats()
