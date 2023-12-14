#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name

INPUT_FILE = "input"
COUNTER = 0


def fully_contains(broad: tuple[int, int], narrow: tuple[int, int]) -> bool:
    """
    Does `broad` pair fully contain all elements in `narrow` pair?
    e.g.
      (5, 10), (6, 9) => True
      (5, 10), (20, 30) => False
      (5, 10), (0, 100) => False
      (5, 10), (10, 10) => True
    """
    return broad[0] <= narrow[0] and broad[1] >= narrow[1]


def Comment(group_1: tuple[int, int], group_2: tuple[int, int]) -> None:
    if fully_contains(group_1, group_2):
        print(
            f"{group_1[0]}-{group_1[1]} fully contains {group_2[0]}-{group_2[1]}"
        )


def is_overlapping(pair_1: tuple[int, int], pair_2: tuple[int, int]):
    """
    Does `pair_1` overlap `pair_2`?
    """
    return (
        pair_2[0] <= pair_1[0] <= pair_2[1]
        or pair_2[0] <= pair_1[1] <= pair_2[1]
        or pair_1[0] <= pair_2[0] <= pair_1[1]
        or pair_1[0] <= pair_2[1] <= pair_1[1]
    )


def Part1(input_file):
    """
    Solution to part 1.
    """
    counter = 0
    try:
        with open(input_file, "r") as f:
            for line in f:
                group_1, group_2 = [
                    tuple(int(x) for x in group)
                    for group in [
                        s.split("-") for s in line.rstrip().split(",")
                    ]
                ]
                # if group_1 and group_2 are identical count ONCE only!
                if fully_contains(group_1, group_2) or fully_contains(
                    group_2, group_1
                ):
                    counter += 1
    except FileNotFoundError:
        print(f"Input file {input_file} not found!")
        exit(1)
    else:
        print(f"Found {counter} groups")


def Part2(input_file):
    """
    Solution to part 2.
    """
    overlapping_groups = []
    try:
        with open(input_file, "r") as f:
            for line in f:
                group_1, group_2 = [
                    tuple(int(x) for x in group)
                    for group in [
                        s.split("-") for s in line.rstrip().split(",")
                    ]
                ]
                # if group_1 and group_2 are identical count ONCE only!
                if is_overlapping(group_1, group_2):
                    overlapping_groups.append((group_1, group_2))
    except FileNotFoundError:
        print(f"Input file {input_file} not found!")
        exit(1)
    else:
        print(f"Number of overlapping groups: {len(overlapping_groups)}")


def main(input_file):
    Part1(input_file)
    Part2(input_file)


groups = [
    ((2, 4), (6, 8)),
    ((2, 3), (4, 5)),
    ((5, 7), (7, 9)),
    ((2, 8), (3, 7)),
    ((6, 6), (4, 6)),
    ((2, 6), (4, 8)),
]


if __name__ == "__main__":
    # shout = False  # True: echo each containing pair of groups
    # for group in groups:
    #     Comment(group[0], group[1], not shout)
    #     Comment(group[1], group[0], not shout)
    # print(f"Found {COUNTER} groups")
    main(INPUT_FILE)
