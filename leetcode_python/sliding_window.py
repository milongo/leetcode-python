"""Module with sliding window pattern problems and their solutions."""


def max_sum_subarray(arr: list[int], k: int) -> int:
    """
    Given an array of positive integers and a positive integer k, finds the maximum sum of any contiguous subarray of size k.
    """

    if len(arr) < k:
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(1, len(arr) - k + 1):
        window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
        max_sum = max(window_sum, max_sum)

    return max_sum
