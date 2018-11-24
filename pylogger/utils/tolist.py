from typing import List


def to_list(o: List[object] or object) -> object:
    ltr = list()

    if o is None:
        return ltr

    if isinstance(o, list):
        ltr.extend(o)
    else:
        ltr.append(o)

    return ltr
