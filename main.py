import random
import pygame
import math
# To initialize the game
pygame.init()
# make screen
screen = pygame.display.set_mode((800, 600))

# Background

background = pygame.image.load("space.png")

# Title and loop
pygame.display.set_caption("Wilbert's Space Adventure")
# set icon
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# implementing the player ship
playerImg = pygame.image.load("enemy.png")
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
# Creating the alien enemies
    enemyImg.append(pygame.image.load("space-ship.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(15)

# Creating the alien enemies
bulletImg = pygame.image.load("bullet-2.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
# ready state means you cannot see the bullet on the screen
# fire means the bullet is already moving so you cannot change anything
bulletState = "ready"

# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
# Game over text

over_font  = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))


def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x,y):
    # draw image of player ship on window
    screen.blit(playerImg,(x,y))


def enemy(x,y,i):
    # draw image of player ship on window
    screen.blit(enemyImg[i],(x,y))


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y+ 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    return False

# game loop
run = True
while run:
    # rgb
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    # loop across every game event to check if program has quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # if key stroke is pressed check whether it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    # get the current x coordinate of the space ship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key -- pygame.K_RIGHT:
                playerX_change = 0

    # Making the player move

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Making the enemy move
    for i in range(num_of_enemies):
        # game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i],i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()









