r, c = map(int, input().split())
start_x, start_y = map(int, input().split())
desired_x, desired_y = map(int, input().split())

start_x -= 1
start_y -= 1
desired_x -= 1
desired_y -= 1

turned = 0 # up = 0, left = 1, down = 2, right = 3
maze = []

visited = set()

for i in range(r):
    maze.append(list(input().strip()))

def can_turn_left_and_face_empty(current_x, current_y):
    vectors = [(0, -1), (-1, 0), (0, 1), (-1, 0)]
    new_x, new_y = -1, -1
    add_vec = vectors[turned]
    new_x, new_y = current_x + add_vec[0], current_y + add_vec[1]

    if new_x >= 0 and new_y >= 0 and new_x < r and new_y < c and maze[new_x][new_y] == "0":
        return (True, new_x, new_y)
    return (False, None, None)

def can_move_forward(current_x, current_y):
    vectors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    new_x, new_y = -1, -1
    add_vec = vectors[turned]
    new_x, new_y = current_x + add_vec[0], current_y + add_vec[1]

    if new_x >= 0 and new_y >= 0 and new_x < r and new_y < c and maze[new_x][new_y] == "0":
        return (True, new_x, new_y)

    return (False, None, None)


def turn_right():
    global turned
    turned = (turned + 1) % 4

possible = True
while True:
    print(start_x, start_y, turned)
    if (start_x, start_y, turned) in visited :
        possible = False
        break

    visited.add((start_x, start_y, turned))
    if (start_x, start_y) == (desired_x, desired_y):
        break

    can_turn_left, new_x, new_y = can_turn_left_and_face_empty(start_x, start_y)
    if can_turn_left:
        turned = (turned - 1) % 4
        start_x, start_y = new_x, new_y
        continue

    can_move_fd, new_x, new_y = can_move_forward(start_x, start_y)
    if can_move_fd:
        start_x, start_y = new_x, new_y
        continue

    turn_right()

print("1" if possible else "0")
