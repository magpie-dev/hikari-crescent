from __future__ import annotations

from typing import Any, Sequence

__all__: Sequence[str] = ("arrays_contain_same_elements",)


def arrays_contain_same_elements(arr1: list[Any], arr2: list[Any]) -> bool:
    arr2 = list(arr2)

    for item in arr1:
        if item in arr2:
            arr2.remove(item)
        else:
            return False
    return not arr2
