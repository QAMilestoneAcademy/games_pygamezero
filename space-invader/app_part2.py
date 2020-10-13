#add title , icon
import pygame

#initialize the pygame
pygame.init()

#create screen
screen=pygame.display.set_mode((800,600))
##Title & Icon
#https://www.flaticon.com/search?word=spaceship
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#set infinite loop to create the screen running
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #RGB-https://www.rapidtables.com/convert/color/hex-to-rgb.html
        screen.fill((0,0,0))
        #update the display inside while loop
        pygame.display.update()

