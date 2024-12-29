# // Lab 12. Write a program to implement the backtracking algorithm for the sum of subsets problem

def sumset(i, wt, total):
    if wt == target_sum:
        print("{", *[w[j] for j in range(i + 1) if included[j]], "}")
        return
    if i + 1 < n and wt + total >= target_sum:
        included[i + 1] = 1
        sumset(i + 1, wt + w[i + 1], total - w[i + 1])
        included[i + 1] = 0
        sumset(i + 1, wt, total - w[i + 1])

n = int(input("Enter number of elements: "))
w = sorted(map(int, input("Enter numbers: ").split()))
target_sum = int(input("Enter target sum: "))

if sum(w) < target_sum:
    print("Subset not possible.")
else:
    included = [0] * n
    print("Subset(s) with the given sum:")
    sumset(-1, 0, sum(w))
