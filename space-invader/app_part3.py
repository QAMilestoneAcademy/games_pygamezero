#Add image
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

#set the player
playerImg=pygame.image.load('player.png')
playerX=370
playerY=480

#draw player using blit(means draw) & screen is known as surface
def player():
    screen.blit(playerImg,(playerX,playerY))

#set infinite loop to create the screen running
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #RGB-https://www.rapidtables.com/convert/color/hex-to-rgb.html
        screen.fill((0,0,0))
        #should be called after screen.fill else will not be visible
        player()
        #update the display inside while loop
        pygame.display.update()

