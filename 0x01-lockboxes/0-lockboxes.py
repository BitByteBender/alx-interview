#!/usr/bin/python3
""" Solving Lockboxes interview question """


def canUnlockAll(boxes):
    """
        Tracks opened boxes starting from the 1st one
        returns: True if boxes can be opened otherwise False
    """
    if not boxes:
        return False

    list_boxes = set()
    checker = {0}

    while checker:
        current = checker.pop()
        if current not in list_boxes:
            list_boxes.add(current)
            checker.update(box for box in boxes[current] if box < len(boxes))

    return len(list_boxes) == len(boxes)
