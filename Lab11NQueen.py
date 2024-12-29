# //Lab11. Write program to implement backtracking algorithm for solving problems like Nqueens.


s,faz,m=[[0]*10 for _ in range(10)],0, [0]*25
k = 0
n = int(input("Enter the number of queens: "))
while k >= 0:
    m[k]+=1
    while m[k] <= n and any(m[k] == m[i] or abs(m[k] - m[i]) == abs(k - i) for i in range(k)):
        m[k]+=1
    if m[k] <= n:
        if k == n -1:
            for i in range(n):
                s[i][m[i]] = 1
            print(f"Solution: {faz + 1} \n")
            for i in range(n): 
                for j in range(n):
                    print(f"{s[i][j]:3}", end="")
                print("\n")
            print("\n")
            s, faz = [[0]*10 for _ in range(10)], faz + 1
        else:
            k += 1
            m[k] = 0

    else:
        k -= 1
