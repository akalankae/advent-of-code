#!/usr/bin/env python3
# -*- coding: utf-8 -*-


INPUT_FILE = "input"


# Get the absolute path of given `target_dir` that resides in `current_dir`
def get_dir_path(current_dir: str, target_dir: str) -> str:
    """
    Change current working directory from `current_dir` to `target_dir` and
    return full path
    REDUNDANT NOTE: function breaks if `current_dir` ends in '/'
    """
    if current_dir == "":
        return target_dir
    if current_dir == "/":
        return f"/{target_dir}"
    if target_dir == "..":
        return current_dir.rpartition("/")[0] or "/"
    current_dir = current_dir.rstrip("/")
    return f"{current_dir}/{target_dir}"


# Get dict containing the contents of given directory
# parameters:
# 1. root: root dict that has all contents of the file systemt mounted at '/'
# 2. dir: dict that has the contents of the given directory
def get_dir_content(root: dict, dir_path: str) -> dict:
    """
    Go through `root` dictionary that contains all files & directories, and
    return the relavent dictionary containing files & directories of `dir`
    If does not have a dictionary for `dir` then return an empty dict
    parameters:
    1. root - dictionary containing all files/directories under "/"
    2. current directory: "/" separated path string

    CAVEATS: if `dir` is an empty string (like in the start of program)
    returns the root dictionary
    """
    if dir_path == "/":
        return root
    dir_content = root
    for dir in filter(None, dir_path.split("/")):
        dir_content = dir_content.setdefault(dir, {})
    return dir_content


# Get list of paths of all directories residing in given directory.
# parameters:
# 1. dir_name: absolute path of given directory
# 2. dir: dict that has the contents of the given directory
def get_containing_dir_names(dir_name: str, dir: dict):
    """
    Get a list of names of directories inside given `directory`
    """
    dir_names = []
    if dir_name == "/":
        dir_name = ""
    for name, content in dir.items():
        if isinstance(content, dict):
            dir_names.append(f"{dir_name}/{name}")
            dir_names.extend(
                get_containing_dir_names(f"{dir_name}/{name}", content)
            )
    return dir_names


cwd = ""  # Current Working Directory
root = None  # dict containing all files & directories in the system

with open(INPUT_FILE, "r") as f:
    for line in map(str.rstrip, f):
        # commands
        if line.startswith("$"):
            cmdLine = line[2:]  # get rid of "$ "
            # command has to be "cd"
            if cmdLine != "ls":
                _, target = cmdLine.split()
                if target == "/":
                    root = {}
                cwd = get_dir_path(cwd, target)

        # command outputs
        else:
            size, name = line.split()
            if size.isnumeric():
                get_dir_content(root, cwd)[name] = int(size)
            else:
                get_dir_content(root, cwd)[name] = {}


def get_dir_size(directory: dict) -> int:
    """
    Get size of the directory by computing sum of all of its contents.
    """
    total = 0
    for name, content in directory.items():
        if isinstance(content, dict):
            total += get_dir_size(content)
        else:
            total += content
    return total


print(f"Size of root directory is {get_dir_size(root)}")


dirs = get_containing_dir_names("/", root)  # list of directories on the system

MAX_TOTAL_SIZE = 100000
results = {}

for dir in dirs:
    results[dir] = get_dir_size(get_dir_content(root, dir))


total_size = 0

for path, size in results.items():
    if size <= MAX_TOTAL_SIZE:
        # print(f"{size:>6d} {path}")
        total_size += size

print(
    f"Total size of directories less than or equal to {MAX_TOTAL_SIZE} is {total_size}"
)
