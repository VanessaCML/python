from random import randint
import playsound
n = randint(0, 10)
ad = int(input('Pensei num número entre 0 a 10. Tente adivinhar: '))
t = 0
e = 0
acertou = False
while not acertou:
    #playsound.playsound('errou.mp3')
    if 0 <= ad <= 10:
        if n == ad:
            acertou = True
        else:
            if n > ad:
                ad = int(input('Mais... Tente de novo: '))
            elif n < ad:
                ad = int(input('Menos... Tente de novo: '))
    else:
        ad = int(input('É só entre 0 e 10, animal! Nem vou contar isso como tentativa e_e...Tenta de novo aí: '))
        e += 1
    t += 1
if t-e == 1:
    print(f'Acertou de {t-e}a, miserávi!! ')
    playsound.playsound('acertou.mp3')
elif 1 < t-e < 6:
    print(f'Boa! Acertou em {t-e} tentativas.')
elif t-e > 5:
    print(f'Até que enfim! Acertou em {t-e} tentativas... Demorou, hein...')

