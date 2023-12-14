#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name

import string

INPUT_FILE = "input"


def get_priority(c: str) -> int:
    """
    Get priority of given alphabetical character `c`
    """
    assert len(c) == 1  # dbg
    return string.ascii_letters.index(c) + 1


def get_common_item_type(items: str) -> str:
    """
    Get item type (a letter) that appears in both front half and rear half of
    the items.
    """
    front_half, rear_half = items[: len(items) // 2], items[len(items) // 2:]
    assert len(front_half) == len(rear_half)  # dbg
    return "".join(set(front_half) & set(rear_half))


def part_1(input_file):
    """
    Solution to part 1.
    """
    try:
        with open(INPUT_FILE, "r") as f:
            sum_of_priorities = 0
            for line in f:
                common_type = get_common_item_type(line.rstrip())
                sum_of_priorities += get_priority(common_type)
    except FileNotFoundError:
        print(f'File "{INPUT_FILE}" not found')
        exit(1)
    else:
        print(f"Sum of misplaced item priorities is {sum_of_priorities}")


def get_group_badge(group):
    """
    Get the letter common to all 3 strings in list `group`
    """
    badge = "".join(set(group[0]) & set(group[1]) & set(group[2]))
    assert len(badge) == 1 and badge in string.ascii_letters
    return badge


def part_2(input_file):
    """
    Solution to part 2.

    Elves are divided into groups of 3.
    In input file, elves corresponding to each 3 lines belong to same group.
    i.e. lines 1-3, 4-6, 7-9, ... are groups of 3 elves.
    Each group has a badge, which is a letter.  This letter is the letter
    common to all 3 elves of the same group.
    Find item type (AKA badge) that corresponds to each 3-elf group, compute
    the relevant priority for that letter, and sum all priorities.
    """
    try:
        with open(input_file, "r") as f:
            sum_of_priorities = 0
            group = []
            for line in f:
                group.append(line.rstrip())

                # once 3-elves are added to group, get the their badge and
                # clear the group to make room next set of 3-elves
                if len(group) == 3:
                    group_badge = get_group_badge(group)
                    sum_of_priorities += get_priority(group_badge)
                    group.clear()

        # make sure when reading file is over that group list is empty
        assert len(group) == 0

    except FileNotFoundError:
        print(f'File "{input_file}" not found')
        exit(1)
    else:
        print(f"Sum of group priorities is {sum_of_priorities}")


# Your testing code goes here
if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
