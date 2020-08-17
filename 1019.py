N = int(input())
A = N//3600
N = N%3600
B = N//60
C = N%60
print('{}:{}:{}' .format(A, B, C))