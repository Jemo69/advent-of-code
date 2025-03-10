# pylint: disable=C0114,C0116,C0301,C0209,W1514

from time import perf_counter as perf_counter
from typing import Any


def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


@profiler
def part1() -> set[tuple[int, int]]:
    """First part of the puzzle."""
    obstacles: set[tuple[int, int]] = set()
    dirs = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    rot = "^>v<"

    for y, line in enumerate(open("input.txt")):
        for x, c in enumerate(line.strip()):
            if c == "#":
                obstacles.add((x, y))
            elif c in dirs:
                guard = (c, (x, y))

    seen: set[tuple[str, tuple[int, int]]] = set()
    while guard not in seen:
        seen.add(guard)

        np = (guard[1][0] + dirs[guard[0]][0], guard[1][1] + dirs[guard[0]][1])
        d = guard[0]
        if np in obstacles:
            d = rot[(rot.index(d) + 1) % len(rot)]
            np = (guard[1][0] + dirs[d][0], guard[1][1] + dirs[d][1])

        if not (0 <= np[0] < len(line.strip()) and 0 <= np[1] < y):
            break
        guard = (d, np)

    path: set[tuple[int, int]] = set(guard[1] for guard in seen)
    print(len(path))

    return path


def is_guard_in_loop(
    guard: tuple[str, tuple[int, int]], obstacles: set[tuple[int, int]], max_x: int, max_y: int
) -> bool:
    """Check if a guard goes in a loop."""
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    rotation = "^>v<"

    seen: set[tuple[str, tuple[int, int]]] = set()
    while guard not in seen:
        seen.add(guard)
        new_position = (
            guard[1][0] + directions[guard[0]][0],
            guard[1][1] + directions[guard[0]][1],
        )
        current_direction = guard[0]

        # keep rotating until the new position is free space
        while new_position in obstacles:
            current_direction = rotation[(rotation.index(current_direction) + 1) % len(rotation)]
            dx, dy = directions[current_direction]
            new_position = (guard[1][0] + dx, guard[1][1] + dy)

        if not (0 <= new_position[0] < max_x and 0 <= new_position[1] < max_y):
            return False

        guard = (current_direction, new_position)

    return True


@profiler
def part2(path: set[tuple[int, int]]) -> None:
    """Second part of the puzzle."""
    max_x, max_y = 0, 0
    guard_direction, guard_position = "", (0, 0)
    obstacles: set[tuple[int, int]] = set()

    with open("input.txt","r") as f:
        for y, line in enumerate(f):
            max_y = y
            line = line.strip()
            max_x = len(line)
            for x, char in enumerate(line):
                if char == "#":
                    obstacles.add((x, y))
                elif char == "^":
                    guard_direction, guard_position = char, (x, y)

    result = sum(
        is_guard_in_loop((guard_direction, guard_position), obstacles | {t}, max_x, max_y) for t in path
    )
    print(result)


if __name__ == "__main__":
    path = part1()
    part2(path)