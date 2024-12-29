# //Lab 9. Implement function to print In-Degree, Out-Degree and to display that adjacency matrix


n = int(input("Enter the number of vertices: "))
adj_matrix = [[int(x) for x in input(f"Enter adjacency (1 for edge, 0 for no edge): ").split()] for i in range(n)]
in_degrees = [sum(row) for row in zip(*adj_matrix)]
out_degrees = [sum(row) for row in adj_matrix]
for i in range(n):
    print(f"Vertex {i+1}: In-degree {in_degrees[i]},Out-degree {out_degrees (i)}")
print("Adjacency matrix:")
for row in adj_matrix:
    print (*row)