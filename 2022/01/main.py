#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name

INPUT_FILE_NAME = "sample.in"


if __name__ == "__main__":
    try:
        with open(INPUT_FILE_NAME, "r") as inputFile:
            calories = []  # list of number of calories each of elves have
            numCalories = 0
            for line in inputFile:
                if line.rstrip() != "":
                    numCalories += int(line.rstrip())

                # blank line stores total number of calories carried by last
                # elf AND resets number of calories for the next elf
                else:
                    calories.append(numCalories)
                    numCalories = 0

    except FileNotFoundError:
        print(f'Input file "{INPUT_FILE_NAME}" missing')
        exit(1)

    else:
        # Number of calories carried by the elf who carries the most number of
        # calories
        print(max(*calories))

        # Total number of calories carried by the 3 elves who carry the most
        # number of calories
        calories.sort(reverse=True)
        print(sum(calories[:3]))
