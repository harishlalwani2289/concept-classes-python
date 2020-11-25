'''
    Find the Minimum length Unsorted Subarray, sorting which makes the complete array sorted
Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such that sorting this subarray makes the whole array sorted.

Examples:
1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], your program should be able to find that the subarray lies between the indexes 3 and 8.

2) If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50], your program should be able to find that the subarray lies between the indexes 2 and 5.
'''


array = [10, 12, 20, 26, 27, 30, 25, 40, 32, 31, 35, 36, 50, 60]

# First we should find the first element such that
# the next element is less than it
n = len(array)
start = 0
end = 0
for i in range(n):
    if array[i] > array[i + 1]:
        start = i
        break

# Then from rear we have to find the first element which is
# less than its left neighbor
for i in range(n - 1, 0, -1):
    if array[i] < array[i - 1]:
        end = i
        break;

print(start, end)

# Now our interim sub array lies between the index
# start and end but this is not the exact array because there can be more elements to be included
# We have to find the max and min of this sub array and then find the number
# which greater than minimum on left of this sub array -- > for our new start index
# and less than the maximum in right of this sub array -- > for our new end index

max_array = max(array[start:end + 1])
min_array = min(array[start:end + 1])
print(max_array, min_array)

# Now lets find the number which is greater than our minimum in left of our sub array
for i in range(start):
    if (array[i] > min_array):
        start = i
        break

for i in range(n - 1, end, -1):
    if (array[i] < max_array):
        end = i
        break

print(start, end)
