# Lab8 Write C program that accepts the vertices and edges for a graph and stores it as an
# adjacency matrix.



vertices, edges = map(int, input ("Enter vertices and edges: ").split())
adj_matrix = [[0] * vertices for _ in range(vertices)]
print( "Enter edges (u, v):")
for _ in range(edges):
    u , v = map(int, input().split())
    adj_matrix[u - 1][v - 1] = adj_matrix[v - 1][u - 1] = 1
print("\nAdjacency Matrix:")
for i in range(vertices):
     for j in range(vertices):
        print (adj_matrix[i][j], end=" ")
     print("\n")