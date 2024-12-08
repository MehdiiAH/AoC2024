def count_xmas(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    count = 0

    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(start_x, start_y, dx, dy):
        word = ""
        x, y = start_x, start_y

        for _ in range(4):
            if not is_valid(x, y):
                return False
            word += grid[x][y]
            x += dx
            y += dy

        return word == target

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1

    return count


def count_x_mas(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_mas(x, y, dx, dy):
        if not all(is_valid(x + i * dx, y + i * dy) for i in range(3)):
            return False

        chars = "".join(grid[x + i * dx][y + i * dy] for i in range(3))
        return chars in ["MAS", "SAM"]

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (check_mas(i - 1, j - 1, 1, 1) and check_mas(i - 1, j + 1, 1, -1)) or (
                check_mas(i + 1, j - 1, -1, 1) and check_mas(i + 1, j + 1, -1, -1)
            ):
                count += 1

    return count


with open("input.txt") as f:
    grid = [line.strip() for line in f]

result1 = count_xmas(grid)
print(f"Part 1: Found {result1} occurrences of XMAS")

result2 = count_x_mas(grid)
print(f"Part 2: Found {result2} occurrences of X-MAS")
