#5. Faça um programa que gera uma lista dos números 
# primos existentes entre 1 e um
# número inteiro informado pelo usuário.
def éPrimo(x):
    fator = 2
    while x % fator !=0 and fator < x/2:
        fator = fator + 1
    if x % fator ==0:
        return False
    else:
        return True

n = int(input('Informe um número inteiro: '))

while n > 0:
    if éPrimo(n):
        print (n, 'É primo!!')
    else:
        (n,'Não é primo')
        


