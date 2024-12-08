from itertools import product


def evaluate_expression(nums, ops):
    result = nums[0]
    for i, op in enumerate(ops):
        if op == "+":
            result += nums[i + 1]
        elif op == "*":
            result *= nums[i + 1]
        elif op == "||":
            result = int(str(result) + str(nums[i + 1]))
    return result


def solve_equations(equations, operators):
    total = 0

    for equation in equations:
        target, *nums = equation
        num_count = len(nums)
        operator_combinations = product(operators, repeat=num_count - 1)

        for ops in operator_combinations:
            if evaluate_expression(nums, ops) == target:
                total += target
                break

    return total


def read_input(file_path):
    equations = []
    with open(file_path, "r") as file:
        for line in file:
            target, nums = line.strip().split(":")
            target = int(target)
            nums = list(map(int, nums.split()))
            equations.append((target, *nums))
    return equations


def part1(equations):
    return solve_equations(equations, ["+", "*"])


def part2(equations):
    return solve_equations(equations, ["+", "*", "||"])


input_file = "input.txt"
data = read_input(input_file)

result_part1 = part1(data)
result_part2 = part2(data)

print("Partie 1 - Résultat total de calibration :", result_part1)
print("Partie 2 - Résultat total de calibration :", result_part2)
