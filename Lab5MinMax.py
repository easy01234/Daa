# //Lab 5. Write a program to find minimum and maximum value in an array using divide and conquer


def find_max_min(arr):
    if len(arr)==1:
        return arr[0],arr[0]
    mid=len(arr)//2
    max1,min1=find_max_min(arr[:mid])
    max2,min2=find_max_min (arr [mid:])
    return max(max1, max2), min(min1, min2)
arr= [1,3,8,2,6]
max_val, min_val=find_max_min (arr)
print("Maximum value:",max_val)
print ("Minimum value:", min_val)
