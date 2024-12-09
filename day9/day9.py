def parse_disk_map(disk_map):
    return [int(x) for x in disk_map.strip()]


def create_block_representation(lengths):
    blocks = []
    file_id = 0
    for i in range(0, len(lengths), 2):
        file_length = lengths[i]
        gap_length = lengths[i + 1] if i + 1 < len(lengths) else 0
        blocks.extend([file_id] * file_length)
        blocks.extend(["."] * gap_length)
        file_id += 1
    return blocks


def get_file_positions(blocks):
    file_positions = {}
    for i, block in enumerate(blocks):
        if block != ".":
            if block not in file_positions:
                file_positions[block] = []
            file_positions[block].append(i)
    return file_positions


def get_gaps(blocks):
    gaps = []
    start = -1
    for i, block in enumerate(blocks):
        if block == ".":
            if start == -1:
                start = i
        elif start != -1:
            gaps.append((start, i - start))
            start = -1
    if start != -1:
        gaps.append((start, len(blocks) - start))
    return gaps


def defragment_disk_part1(blocks):
    file_positions = get_file_positions(blocks)
    gaps = [i for i, block in enumerate(blocks) if block == "."]

    if not gaps:
        return blocks

    for file_id in sorted(file_positions.keys(), reverse=True):
        positions = file_positions[file_id]
        for pos in sorted(positions):
            available_gaps = [g for g in gaps if g < pos]
            if not available_gaps:
                continue
            gap_pos = min(available_gaps)
            blocks[gap_pos] = file_id
            blocks[pos] = "."
            gaps.remove(gap_pos)
            gaps.append(pos)
            gaps.sort()
    return blocks


def defragment_disk_part2(blocks):
    file_positions = get_file_positions(blocks)

    for file_id in sorted(file_positions.keys(), reverse=True):
        positions = sorted(file_positions[file_id])
        file_size = len(positions)
        gaps = get_gaps(blocks)

        suitable_gap = None
        for gap_start, gap_size in gaps:
            if gap_size >= file_size and gap_start < positions[0]:
                suitable_gap = gap_start
                break

        if suitable_gap is not None:
            for i, pos in enumerate(positions):
                blocks[suitable_gap + i] = file_id
                blocks[pos] = "."
    return blocks


def calculate_checksum(blocks):
    return sum(pos * val for pos, val in enumerate(blocks) if val != ".")


def main():
    with open("input.txt") as f:
        disk_map = f.read().strip()

    blocks = create_block_representation(parse_disk_map(disk_map))
    final_blocks = defragment_disk_part1(blocks)
    print(calculate_checksum(final_blocks))

    blocks = create_block_representation(parse_disk_map(disk_map))
    final_blocks = defragment_disk_part2(blocks)
    print(calculate_checksum(final_blocks))


if __name__ == "__main__":
    main()
