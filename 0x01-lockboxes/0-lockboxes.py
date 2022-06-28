#!/usr/bin/python3

def canUnlockAll(boxes):
    '''
    determines if all the boxes can be opened 
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        box = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if box != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
