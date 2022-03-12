from math import hypot
cat1 = int(input('Qual o comprimento do cateto oposto? '))
cat2 = int(input('Qual o comprimento do cateto adjacente? '))
print(f'O comprimento da hipotenusa desse triângulo retângulo é {hypot(cat1,cat2):.2f}')

