n1 = int (input('Primeiro valor:'))
n2 = int (input('Segundo valor:'))
opção = 0
while opção != 5: # ! significa diferente.
    print ('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int (input('>>>>>>>>>>>>Qual é a sua opção:'))
    if opção == 1:
        soma = n1 + n2
        print ('A soma entre {} e {} é {}'.format(n1,n2,soma))
    
    elif opção == 2:
        produto = n1*n2
        print ('O resultado de {} x {} é {}'.format(n1,n2,produto))

    elif opção == 3:
        if n1>n2:
            maior = n1

    elif opção == 4:
        print ('informe os números novamente:')
        n1 = int (input ('Primeiro valor:'))
        n2 = int (input ('Segundo valor: '))

    elif opção == 5:
        print ('Finalizando....')

    else:
        print ('Opção invalida. Tente novamente.')
        print ('=-='*15)
print('Fim do programa! Volte sempre!.')