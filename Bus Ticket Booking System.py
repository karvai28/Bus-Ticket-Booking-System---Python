total_tickets = 100
available_tickets = total_tickets

def display_menu():
    print("\n1. Book Tickets")
    print("2. Cancel Tickets")
    print("3. View Available Tickets")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def book_tickets():
    global available_tickets
    num_tickets = int(input("Enter the number of tickets to book: "))
    if num_tickets > available_tickets:
        print("Not enough tickets available.")
    elif num_tickets > 0:
        available_tickets -= num_tickets
        print(f"Successfully booked {num_tickets} tickets.")
    else:
        print("Invalid number of tickets.")

def cancel_tickets():
    global available_tickets
    num_tickets = int(input("Enter the number of tickets to cancel: "))
    booked_tickets = total_tickets - available_tickets
    if num_tickets > booked_tickets:
        print("You cannot cancel more tickets than you have booked.")
    elif num_tickets > 0:
        available_tickets += num_tickets
        print(f"Successfully cancelled {num_tickets} tickets.")
    else:
        print("Invalid number of tickets.")

def view_available_tickets():
    print(f"Available tickets: {available_tickets}")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            book_tickets()
        elif choice == '2':
            cancel_tickets()
        elif choice == '3':
            view_available_tickets()
        elif choice == '4':
            print("Thank you for booking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
