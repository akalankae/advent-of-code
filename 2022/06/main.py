#!/usr/bin/env _python3
# -*- coding: utf-8 -*-
# Last Modified: <date time>
# pylint: disable=invalid-name

input_file = "input"


def get_start_of_packet(buffer):
    assert len(buffer) >= 4
    for i in range(3, len(buffer)):
        if len(set(buffer[i - 4: i])) == 4:
            return i
    return -1


def get_start_of_msg(buffer):
    assert len(buffer) >= 14
    for i in range(13, len(buffer)):
        if len(set(buffer[i - 14: i])) == 14:
            return i
    return -1


# Your testing code goes here
def test_get_start_of_packet():
    assert get_start_of_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert get_start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert get_start_of_packet("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert get_start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert get_start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_get_start_of_msg():
    assert get_start_of_msg("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert get_start_of_msg("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert get_start_of_msg("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert get_start_of_msg("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert get_start_of_msg("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


def part_1(input_file):
    try:
        with open(input_file, "r") as f:
            buffer = f.read().rstrip()
    except FileNotFoundError:
        print(f'Input file not found: "{input_file}"')
    else:
        print(get_start_of_packet(buffer))


def part_2(input_file):
    try:
        with open(input_file, "r") as f:
            buffer = f.read().rstrip()
    except FileNotFoundError:
        print(f'Input file not found: "{input_file}"')
    else:
        print(get_start_of_msg(buffer))


if __name__ == "__main__":
    part_1(input_file)
    part_2(input_file)
