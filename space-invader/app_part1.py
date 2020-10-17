import pygame

#initialize the pygame
pygame.init()

#create screen
screen=pygame.display.set_mode((800,600))

#set infinite loop to create the screen running
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

