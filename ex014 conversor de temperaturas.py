#transformação/conversão de temperatura

print('Você quer saber o quanto faz frio ou calor em qualquer lugar do mundo usando as escapas C(celsius) ou F(Fahrenheit)?  ')
C = float(input('Quantos graus Celsius está fazendo agora? '))
F = C*9/5+32
print('Atualmente, com a temperatura em {}C, está marcando {:.2f}F.'.format(C,F))


#convertendo de FAHRENHEIT para CELSIUS
F = float(input('Quantos graus em Fahrenheit está fazendo agora?'))
C = (F-32)*5/9
print('Atualmente com a temperatura em {}F, está marcando {:.2f}C.'.format(F,C))

"""#convertendo CELSIUS para KELVIN
C = float(input('Quantos graus C está fazendo agora? '))
K = C+273.15
print('Atualmente com a temperatura em {}C, está marcando {:.2f}K'.format(C,K))"""

"""#convertendo KELVIN para CELSIUS
K = float(input('Quantos graus K está fazendo agora? '))
C = K-273.15
print('Atualmente com a temperatura em {}K, está marcando {}C'.format(K,C))"""

"""#convertendo de KELVIN para FAHRENHEIT
K = float(input('Quantos graus K está fazendo agora? '))
F = (K-273.15)*9/5+32
print('Atualmente com a temperatura em {}K, está marcando {:.2f}F'.format(K,F))"""

"""#convertendo de FAHRENHEIT para KELVIN
F = float(input('Quantos graus F está fazendoa agora? '))
K = (F-32)*5/9+273.15
print('Atualmente com a temperatura em {}F, está marcando {:.2f}K'.format(F,K))"""