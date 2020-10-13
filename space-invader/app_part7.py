# Add enemy
import pygame

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))
##Title & Icon
# https://www.flaticon.com/search?word=spaceship
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# set the player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = 370
enemyY = 50
enemyX_change = 0


# draw player using blit(means draw) & screen is known as surface
def player(x, y):
    screen.blit(playerImg, (x, y))


# Add enemy
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# set infinite loop to create the screen running
running = True
while running:
    # RGB-https://www.rapidtables.com/convert/color/hex-to-rgb.html
    screen.fill((0, 0, 0))
    # playerX+=0.2
    # playerX -= 0.1
    # playerY -= 0.1
    # print(playerX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if keystroke is pressed right or left
        # keydown happens when key is pressed
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed ")
            if event.key == pygame.K_LEFT:
                # print("left arrow is pressed")
                # decrease the value of x coordinate
                playerX_change = -0.3

            if event.key == pygame.K_RIGHT:
                # print("right arrow is pressed")
                # decrease the value of x coordinate
                playerX_change = 0.3
        # key up happens when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("keystroke has been released")
                # no change when keystroke is released
                playerX_change = 0

    # should be called after screen.fill else will not be visible
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # update the display inside while loop
    pygame.display.update()
