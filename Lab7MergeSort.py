# // Lab7. Write a program to implement Merge sort algorithm for sorting a list of integers in ascending order


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr [: mid])
    right = merge_sort(arr[mid: ])
    return merge (left, right)
def merge (left, right) :
    result = []
    i=j=0
    while i < len(left) and j< len (right):
        if left[i] < right[j]:
            result. append (left [i])
            i += 1
        else:
            result. append (right [j])
            j += 1
    result.extend (left[i: ])
    result. extend (right [j: ])
    return result
input_list = list(map(int, input("Enter numbers to sort: ").split()))
sorted_list = merge_sort(input_list)
print("Sorted List:", sorted_list)