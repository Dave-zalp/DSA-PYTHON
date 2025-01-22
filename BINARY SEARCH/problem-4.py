# 5. Finding the Missing Number
# You are given a sorted array of unique integers in which one number is missing,
# but all other numbers follow a natural sequence (e.g., [1, 2, 4, 5]).
# Use binary search to determine the missing number.

# Solution case
# input = [1, 2, 4, 5]
# Output = 3
# Determine the sequence between each number. And then find the most occurring sequential number


def find_missing_num(arr):
    low, high = 0, len(arr) - 1             # low = 0, high = 8                  low = 5, high = 8

    while low < high:
        mid = low + (high - low) // 2                # mid = 0+(8-0) //2 = 4       mid = 5 + (8-5) //2 = 4

        # Check if the difference matches the expected difference
        if arr[mid] == mid + arr[0]:                  # if 5 == 4+1. Then low = 4+1 = 5
            # The missing number is in the right half
            low = mid + 1
        else:
            # The missing number is in the left half
            high = mid                               # high = 1

    # The missing number is determined by the position
    return low + arr[0]


print(find_missing_num([1, 2, 3, 4, 5, 6, 7, 8, 10]))
