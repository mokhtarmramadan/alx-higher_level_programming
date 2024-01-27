#!/usr/bin/env python3
# Write a function that finds a peak in a list of unsorted integers
def find_peak(nums):
    """ Takes nums list as an arg and finds the peak """
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return None
    else:
        sorted_list = merge_sort(nums)
        peak = sorted_list[len(sorted_list) - 1]
        return peak

def merge_sort(arr):
    """Sorts a list using the merge sort algorithm."""

    if len(arr) <= 1:
        return arr  # Base case: lists with 0 or 1 element are already sorted

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursively sort the left half
    right = merge_sort(arr[mid:])  # Recursively sort the right half

    return merge(left, right)  # Merge the sorted halves

def merge(left, right):
    """Merges two sorted lists into a single sorted list."""

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]  # Add any remaining elements from the left list
    result += right[j:]  # Add any remaining elements from the right list

    return result
