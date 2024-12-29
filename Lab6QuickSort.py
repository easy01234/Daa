# //Lab6 Write a test program to implement Divide and Conquer Strategy. Eg: Quick sort algorithm for sorting list of integers in ascending order.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr [0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort (greater)
input_list = list (map(int, input ("Enter numbers: ").split()))
sorted_list = quick_sort(input_list)
print(sorted_list)