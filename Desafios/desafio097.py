def escreva(msg):
    print('~'*(len(msg)))
    print(msg)
    print('~'*(len(msg)))


escreva(f'{"Oi, mundo!":^15}')
escreva(f'{"TESTADOR DE TEXTOS":^30}')
