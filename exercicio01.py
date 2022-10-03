# 1 - Faça um programa para leitura de
# três notas parciais de um aluno.
#  O programa deve calcular a média alcançada por
# aluno e apresentar.

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

media = (n1 + n2 + n3)/3
if media == 10:
    print ('Média: {:.1f} Aprovado com Distinção.'.format(media))
if media < 10 and media >= 7:
    print ('Média: {:.1f} Aprovado.'.format(media))
if media <7 :
    print ('Média: {:.1f} Reprovado.'.format(media))