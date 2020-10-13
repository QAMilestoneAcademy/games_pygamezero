import pgzrun
from random import randint

TITLE="SPACE INVASION"
WIDTH=800
HEIGHT=700
CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2
CENTER=(CENTER_X,CENTER_Y)
aliens=[]
move_sequence=0

initial_player_position=(400,400)
player=Actor("player",initial_player_position)

def draw():
    screen.blit("background",(0,0))
    player.draw()
    draw_aliens()

def update():
    check_keys()


def check_keys():
    if keyboard.left:
        if player.x>40:
            player.x-=5
    if keyboard.right:
        if player.x<760:
            player.x+=5

def init_aliens():
    global aliens
    aliens=[]
    for a in range(18):
        alienX=210+(a%6)*80
        alienY=100+int(a/6)*64
        aliens.append(Actor("alien1",(alienX,alienY)))
        aliens[a].status=0

def draw_aliens():
    for alien in aliens:
        alien.draw()

def update_aliens():
    global move_sequence
    move_x=move_y=0
    if move_sequence < 10 or move_sequence > 30:
        move_x = -15
    if move_sequence == 10 or move_sequence == 30:
        move_y = 50
    if move_sequence > 10 and move_sequence < 30:
        move_x = 15

    for alien in aliens:
        animate(
            alien, pos=(alien.x + move_x, alien.y + move_y),
            duration=0.5, tween="linear"
        )
        if randint(0, 1) == 0:
            alien.image = "alien1"
        else:
            alien.image = "alien1b"
            if randint(0, 10) == 0:
                l = len(lasers)
                lasers.append(Actor("laser1", midtop=alien.midbottom))
                lasers[l].status = 0
                lasers[l].type = 0

    move_sequence += 1
    if move_sequence == 40:
        move_sequence = 0




init_aliens()
pgzrun.go()
