def is_safe_report(levels):
    increasing = all(
        levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3
        for i in range(len(levels) - 1)
    )
    decreasing = all(
        levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3
        for i in range(len(levels) - 1)
    )
    return increasing or decreasing


def can_be_safe_by_removing_one(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1 :]
        if is_safe_report(new_levels):
            return True
    return False


def count_safe_reports_part1(file_path):
    safe_count = 0
    with open(file_path, "r") as file:
        for line in file:
            levels = list(map(int, line.split()))
            if is_safe_report(levels):
                safe_count += 1
    return safe_count


def count_safe_reports_part2(file_path):
    safe_count = 0
    with open(file_path, "r") as file:
        for line in file:
            levels = list(map(int, line.split()))
            if can_be_safe_by_removing_one(levels):
                safe_count += 1
    return safe_count


file_path = "input.txt"
print(count_safe_reports_part1(file_path))
print(count_safe_reports_part2(file_path))
