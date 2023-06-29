#clock and timer
import time

def display_time():
    current_time = time.strftime("%H:%M:%S")
    print("Current Time:", current_time)

def countdown_timer(minutes):
    seconds = minutes * 60
    while seconds >= 0:
        minutes, seconds = divmod(seconds, 60)
        timer = f"{minutes:02d}:{seconds:02d}"
        print("Countdown Timer:", timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Countdown Timer: 00:00")

def clock():
    while True:
        display_time()
        time.sleep(1)

# Example usage:
print("1. Clock")
print("2. Countdown Timer")
choice = input("Select an option (1 or 2): ")

if choice == '1':
    clock()
elif choice == '2':
    minutes = int(input("Enter the countdown timer duration in minutes: "))
    countdown_timer(minutes)
else:
    print("Invalid choice. Exiting the program.")
