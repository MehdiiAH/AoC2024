from collections import Counter


def read_and_split_numbers(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list


def calculate_total_distance(file_path):
    left_list, right_list = read_and_split_numbers(file_path)
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    print(f"Total distance: {total_distance}")


def calculate_similarity_score(file_path):
    left_list, right_list = read_and_split_numbers(file_path)
    right_count = Counter(right_list)
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_count[number]
    print(f"Total similarity score: {similarity_score}")


calculate_total_distance("input.txt")
calculate_similarity_score("input.txt")
