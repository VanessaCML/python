from random import randint
from time import sleep
import playsound
import emoji
print('-=-'*(16+1))
print('Tente adivinhar, vou pensar num número entre 1 e 5')
print('-=-'*(16+1))
pergunta = int(input('Qual número pensei? '))
n = randint(1, 5)
print(emoji.emojize(':heart:PROCESSANDO  :heart:', use_aliases=True))
sleep(2)
if pergunta == n:
    print(emoji.emojize('\nAcertou, miserávi! :smile:', use_aliases=True))
    playsound.playsound('acertou.mp3')
else:
    print(emoji.emojize(f'\nERRRROU! Eu pensei no número {n}! :shit:', use_aliases=True))
    playsound.playsound('errou.mp3')
