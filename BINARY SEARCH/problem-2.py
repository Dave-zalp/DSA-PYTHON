# 2. Temperature Prediction
# You have an array of daily temperatures recorded for a month, sorted in ascending order.
# Write a function to find the day when the temperature was closest to a given target temperature.
# If there are multiple such days, return the first occurrence.

# Temp
# day = 4

import math


class Temperature:
    def __init__(self, arr, target_temp):
        self.arr = arr
        self.target_temp = target_temp

    def locate_close(self):
        close_temp = min(self.arr, key=lambda x: abs(x - self.target_temp))

        if close_temp:
            print(f'The Temperature is closer to the {self.arr.index(close_temp)} day')
        else:
            print('None')


find_temp = Temperature([12, 3, 5, 7, 9], 10)
print(find_temp.locate_close())
