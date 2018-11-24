from typing import List


def to_list(o: List[object] or object) -> object:
    ltr = list()

    if isinstance(o, list):
        ltr.extend(o)
    else:
        ltr.append(o)

    return ltr
