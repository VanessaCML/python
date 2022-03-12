p = float(input('Digite seu peso em Kg: '))
a = float(input('Digite sua altura em m: '))
imc = p / a**2
if imc < 18.5:
    print(f'{imc:.1f} - ABAIXO DO PESO ')
elif 18.5 <= imc < 25:
    print(f'{imc:.1f} - NORMAL')
elif 25 <= imc < 30:
    print(f'{imc:.1f} - SOBREPESO')
elif 30 <= imc < 40:
    print(f'{imc:.1f} - OBESIDADE')
elif imc >= 40:
    print(f'{imc:.1f} - OBESIDADE MÓRBIDA')
