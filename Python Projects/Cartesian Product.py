from itertools import product

A = list(map(int,input().split())) 
B = list(map(int,input().split())) 
res = list(product(A,B))
res.sort()

for i in res:
    print(i, end = " ")