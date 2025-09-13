from typing import Iterable, List, Any


def find_duplicates(chars: Iterable[Any]) -> List[Any]:
    """
    Return items that appear >= 2 times, preserving first-seen order.
    Unhashable items are skipped.
    """
    if chars is None:
        return []
    seen = {}
    order = []
    for ch in chars:
        try:
            seen[ch] = seen.get(ch, 0) + 1
            if seen[ch] == 1:
                order.append(ch)
        except TypeError:
            # skip unhashable items
            continue
    return [ch for ch in order if seen.get(ch, 0) >= 2]


if __name__ == "__main__":
    sample = ['c','a','i','o','p','a']
    print(find_duplicates(sample))  # ['a']
