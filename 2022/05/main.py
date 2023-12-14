#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name

# TODO: Better variable names please

from copy import deepcopy

INPUT_FILE = "input"


# extract number of crates to move, stack number to take crates from, stack
# number to put crates in from each string that describes one move
def parse_move(s):
    """
    Parse `s` string and get following integer values;
    - number of crates to move
    - stack to move crates from
    - stack to move crates to
    """
    num_crates, from_stack, to_stack = [
        int(x) for x in s.split() if x.isdigit()
    ]
    return num_crates, from_stack, to_stack


# move given number of crates from stack A to stack B
def move_crates(stacks, num_crates, from_stack, to_stack):
    """
    Move `num_crates` number of crates from `from_stack` to `to_stack`
    stacks: dictionary of stack data, where keys are stack numbers and values
    are lists of crates from bottom crate to top crate
    """
    for _ in range(num_crates):
        stacks[to_stack].append(stacks[from_stack].pop())


def move_crates_CrateMover_9001(stacks, num_crates, from_stack, to_stack):
    """
    Move crates with new CrateMover 9001, any number of crates at a time from
    each stack (instead of last crate on stack)
    """
    removed_crates = []
    for _ in range(num_crates):
        removed_crates.append(stacks[from_stack].pop())
    removed_crates.reverse()
    stacks[to_stack].extend(removed_crates)


def get_top_crate_letters(stacks):
    """Letters of top crates in each stack from first to last"""
    top_crates = ""
    for stack_num in sorted(stacks.keys()):
        top_crates += stacks[stack_num][-1]
    return top_crates


moves = []  # sequence of crate moves from stack to stack, from first to last
stack_data = []  # list of crates in same horizontal level in stacks

# read input file and build-up data structures about,
# - how stacks are organized and
# - how to gradually move crates from one stack to another
with open(INPUT_FILE, "r") as f:
    for line in f:
        row = line.rstrip()
        if not row:
            break
        stack_data.append(row)

    for line in f:
        moves.append(parse_move(line))

results = []
for line in stack_data[::-1]:
    results.append([line[i: i + 4] for i in range(0, len(line), 4)])

stack_numbers, *crates = results
stack_numbers = list(map(str.strip, stack_numbers))

STACKS = {}
for i, stack_num in enumerate(stack_numbers):
    for crate in crates:
        STACKS.setdefault(int(stack_num), []).append(crate[i].strip("[] "))

for k, v in STACKS.items():
    STACKS[k] = list(filter(None, v))


def part_1(stacks, moves):
    """
    Move stacks with traditional CrateMover 9000, one crate at a time from top
    of one stack to top of another.
    """
    stacks_cp = deepcopy(stacks)
    for move in moves:
        move_crates(stacks_cp, *move)
    return stacks_cp


def part_2(stacks, moves):
    """
    Move stacks with modern CrateMover 9001, any number of crates from top of
    one stack to top of another stack in original order.
    """
    stacks_cp = deepcopy(stacks)
    for move in moves:
        move_crates_CrateMover_9001(stacks_cp, *move)
    return stacks_cp


print(f"Part 1 solution: {get_top_crate_letters(part_1(STACKS, moves))}")
print(f"Part 2 solution: {get_top_crate_letters(part_2(STACKS, moves))}")
