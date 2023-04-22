# from playsound import playsound

# playsound("songs\\a.mp3")

import pygame.mixer as mx

mx.init()
mx.music.load('songs/get_money.mp3')
mx.music.play()

while mx.music.get_busy() == True:
    continue