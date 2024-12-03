import re


def extract_and_multiply_part1(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    total_sum = 0

    instructions = re.findall(r"mul\((\d+),(\d+)\)", content)

    for instruction in instructions:
        x, y = map(int, instruction)
        total_sum += x * y

    return total_sum


def extract_and_multiply_part2(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    total_sum = 0
    mul_enabled = True

    instructions = re.findall(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)", content)

    for instruction in instructions:
        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                num1, num2 = map(int, re.findall(r"\d+", instruction))
                total_sum += num1 * num2

    return total_sum


file_path = "input.txt"
result1 = extract_and_multiply_part1(file_path)
print(result1)

result2 = extract_and_multiply_part2(file_path)
print(result2)
