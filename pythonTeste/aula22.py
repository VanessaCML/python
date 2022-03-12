# Importando através de pacotes
from uteis import numeros                    # TODO ARQUIVO .PY PODE SER UM MÓDULO, CONTANTO QUE TENHA FUNÇÕES
n = int(input('Digite um número: '))
fat = numeros.fatorial(n)
print(f'O fatorial de {n} é {fat}.')
print(f'O dobro de {n} é {numeros.dobro(n)}.')

# OU from uteis import triplo, fatorial
# print(f'O triplo de {n} é {triplo(n)}.')

# Importando através de módulos
# Para evitar conflitos no caso de dois módulos terem a mesma função, a melhor forma de importação é a primeira:
# import uteis   fat = uteis.fatorial(n)
