from math import isclose


def read_input(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]


def find_antennas(grid):
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas


def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)) < 1e-10


def check_point_for_antinode(point, ant1, ant2):
    if not is_collinear(ant1, point, ant2):
        return False

    d1 = distance(ant1, point)
    d2 = distance(ant2, point)

    return (d1 > 0 and d2 > 0 and
            (isclose(d1 / d2, 2.0, rel_tol=1e-9) or isclose(d2 / d1, 2.0, rel_tol=1e-9)))


def calculate_antinodes(grid, antennas):
    height = len(grid)
    width = len(grid[0])
    antinodes = set()

    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                ant1 = positions[i]
                ant2 = positions[j]

                for y in range(height):
                    for x in range(width):
                        point = (x, y)
                        if check_point_for_antinode(point, ant1, ant2):
                            antinodes.add(point)

    return antinodes


def calculate_antinodes_part2(grid, antennas):
    height = len(grid)
    width = len(grid[0])
    antinodes = set()

    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue

        antinodes.update(positions)

        for y in range(height):
            for x in range(width):
                point = (x, y)

                for i in range(len(positions)):
                    for j in range(i + 1, len(positions)):
                        ant1 = positions[i]
                        ant2 = positions[j]

                        if is_collinear(ant1, point, ant2):
                            antinodes.add(point)

    return antinodes


def solve_antenna_problem(filename, part=1):
    grid = read_input(filename)
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(grid, antennas) if part == 1 else calculate_antinodes_part2(grid, antennas)
    return len(antinodes)


if __name__ == "__main__":
    filename = "input.txt"
    result1 = solve_antenna_problem(filename, part=1)
    result2 = solve_antenna_problem(filename, part=2)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")