"""Problems with arrays or hashes"""


def has_duplicate(nums: list[int]) -> bool:
    """Computes whether array has duplicates."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


def is_anagram(s: str, t: str) -> bool:
    """Determines if two strings are anagrams of each other."""

    seen = {}
    for char in s:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1

    for char in t:
        if char in seen:
            seen[char] -= 1
        else:
            return False

    for val in seen.values():
        if val != 0:
            return False

    return True
