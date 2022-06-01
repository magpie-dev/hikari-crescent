from typing import Any, List, Sequence

__all__: Sequence[str] = ("arrays_contain_same_elements",)


def arrays_contain_same_elements(arr1: List[Any], arr2: List[Any]) -> bool:
    for i in arr1:
        if i not in arr2:
            return False
    return True
