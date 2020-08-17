from decimal import Decimal
TETA = float(input())
N = TETA
A = N//100
N = N%100
B = N//50
N = N%50
C = N//20
N = N%20
D = N//10
N = N%10
E = N//5
N = N%5
F = N//2
N = N%2
#moedas
N = N*1000
G = N//1000
N = N%1000
H = N//500
N = N%500
I = N//250
N = N%250
J = N//100
N = N%100
K = N//50
N = N%50
L = N
print('NOTAS:')
print('{} nota(s) de R$ 100.00' .format(int(A)))
print('{} nota(s) de R$ 50.00' .format(int(B)))
print('{} nota(s) de R$ 20.00' .format(int(C)))
print('{} nota(s) de R$ 10.00' .format(int(D)))
print('{} nota(s) de R$ 5.00' .format(int(E)))
print('{} nota(s) de R$ 2.00' .format(int(F)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00' .format(int(G)))
print('{} moeda(s) de R$ 0.50' .format(int(H)))
print('{} moeda(s) de R$ 0.25' .format(int(I)))
print('{} moeda(s) de R$ 0.10' .format(int(J)))
print('{} moeda(s) de R$ 0.05' .format(int(K)))
print('{} moeda(s) de R$ 0.01' .format(int(L)))