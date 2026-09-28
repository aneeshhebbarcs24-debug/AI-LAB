room_A = "Dirty"
room_B = "Dirty"
vacuum_location = "A"

print("Initially: Room A is", room_A, "and Room B is", room_B)

if room_A == "Dirty":
    room_A = "Clean"
    print(" Step 1: Sucked dirt in Room A")

vacuum_location = "B"
print(" Step 2 : Moved to Room B")

if room_B == "Dirty":
    room_B = "Clean"
    print(" Step 3: Sucked dirt in Room B")


print("Finish : Room A is", room_A, "and Room B is", room_B)
