from math import sin, cos, tan, radians
angulo = int(input('Qual o ângulo? '))
print(f'O seno, cosseno e tangente deste ângulo são, respectivamente: {sin(radians(angulo)):.2f}, {cos(radians(angulo)):.2f} e '
      f'{tan(radians(angulo)):.2f}.')
