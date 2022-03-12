import time
import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()
# Inicializando o PyGame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait(time.sleep(100))

'''import playsound
playsound.playsound('ex021.mp3')'''
