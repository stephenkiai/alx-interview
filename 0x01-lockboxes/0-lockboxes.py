#!/usr/bin/python3
"""
method to determines if all boxex can be opened
"""


def canUnlockAll(boxes):
    """
     Function to determine if all boxes can be unlocked.

    Returns:
        bool: True if all boxes can be opened, else False
    """
    if not boxes or not boxes[0]:
        return False

    # Set to keep track of opened boxes
    opened_boxes = {0}

    # List to keep track of newly found keys
    new_keys = [0]

    while new_keys:
        current_box = new_keys.pop()

        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                new_keys.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
