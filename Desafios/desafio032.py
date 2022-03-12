from datetime import date
a = int(input('Digite um ano qualquer: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é bissexto.')
else:
    print(f'O ano {a} não é bissexto.')



#ERRADO, POR QUE? Porque teria que obrigatoriamente cumprir as DUAS condições para poder ser bissexto.
'''a = int(input('Digite um ano qualquer: '))
b = datetime.date
if a % 4 == 0 and a % 400 == 0:
    print(f'O ano {a} é bissexto.')
else:
    print(f'O ano {a} não é bissexto.')'''
