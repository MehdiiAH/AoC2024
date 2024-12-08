def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    rules = []
    updates = []
    is_update_section = False

    for line in lines:
        line = line.strip()
        if not line:
            is_update_section = True
            continue

        if is_update_section:
            updates.append(list(map(int, line.split(","))))
        else:
            x, y = map(int, line.split("|"))
            rules.append((x, y))

    return rules, updates


def is_correct_order(update, rules):
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True


def find_middle_page(update):
    return update[len(update) // 2]


def main_part1(file_path):
    rules, updates = read_input(file_path)
    total_middle_sum = 0

    for update in updates:
        if is_correct_order(update, rules):
            total_middle_sum += find_middle_page(update)

    return total_middle_sum


def sort_update(update, rules):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)

    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []

    while queue:
        page = queue.popleft()
        sorted_update.append(page)
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def main_part2(file_path):
    rules, updates = read_input(file_path)
    total_middle_sum = 0

    for update in updates:
        if not is_correct_order(update, rules):
            sorted_update = sort_update(update, rules)
            total_middle_sum += find_middle_page(sorted_update)

    return total_middle_sum


file_path = "input.txt"
print(main_part1(file_path))
print(main_part2(file_path))
