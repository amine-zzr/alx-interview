#!/usr/bin/python3
""" Method that determines if all boxes can be opened """


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.

    Args:
        boxes (a list of lists): contain keys to the other boxes

    Returns:
        boolean: True if all boxes can be opened, else return False
    """
    n = len(boxes)

    opened = [False] * n
    opened[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
