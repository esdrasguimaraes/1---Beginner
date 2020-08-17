A = int(input())
B = A//365
A = A%365
C = A//30
D = A%30
print('{} ano(s)' .format(B))
print('{} mes(es)' .format(C))
print('{} dia(s)' .format(D))