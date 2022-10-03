#3. Façaum Programa que peça a temperatura
#  em graus Fahrenheit, transforme e mostre a
# temperatura em graus Celsius. C = 5 * ((F-32) / 9).

F = float(input('Digite a temperatura em Fahrenheit, para ser exibida em Celsius: '))

C = 5 * ((F-32) / 9)

print ('A temperatura de {:.1f} F, corresponde a {:.1f} C'.format(F, C))

