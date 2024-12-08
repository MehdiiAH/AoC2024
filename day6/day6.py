def load_map(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f.readlines()]


def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in "^>v<":
                return x, y, grid[y][x]
    return None


def get_initial_direction(symbol):
    directions = {
        "^": (0, -1),  # up
        ">": (1, 0),  # right
        "v": (0, 1),  # down
        "<": (-1, 0),  # left
    }
    return directions[symbol]


def turn_right(dx, dy):
    return -dy, dx


def is_valid_position(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def count_visited_positions(grid):
    start = find_start(grid)
    if not start:
        return 0

    x, y, direction_symbol = start
    dx, dy = get_initial_direction(direction_symbol)

    visited = set()
    visited.add((x, y))

    while True:
        next_x, next_y = x + dx, y + dy

        if not is_valid_position(next_x, next_y, grid) or (
            is_valid_position(next_x, next_y, grid) and grid[next_y][next_x] == "#"
        ):
            dx, dy = turn_right(dx, dy)
        else:
            x, y = next_x, next_y
            visited.add((x, y))

            if not is_valid_position(x + dx, y + dy, grid):
                break

    return len(visited)


def count_obstruction_positions(grid):
    def simulate_with_obstruction(grid, obs_x, obs_y):
        start = find_start(grid)
        if not start:
            return False

        x, y, direction_symbol = start
        dx, dy = get_initial_direction(direction_symbol)
        state_history = set()

        while True:
            state = (x, y, dx, dy)
            if state in state_history:
                return True
            state_history.add(state)

            next_x, next_y = x + dx, y + dy

            if (
                (next_x, next_y) == (obs_x, obs_y)
                or (
                    is_valid_position(next_x, next_y, grid)
                    and grid[next_y][next_x] == "#"
                )
                or not is_valid_position(next_x, next_y, grid)
            ):
                dx, dy = turn_right(dx, dy)
            else:
                x, y = next_x, next_y

            if not is_valid_position(x + dx, y + dy, grid):
                return False

    valid_positions = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == ".":
                if simulate_with_obstruction(grid, x, y):
                    valid_positions += 1

    return valid_positions


def main():
    grid = load_map("input.txt")
    result = count_visited_positions(grid)
    print(
        f"The guard will visit {result} distinct positions before leaving the mapped area."
    )
    result2 = count_obstruction_positions(grid)
    print(
        f"There are {result2} positions where you can place an obstruction to get the guard stuck in a loop."
    )


if __name__ == "__main__":
    main()
