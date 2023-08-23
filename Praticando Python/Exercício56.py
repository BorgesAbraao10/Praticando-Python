# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
médiaidade = 0 
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for pessoa in range (1,5):
    print ('----- {}º PESSOA -----'.format(pessoa))
    nome = str (input ('nome:')).strip()
    idade = int (input('idade:'))
    sexo = str (input ('sexo [M/F]:')).strip ()
    somaidade += idade 
    if pessoa == 1 and sexo in'Mm':
        maioridadehomem = idade
        nomevelho = nome 
        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade 
            nomevelho = nome 
            if sexo in 'Ff' and idade < 20:
                totmulher20 += 1


médiaidade = somaidade / 4
print ('A média da idade do grupo é de {}.'.format(médiaidade))
print ('O homem mais velho tem {} anos e se chama {}.'.format (médiaidade, nomevelho))
print ('Ao todo são {} mulheres com menos de 20 anos'.format (totmulher20))
