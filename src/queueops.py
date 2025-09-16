# src/queueops.py

from typing import List, Tuple, Optional

def take_next(queue: List[str]) -> Tuple[Optional[str], List[str]]:
    """
    Remove and return the first element from the queue.
    Returns a tuple of (element, remaining_queue).
    If queue is empty, returns (None, []).
    """
    if not queue:
        return None, []
    return queue[0], queue[1:]


def move_to_back(queue: List[str], item: str) -> List[str]:
    """
    Move the given item to the back of the queue if it exists.
    If item is not in the queue, return the queue unchanged.
    """
    if item not in queue:
        return queue
    queue_copy = [x for x in queue if x != item]
    queue_copy.append(item)
    return queue_copy


def interleave(list1: List[str], list2: List[str]) -> List[str]:
    """
    Interleave two lists. Remaining elements from the longer list
    are added at the end.
    """
    result = []
    len1, len2 = len(list1), len(list2)
    for i in range(max(len1, len2)):
        if i < len1:
            result.append(list1[i])
        if i < len2:
            result.append(list2[i])
    return result
