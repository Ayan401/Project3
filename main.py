x = 0
y = 0

GRID_MIN = -5
GRID_MAX = 5

def move(command):
    global x, y  #Fixed scope

    if command == "forward":
        if y + 1 <= GRID_MAX:
            y += 1
        else:
            print("Boundary reached!")
    elif command == "backward":
        if y - 1 >= GRID_MIN:
            y -= 1
        else:
            print("Boundary reached!")
    elif command == "right":
        if x + 1 <= GRID_MAX:
            x += 1
        else:
            print("Boundary reached!")
    elif command == "left":
        if x - 1 >= GRID_MIN:
            x -= 1
        else:
            print("Boundary reached!")
    else:
        print("Invalid command! Use: forward, backward, left, right")

def print_position():
    print(f"Position: ({x}, {y})")  # ✅ clearer format

while True:
    cmd = input("Enter command (forward/backward/left/right/exit): ").lower().strip()
    
    if cmd == "exit":
        break
    a
    move(cmd)
    print_position()
