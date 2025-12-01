import argparse
from itertools import cycle


"""
--- Day 1: Secret Entrance ---

The Elves have good news and bad news.

The good news is that they've discovered project management! This has given them the tools they need to prevent
their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished
soon so that other critical tasks can start on time.

The bad news is that they've realized they have a different emergency: according to their resource planning, none
of them have any time left to decorate the North Pole!

To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when
you complete the first. Each puzzle grants one star. Good luck!
"""

def get_input_file(filenamen: str) -> list:
    """
    Reads all lines from a file and returns them as a list of strings.

    This function opens a file specified by the input filename in read mode,
    reads all lines from it, and returns those lines as a list of strings in
    the order they appear in the file.

    :param filenamen: The path to the file to read.
    :type filenamen: str
    :return: A list of strings, where each string is a line from the file.
    :rtype: list
    """
    with open(file=filenamen, mode="r") as file:
        result = file.readlines()

    return result


def solve_puzzle_1(input_data: list) -> int:
    """
    Part One
    ========
    You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password
    seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

    "Due to new security protocols, the password is locked in the safe below. Please see the attached document for the
    new combination."

    The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn
    the dial, it makes a small click noise as it reaches each number.

    The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to
    open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left
    (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which
    indicates how many clicks the dial should be rotated in that direction.

    So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation
    of L19 would cause it to point at 0.

    Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the
    dial right from 99 one click makes it point at 0.

    So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5
    could cause it to point at 0.

    The dial starts by pointing at 50.

    You could follow the instructions, but your recent required official North Pole secret entrance security training
    seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left
    pointing at 0 after any rotation in the sequence.

    For example, suppose the attached document contained the following rotations:

    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82

    Following these rotations would cause the dial to move as follows:

        The dial starts by pointing at 50.
        The dial is rotated L68 to point at 82.
        The dial is rotated L30 to point at 52.
        The dial is rotated R48 to point at 0.
        The dial is rotated L5 to point at 95.
        The dial is rotated R60 to point at 55.
        The dial is rotated L55 to point at 0.
        The dial is rotated L1 to point at 99.
        The dial is rotated L99 to point at 0.
        The dial is rotated R14 to point at 14.
        The dial is rotated L82 to point at 32.

    Because the dial points at 0 a total of three times during this process, the password in this example is 3.

    Analyze the rotations in your attached document. What's the actual password to open the door?

    Function description:
    =====================
    This function processes a list of movement instructions and updates a position within
    a circular list of numbers. For every full cycle (when the position resets to the start
    of the list), a counter is incremented. The final count of these cycles is returned as
    the result.

    :param input_data: A list of strings, where each string represents a movement instruction.
        Each string starts with "L" (move left) or "R" (move right), followed by a number
        indicating steps to move in that direction.
    :return: The number of times the position resets to the beginning of the list during
        the processing of the input data.
    :rtype: int
    """
    position: int = 50
    safe_numbers = list(range(100))
    result: int = 0

    for item in input_data:
        steps = int(item[1:]) if item.startswith("R") else -int(item[1:])
        position = (position + steps) % len(safe_numbers)
        result += (position == 0)

    return result


def solve_puzzle_2(input_data: list) -> int:
    """
    6223

    :param input_data:
    :return:
    """
    position: int = 50
    safe_numbers = 100
    result: int = 0

    for item in input_data:
        steps = int(item[1:])

        if item.startswith("R"):
            total_steps = (position + steps)
            result += total_steps % safe_numbers
        else:
            total_steps = (position - steps) % safe_numbers
            result += total_steps % safe_numbers

        if item.startswith("L"):
            steps = -steps

        position = (position + steps) % safe_numbers

    return result


def main(puzzle: int, input_file: str):
    """

    :param puzzle:
    :param input_file:
    :return:
    """
    if puzzle == 1:
        solution = solve_puzzle_1(get_input_file(filenamen=input_file))
    else:
        solution = solve_puzzle_2(get_input_file(filenamen=input_file))

    print(f"Solution for puzzle {puzzle}: {solution}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--puzzle", "-p",
        action="store",
        dest="puzzle",
        type=int,
        required=True,
        choices=[1, 2],
        help="Number of puzzle to solve."
    )
    parser.add_argument("--input", "-i",
        action="store",
        dest="input_file",
        type=str,
        required=True,
        help="Number of input file for puzzle to solve."
    )
    args = parser.parse_args()

    main(puzzle=args.puzzle, input_file=args.input_file)
