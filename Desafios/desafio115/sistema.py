from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from desafio111.utilidadeCeV import dado
from time import sleep
arq = 'cadastro.txt'
if not ArquivoExiste(arq):
    criarArq(arq)
while True:
    resp = menu(['Exibir Cadastros', 'Novo Cadastro', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArq(arq)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa
        cab('NOVO CADASTRO')
        n = str(input('Nome: ')).strip().title()
        i = dado.leiaInt('Idade: ')
        cadastrar(arq, n, i)
    elif resp == 3:
        cab('FIM DO PROGRAMA. Até a próxima.')
        break
    else:
        print('\033[31mOpção inválida\033[m')
    sleep(2)

