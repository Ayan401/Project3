# Robot Movement Simulator (Broken Version)

x = 0
y = 0

def move(command):
    if command == "forward":
        y = y + 1   # ❌ local variable issue
    elif command == "backward":
        y = y - 1
    elif command == "right":
        x = x + 1
    elif command == "left":
        x = x - 1
    else:
        print("Invalid command")


def print_position():
    print("Position:", x, y)


while True:
    cmd = input("Enter command (forward/backward/left/right/exit): ")
    
    if cmd == "exit":
        break
    
    move(cmd)
    print_position()