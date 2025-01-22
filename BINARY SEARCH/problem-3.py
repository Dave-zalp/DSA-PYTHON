# 2. Temperature Prediction
# You have an array of daily temperatures recorded for a month, sorted in ascending order.
# Write a function to find the day when the temperature was closest to a given target temperature.
# # If there are multiple such days, return the first occurrence.

# Temp
# day = 4


# temp = [23, 56, 78, 88, 99, 100]
# target_temp = 79
# Answer = 3

def find_closest_temperature(temperatures, target_temp):
    low, high = 0, len(temperatures) - 1
    closest_index = 0

    while low <= high:
        mid = (low + high) // 2

        # Update the closest index if current temperature is closer
        if abs(temperatures[mid] - target_temp) < abs(temperatures[closest_index] - target_temp):
            closest_index = mid
        elif abs(temperatures[mid] - target_temp) == abs(temperatures[closest_index] - target_temp):
            # In case of a tie, take the first occurrence
            closest_index = min(closest_index, mid)

        # Adjust the search range
        if temperatures[mid] < target_temp:
            low = mid + 1
        else:
            high = mid - 1

    return closest_index + 1  # Days are typically 1-indexed


obj = find_closest_temperature([23, 56, 78, 88, 99, 100], 100)
print(obj)


