def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}m x {comp}m é de {a} m².')


l = float(input('Largura do terreno em m: '))
c = float(input('Comprimento do terreno em m: '))
area(l, c)
