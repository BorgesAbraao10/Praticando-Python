# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*15)

primeiro = int (input('Digite o primeiro termo:'))
razão = int (input('Razão da Pa:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais    
    while cont <= total:
        print ('{}->'.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int (input('Quantos termos você quer mostrar a mais?'))
print ('Progressão mostrada com {} termos utilizados'.format (total))