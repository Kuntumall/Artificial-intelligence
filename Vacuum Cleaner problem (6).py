def vacuum_cleaner():
    num_rooms = int(input("Enter the number of rooms: "))
    room_states = []

    for i in range(num_rooms):
        state = input(f"Enter state of Room {i + 1} (clean/dirty): ").strip().lower()
        room_states.append(state)

    current_position = int(input("Enter the starting position of the vacuum cleaner (1 to number of rooms): ")) - 1

    print("\nStarting the cleaning process...\n")
    for i in range(len(room_states)):
        room = (current_position + i) % num_rooms
        if room_states[room] == "dirty":
            print(f"Room {room + 1} is dirty. Cleaning...")
            room_states[room] = "clean"
            print(f"Room {room + 1} is now clean.")
        else:
            print(f"Room {room + 1} is already clean.")

    print("\nCleaning complete.")
    print("Final states of the rooms:")
    for i, state in enumerate(room_states):
        print(f"Room {i + 1}: {state}")

if __name__ == "__main__":
    vacuum_cleaner()
