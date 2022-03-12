import emoji
import pygame
frase = str(input('Digite uma frase: ')).upper().strip()
frase = frase.replace('Á', 'A')
frase = frase.replace('À', 'A')
frase = frase.replace('Ã', 'A')
frase = frase.replace('Â', 'A')
b = frase.find('A')
print(f'Essa frase tem {frase.count("A")} letras A.')
print(f'A posição em que a letra A aparece pela primeira vez é: {frase.find("A")+1}')
print(f'A posição em que a letra A aparece pela última vez é: {frase.rfind("A")+1}')
print(emoji.emojize(":heart:", use_aliases=True))





#ATUALIZAÇÃO: print(f'Essa frase tem {frase.count("A")} letras A.') - aspas duplas dentro de outras aspas!
'''frase é objeto, .count() é método'''