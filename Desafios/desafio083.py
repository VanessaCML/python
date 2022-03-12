exp = str(input('Digite uma expressão: '))
pilha = []
c = 0
for simbolo in exp:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbolo)
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')



'''exp = str(input('Digite a expressão: '))
teste = list(exp)
d = e = 0
for pos, c in enumerate(teste):
    if pos==0 and teste[0]==')':
        print('Expressão errada')
    else:
        if teste[pos] == '(':
            d += 1
        if teste[pos] == ')':
            e += 1
if e == d:
    print('Expressão CORRETA!')
else:
    print('Expressão INCORRETA!')'''