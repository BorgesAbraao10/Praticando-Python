# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int (input('Digite um número:')) # número 'primo' só é divisivel por 1 e por ele mesmo.
total = 0 
for c in range (1, num + 1):
    if num % c == 0:
        print ('\033[34m', end=' ' )
    else:
        print ('\033[m', end=' ')
    print ('{}'.format(c), end= ' ')