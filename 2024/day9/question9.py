def part1(disk, file_blocks):
    file_positions = (
        idx
        for start, length in reversed(file_blocks)
        for idx in range(start + length - 1, start - 1, -1)
    )
    idx_file = next(file_positions)
    idx_disk = 0

    checksum = 0
    while idx_disk <= idx_file:
        if disk[idx_disk] == ".":
            checksum += idx_disk * disk[idx_file]
            idx_file = next(file_positions)
        else:
            checksum += idx_disk * disk[idx_disk]
        idx_disk += 1

    return checksum


def part2(disk, file_blocks, free_blocks):
    for file_start, file_len in reversed(file_blocks):
        for free_start, free_len in free_blocks:
            if free_start > file_start:
                break
            if free_len >= file_len:
                disk[free_start : free_start + file_len] = disk[file_start : file_start + file_len]
                disk[file_start : file_start + file_len] = ["."] * file_len
                idx = free_blocks.index((free_start, free_len))
                if file_len < free_len:
                    free_blocks[idx] = (free_start + file_len, free_len - file_len)
                else:
                    free_blocks.pop(idx)
                break

    return sum(idx * entry for idx, entry in enumerate(disk) if entry != ".")


def main():
    file_id = 0
    file_blocks, free_blocks, disk = [], [], []

    with open("input.txt", "rt") as f:
        for idx, block_len in enumerate(map(int, f.read().strip())):
            if idx % 2 == 0:
                file_blocks.append((len(disk), block_len))
                disk += [file_id] * block_len
                file_id += 1
            else:
                free_blocks.append((len(disk), block_len))
                disk += ["."] * block_len

    print(f"Part 1: {part1(disk, file_blocks)}")
    print(f"Part 2: {part2(disk, file_blocks, free_blocks)}")


if __name__ == "__main__":
    main()
