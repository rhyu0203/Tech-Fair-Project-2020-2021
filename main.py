import pygame
import time
import math
import sys
import random
import sys

# initialize
pygame.init()
pygame.mixer.init()

# screen
screenSize = (1280, 720)
screen = pygame.display.set_mode(screenSize)

# fps
fpsClock = pygame.time.Clock()

# losing screen
losingScreen = pygame.image.load('losing screen.png')
losingScreen = pygame.transform.scale(losingScreen, screenSize)

# caption and icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('tech fair game')

# background
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (1280, 8000))
background2 = pygame.image.load('testBG.png')
background2 = pygame.transform.scale(background2, screenSize)
blackScreenImg = pygame.image.load('black rectangle.jpg')
whiteScreenImg = pygame.image.load('white rectangle.png')
transparentImg = pygame.image.load('transparent.png')

gameWinScreenImg = pygame.image.load('gameWinScreen.png')
gameOverScreenImg = pygame.image.load('gameOverScreen.png')
retryGlowImg = pygame.image.load('retryGlow.png')
returnGlowImg = pygame.image.load('returnGlow.png')

# lives
fullHeart = pygame.image.load('heartFull.png')
fullHeart = pygame.transform.scale(fullHeart, (42, 36))
halfHeart = pygame.image.load('heartHalf.png')
halfHeart = pygame.transform.scale(halfHeart, (42, 36))
enemyHPImg = pygame.image.load('hp bar.png')
enemyHPBackImg = pygame.image.load('hp bar back.png')
hpBarBack = pygame.transform.scale(enemyHPBackImg, (screenSize[0] - 20, 20))

# enemy
enemyImg = pygame.image.load('enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (128, 132))
enemyMouthImg = pygame.image.load('enemyMouth.png')
enemyMouthImg = pygame.transform.scale(enemyMouthImg, (128, 132))
enemyDeathImg = pygame.image.load('enemyDeath.png')
enemyDeathImg = pygame.transform.scale(enemyDeathImg, (128, 132))
enemyWhiteImg = pygame.image.load('enemyWhite.png')

enemyGlowImg = pygame.image.load('enemyGlow.png')
enemyCracksImg = pygame.image.load('enemyCracks.png')
enemyShatterImg1 = pygame.image.load('enemyShatter1.png')
enemyShatterImg2 = pygame.image.load('enemyShatter2.png')
enemyShatterImg3 = pygame.image.load('enemyShatter3.png')


# projectiles
arrowBulletImage = pygame.image.load('arrow bullet.png')
redArcBulletImage = pygame.image.load('red arc bullet.png')
redTriangleGlowBulletImage = pygame.image.load('redTriangleGlow.png')
blueCircleGlowBulletImage = pygame.image.load('blueCircleGlow.png')

circleBullet1 = pygame.image.load('circle bullet 1.png')
circleBullet2 = pygame.image.load('circle bullet 2.png')
circleBullet3 = pygame.image.load('circle bullet 3.png')
circleBullets = [circleBullet1, circleBullet2, circleBullet3]


global beginCursor
beginCursor = screenSize[1]/2 - 3.3*screenSize[1]/15
y_value = beginCursor
global timeGlimmer
timeGlimmer = 126

#character images
archerPortrait = pygame.image.load('charPortraitArcher.png')
archerPortrait = pygame.transform.scale(archerPortrait,(300, 400))
richardPortrait = pygame.image.load('charPortraitRichard.png')
richardPortrait = pygame.transform.scale(richardPortrait,(300, 400))

#color definitoins
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#menu cursor
cursorOne = pygame.image.load('cursor_1.png')
cursorOne = pygame.transform.scale(cursorOne, (int(4*screenSize[1]/6), int(screenSize[1]/6)))
cursorTwo = pygame.image.load('cursor_2.png')
cursorTwo  = pygame.transform.scale(cursorTwo , (int(4*screenSize[1]/6), int(screenSize[1]/6)))
cursorThree = pygame.image.load('cursor_3.png')
cursorThree = pygame.transform.scale(cursorThree , (int(4*screenSize[1]/6), int(screenSize[1]/6)))

#menu images
title_image = pygame.image.load("title.png")
background_image = pygame.image.load("charSelectBG.jpg")
bigbackground_image = pygame.transform.scale(background_image, screenSize)
fadeIn_image = pygame.image.load("fadeIn.png")
fadeIn_image = pygame.transform.scale(fadeIn_image, screenSize)
charSelectBG = pygame.image.load('charSelectBG.jpg')
charSelectBG = pygame.transform.scale(charSelectBG, screenSize)
font = pygame.font.SysFont("gabriola", 75)

returnMenuButton = pygame.image.load('returnToMenu.png')
retryButton = pygame.image.load('retry.png')

returnMenuButton = pygame.transform.scale(returnMenuButton, (int(8*screenSize[1]/15), int(2*screenSize[1]/15)))
retryButton = pygame.transform.scale(retryButton, (int(8*screenSize[1]/15), int(2*screenSize[1]/15)))

#playButton
playButtonImages = []
for i in range(9):
    playButtonImages.append(pygame.image.load("buttonPlay_" + str(i) + ".png"))
    playButtonImages[i] = pygame.transform.scale(playButtonImages[i], (int(8*screenSize[1]/15), int(2*screenSize[1]/15)))
#optionsButton
optionsButtonImages = []
for i in range(9):
    optionsButtonImages.append(pygame.image.load("buttonOptions_" + str(i) + ".png"))
    optionsButtonImages[i] = pygame.transform.scale(optionsButtonImages[i], (int(8*screenSize[1]/15), int(2*screenSize[1]/15)))
#creditsButton
creditsButtonImages = []
for i in range(9):
    creditsButtonImages.append(pygame.image.load("buttonsAnimated_" + str(i) + ".png"))
    creditsButtonImages[i] = pygame.transform.scale(creditsButtonImages[i], (int(8*screenSize[1]/15), int(2*screenSize[1]/15)))
#_________________________________________________________________________________________________________________

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(int(x), int(y))).center)

    return rotated_image, new_rect

def menuCursor(y_value, counter):
    if (counter % 180 <= 60):
        screen.blit(cursorOne, (int(screenSize[0]/2 - screenSize[1]/3), int(y_value)))
    elif (counter % 180 <= 120) and (counter % 180 >= 60):
        screen.blit(cursorTwo, (int(screenSize[0]/2 - screenSize[1]/3), int(y_value)))
    elif (counter % 180 >= 120) and (counter % 180 <= 180):
        screen.blit(cursorThree, (int(screenSize[0]/2 - screenSize[1]/3), int(y_value)))

def messageScreen(text, R, G, B, x, y):
    text = font.render(text, True, (R, G, B))
    screen.blit(text, (x, y))

def titleMessageScreen(text, R, G, B, x, y):
    text = font.render(text, True, (R, G, B))
    screen.blit(text, (x, y))

def menuButtons(images, y, counter):
    if (counter % timeGlimmer <= (timeGlimmer/2)):
        screen.blit(images[0], (int(screenSize[0]/2 - 4*screenSize[1]/15), int(y)))
    for i in range(9):
        if (counter % timeGlimmer >= (i*timeGlimmer/9)) and (counter % timeGlimmer <= ((i+1)*timeGlimmer/9)):
            screen.blit(images[i-7], (int(screenSize[0]/2 - 4*screenSize[1]/15), int(y)))

def startButton(counter):
    menuButtons(playButtonImages, screenSize[1]/2 + screenSize[1]/32 - 3.5*screenSize[1]/15, counter)

def optionsButton(counter):
    menuButtons(optionsButtonImages, screenSize[1]/2 + screenSize[1]/32 - screenSize[1]/15, counter)

def creditsButton(counter):
    menuButtons(creditsButtonImages, screenSize[1]/2 + screenSize[1]/32 + 1.5*screenSize[1]/15, counter)

def fadeOut(width, height, counter):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    for i in range(0, 255, 4):
        fade.set_alpha(i)
        fadeOutScreen(counter)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(1)

def fadeIn(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    screen.blit(fade, (0, 0))
    for i in range(0, 255, 4):
        fade.set_alpha(255-i)
        fadeInScreen()
        screen.blit(fade, (0, 0))
        pygame.display.update()

def fadeInScreen():
    screen.blit(fadeIn_image, [0, 0])

def fadeOutScreen(counter):
    screen.blit(bigbackground_image, [0, 0])
    screen.blit(title_image, [520, 40])
    startButton(counter)
    optionsButton(counter)
    creditsButton(counter)
    menuCursor(y_value, counter)

# refresh menu screen
def menuScreenUpdate(counter):
    screen.blit(bigbackground_image, [0, 0])
    screen.blit(title_image, [520, 40])
    startButton(counter)
    optionsButton(counter)
    creditsButton(counter)
    menuCursor(y_value, counter)

#character choosing:
def characterScreenUpdate(y) :
    screen.fill(black)
    titleMessageScreen("Choose your Character", 255, 255, 255, 360, 50)
    screen.blit(archerPortrait, [int(screenSize[0] / 10) + int(11 * screenSize[0] / 20), 160])
    screen.blit(richardPortrait, [int(screenSize[0] / 10), 160])
    pygame.draw.rect(screen, (255, 255, 255), (int(screenSize[0] / 10), 160, 300, 400), 2)
    pygame.draw.rect(screen, (255, 255, 255), (int(screenSize[0] / 10) + int(11 * screenSize[0] / 20), 160, 300, 400), 2)
    if y:
        pygame.draw.rect(screen, (255, 255, 255), (int(screenSize[0] / 10), 160, 300, 400), 10)
        pygame.draw.rect(screen, (255, 255, 255), (int(screenSize[0] / 10) + int(11 * screenSize[0] / 20), 160, 300, 400), 2)
    else:
        pygame.draw.rect(screen, (255, 255, 255), (int(screenSize[0] / 10), 160, 300, 400), 2)
        pygame.draw.rect(screen, (255, 255, 255), (int(screenSize[0] / 10) + int(11 * screenSize[0] / 20), 160, 300, 400), 10)

def characterChooseScreen():
    ticks = 0
    cursorY = True
    screen.blit(archerPortrait, [int(screenSize[0] / 10) + int(11 * screenSize[0] / 20), 160])
    screen.blit(richardPortrait, [int(screenSize[0] / 10), 160])
    pygame.draw.rect(screen, (255, 255, 255), (int(screenSize[0]/10), 160, 300, 400),  2)
    pygame.draw.rect(screen, (255, 255, 255), (int(screenSize[0] / 10) + int(11 * screenSize[0]/20), 160, 300, 400), 2)
    img = blackScreenImg
    screen.blit(img, [0, 0])
    pygame.display.update()
    while True:
        characterScreenUpdate(cursorY)
        blit_alpha(screen, img, [0, 0], 255 - ticks)
        ticks += 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            events = pygame.event.get()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cursorY = True
                elif event.key == pygame.K_RIGHT:
                    cursorY = False
                if event.key == pygame.K_RETURN:
                    if cursorY:
                        return 2
                    else:
                        return 1
        pygame.display.update()




#def characterChooseArrows():

def options():
    screen.blit(bigbackground_image, [0, 0])
    pygame.display.update()

def credits():
    screen.blit(bigbackground_image, [0, 0])
    pygame.display.update()

def menu():
    counter = 0
    ticks = 0
    menuRunning = True
    pygame.key.set_repeat()
    y_value = beginCursor

    #menu song
    pygame.mixer.music.load('menuSong.mp3')
    pygame.mixer.music.play(-1)

    while True:
        pygame.display.flip()
        counter += 1
        menuScreenUpdate(counter)
        if not(menuRunning):
            ticks += 10
        blit_alpha(screen, blackScreenImg, [0, 0], ticks)
        if(ticks > 255):
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            events = pygame.event.get()
            if event.type == pygame.KEYDOWN:
                '''if event.key == pygame.K_DOWN and y_value == beginCursor:
                    y_value = beginCursor + 2.5*screenSize[1]/15
                elif event.key == pygame.K_DOWN and y_value == beginCursor + 2.5*screenSize[1]/15:
                    y_value = beginCursor + 5*screenSize[1]/15
                if event.key == pygame.K_UP and y_value == beginCursor + 2.5*screenSize[1]/15:
                    y_value = beginCursor
                elif event.key == pygame.K_UP and y_value == beginCursor + 5*screenSize[1]/15:
                    y_value = beginCursor + 2.5*screenSize[1]/15'''
                if event.key == pygame.K_RETURN:
                    if y_value == beginCursor:
                        menuRunning = False
                    elif y_value == beginCursor + 2.5*screenSize[1]/15:
                        menuRunning = False
                    elif y_value == beginCursor + 5*screenSize[1]/15:
                        menuRunning = False
        pygame.display.update();
    pygame.mixer.music.stop()
    AfterMenu = True
    while AfterMenu:
        if (y_value == beginCursor + 2.5*screenSize[1]/15):
            options()
        elif (y_value == beginCursor + 5*screenSize[1]/15):
           credits()
        elif (y_value == beginCursor):
            return(characterChooseScreen())
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (int(-x), int(-y)))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

def getDegrees(x, y):
    if x == 0:
        if y <= 0:
            deg = 0
        else:
            deg = 180
    else:
        if x < 0:
            deg = math.degrees(math.atan(-1.0 * y / x)) + 90
        else:
            deg = math.degrees(math.atan(-1.0 * y / x)) - 90
    return -deg - 90

class Entity:
    def __init__(self, img, hitboxSize, xy, vXY, hp, maxHP, bullets):
        self.img = img
        self.size = self.img.get_size()
        self.hitboxSize = hitboxSize
        self.xy = xy
        self.vXY = vXY
        self.hp = hp
        self.maxHP = maxHP
        self.bullets = bullets

    def updateBulletPos(self, entity, dt):
        ix = entity.xy[0] + entity.vXY[0] * dt
        iy = entity.xy[1] + entity.vXY[1] * dt
        xy = (ix, iy)
        entity.xy = xy
        return xy

    def setBulletDegrees(self, entity):
        if entity.vXY[0] == 0:
            if entity.vXY[1] <= 0:
                deg = 0
            else:
                deg = 180
        else:
            if entity.vXY[0] < 0:
                deg = math.degrees(math.atan(-1.0 * entity.vXY[1] / entity.vXY[0])) + 90
            else:
                deg = math.degrees(math.atan(-1.0 * entity.vXY[1] / entity.vXY[0])) - 90
        return deg

    def update(self, collider, timer, dt, selfIFrames, iFrames, deathTick):
        isHit = False
        x = self.xy[0] + self.vXY[0]*dt
        y = self.xy[1] + self.vXY[1]*dt
        self.xy = (x, y)

        if selfIFrames % 3 != 2:
            if self.maxHP > 0:
                screen.blit(self.img, (int(self.xy[0]), int(self.xy[1])))
            else:
                deg = self.setBulletDegrees(self)
                n = rot_center(self.img, deg, self.xy[0], self.xy[1])
                screen.blit(n[0], (n[1].x, n[1].y))

        for i in range(len(self.bullets) - 1, -1, -1):
            xy = self.updateBulletPos(self.bullets[i], dt)
            deg = self.setBulletDegrees(self.bullets[i])
            n = rot_center(self.bullets[i].img, deg, xy[0], xy[1])

            if deathTick < 730 and iFrames <= 0 and collision(n[0], (n[1].x, n[1].y), collider):
                collider.hp -= 1
                del self.bullets[i]
                iFrames += 1
                isHit = True

        for i in range(len(self.bullets) - 1, -1, -1):
            if len(self.bullets) > 0 and (self.bullets[i].xy[1] > screenSize[1] + 2 * self.bullets[i].size[1] or
                    self.bullets[i].xy[1] < 0 - 2 * self.bullets[i].size[1] or
                    self.bullets[i].xy[0] > screenSize[0] + 2 * self.bullets[i].size[0] or
                    self.bullets[i].xy[0] < 0 - 2 * self.bullets[i].size[0]):
                del self.bullets[i]

        for i in range(len(self.bullets) - 1, -1, -1):
            self.bullets[i].update(collider, timer, dt, 0, iFrames, deathTick)

        return isHit

    def straightShoot(self, img, timer, interval, xy, vXY):
        if timer % interval == 0:
            self.bullets.append(Entity(img, img.get_size(), xy, vXY, 0, 0, []))

# A is the bullet

def collision(imgA, locA, entityB):
    hitboxBLeft = int(entityB.size[0]/2 - entityB.hitboxSize[0]/2)
    hitboxBTop = int(entityB.size[1]/2 - entityB.hitboxSize[1]/2)
    rectA = imgA.get_rect()
    hitboxA = imgA.subsurface(0, 0, rectA.width, rectA.height)
    hitboxB = entityB.img.subsurface(hitboxBLeft, hitboxBTop, entityB.hitboxSize[0], entityB.hitboxSize[1])
    maskA = pygame.mask.from_surface(hitboxA)
    maskB = pygame.mask.from_surface(hitboxB)
    x = int(entityB.xy[0] + hitboxBLeft - locA[0])
    y = int(entityB.xy[1] + hitboxBTop - locA[1])
    if maskA.overlap(maskB, (x, y)) != None:
        return True
    return False

# A should be the bullet, B should be the player/enemy

# def __init__(self, img, hitboxSize, xy, vXY, hp, maxHP, bullets):





#path = []
def gameScreen(playerNum):
    hits = []
    time = pygame.time.get_ticks()
    startTime = pygame.time.get_ticks()
    totalTicks = 0
    timer = -1
    clock = 0
    iFrames = 0
    enemyIFrames = 0
    phaseSwitch = False
    ticks = 0
    deathTick = 0
    enemyShootTick = 0

    pygame.mixer.music.load('1_28_21.mp3')
    pygame.mixer.music.play(-1)

    redTriangleGlowBulletImg = pygame.transform.scale(redTriangleGlowBulletImage, (153, 231))
    redTriangleGlowBulletImg = pygame.transform.rotate(redTriangleGlowBulletImg, 180)
    redTriangleGlowBulletImg = pygame.transform.scale(redTriangleGlowBulletImg, (25, 36))
    redArcBulletImg = pygame.transform.scale(redArcBulletImage, (50, 34))

    playerImgStand = pygame.image.load('ingame_char_sprite' + str(playerNum) + '.png')
    playerImgWalk1 = pygame.image.load('ingame_char_sprite' + str(playerNum) + '_walk1.png')
    playerImgWalk2 = pygame.image.load('ingame_char_sprite' + str(playerNum) + '_walk2.png')

    playerImgStand = pygame.transform.scale(playerImgStand, (64, 64))
    playerImgWalk1 = pygame.transform.scale(playerImgWalk1, (64, 64))
    playerImgWalk2 = pygame.transform.scale(playerImgWalk2, (64, 64))

    playerImg = playerImgStand


    player = Entity(playerImg, (2, 2), (screenSize[0] / 2 - playerImg.get_size()[0] / 2,
                                        screenSize[1] / 2 - playerImg.get_size()[1] / 2), (0, 0), 6, 6, [])

    enemy = Entity(enemyImg, enemyImg.get_size(), (screenSize[0] / 2 - enemyImg.get_size()[0] / 2,
                                                   screenSize[1] / 4 - enemyImg.get_size()[1] / 2), (0, 0), 300, 300, [])

    playerHB = pygame.Rect((int(player.img.get_size()[0] / 2 - player.hitboxSize[0] / 2),
                            int(player.img.get_size()[1] / 2 - player.hitboxSize[1] / 2)), player.hitboxSize)

    rand1 = 1.5 * (2.0 * random.random() - 1)
    rand2 = 1.5 * (2.0 * random.random() - 1)
    rand3 = 1.5 * (2.0 * random.random() - 1)

    enemy.vXY = (0, 0)
    while True:
        dt = fpsClock.tick(30)
        dt = dt/100
        clock = pygame.time.get_ticks() - time
        timer += 1
        totalTicks += 1
        if enemyShootTick > 0:
            enemyShootTick -= 1
            enemy.img = enemyMouthImg
        else:
            enemy.img = enemyImg
        if enemy.hp <= 0:
            enemy.img = enemyDeathImg
        if deathTick > 730:
            enemy.img = transparentImg

        if(clock > 1000):
            #print(timer - ticks)
            ticks = timer
            time = pygame.time.get_ticks()
        screen.blit(background, (0, 0), (0, 6000 - (2*timer % 1000), 1280, 720))
        '''path.append(pygame.Rect(enemy.xy[0] + enemy.size[0] / 2, enemy.xy[1] + enemy.size[1] / 2, 2, 2))
        for i in path:
            pygame.draw.rect(screen, (0, 0, 0), i)'''

        if player.vXY[0] == 0 and player.vXY[1] == 0:
            playerImg = playerImgStand
        elif timer % 20 < 10:
            playerImg = playerImgWalk1
        else:
            playerImg = playerImgWalk2

        player.img = playerImg

    # def straightShoot(self, img, time, interval, xy, vXY):
        a = -(player.xy[0] + player.size[0] / 2) + (pygame.mouse.get_pos()[0])
        b = -(player.xy[1] + player.size[1] / 2) + (pygame.mouse.get_pos()[1])
        k = math.sqrt(a * a + b * b)
        a = 30 * a / k
        b = 30 * b / k

        if(player.hp > 0):
            player.straightShoot(arrowBulletImage, timer, 3, (player.xy[0] + player.size[0] / 2,
                                                         player.xy[1] + player.size[1] / 2), (a, b))


        # enemy behavior
        # phase 1
        if enemy.hp > int(2.0/3 * enemy.maxHP):
            enemy.vXY = (-12*math.sin(math.radians(timer+210)), 6*math.cos(math.radians(2*timer+420)))
            if(timer < 60):
                enemy.vXY = (0, 0)
            c = (player.xy[0] + player.size[0] / 2) - (enemy.xy[0] + enemy.size[0] / 2)
            d = (player.xy[1] + player.size[1] / 2) - (enemy.xy[1] + 3*enemy.size[1] / 4)
            l = math.sqrt(c * c + d * d)
            c = 20 * c / l
            d = 20 * d / l
            l = math.sqrt(c * c + d * d)

            deg = getDegrees(c, d)

            for i in range(16):
                r = i / 16
                r2 = i % 2
                if r2 < 0.5:
                    r2 = -1
                else:
                    r2 = 1
                if(timer > 60):
                    enemy.straightShoot(redTriangleGlowBulletImg, timer - int(8 * r), 30,
                                    (enemy.xy[0] + enemy.size[0] / 2, enemy.xy[1] + 3*enemy.size[1] / 4),
                                    ((r + 1) * l * math.cos(math.radians(deg + 10 * ((1 - r) * r2))),
                                     (r + 1) * l * math.sin(math.radians(deg + 10 * ((1 - r) * r2)))))
                    if (timer - int(8 * r)) % 30 == 0:
                        enemyShootTick = 5

        # phase 2

        elif enemy.hp > int(1.0/3 * enemy.maxHP):
            enemy.vXY = (0, 0)
            if not(phaseSwitch):
                enemyIFrames += 60
                phaseSwitch = True
                blueCircleGlowBulletImg2 = pygame.transform.scale(blueCircleGlowBulletImage, (25, 25))
                blueCircleGlowBulletImg = pygame.transform.scale(blueCircleGlowBulletImage, (50, 50))

            if enemyIFrames == 30:
                a = (screenSize[0] / 2) - (enemy.xy[0] + enemy.size[0] / 2)
                b = (screenSize[1] / 3) - (enemy.xy[1] + enemy.size[1] / 2)
                vA = a/(30*dt)
                vB = b/(30*dt)

            if enemyIFrames < 30 and enemyIFrames > 0:
                enemy.vXY = (vA, vB)

            if enemyIFrames == 0:
                c = (player.xy[0] + player.size[0] / 2) - (enemy.xy[0] + enemy.size[0] / 2)
                d = (player.xy[1] + player.size[1] / 2) - (enemy.xy[1] + 3*enemy.size[1] / 4)
                l = math.sqrt(c * c + d * d)
                c = 15 * c / l
                d = 15 * d / l
                deg = getDegrees(c, d)
                for i in range(5):
                    enemy.straightShoot(redTriangleGlowBulletImg, timer, 30,
                                        (enemy.xy[0] + enemy.size[0] / 2, enemy.xy[1] + 3*enemy.size[1] / 4),
                                        (15 * math.cos(math.radians(deg + 10 * (i-1))),
                                         15 * math.sin(math.radians(deg + 10 * (i-1)))))
                    if timer % 30 == 0:
                        enemyShootTick = 5

                for i in range(4):
                    enemy.straightShoot(blueCircleGlowBulletImg, timer, 20, (enemy.xy[0] + enemy.size[0] / 2, enemy.xy[1] + enemy.size[1] / 2),
                                    (6*math.cos(math.radians(90*i-1*timer)), 6*math.sin(math.radians(90*i-1*timer))))

                for i in range(len(enemy.bullets)):
                    if enemy.bullets[i].size[0] == 50:
                        deg = getDegrees(enemy.bullets[i].vXY[0], enemy.bullets[i].vXY[1])
                        enemy.straightShoot(blueCircleGlowBulletImg2, timer, 30,
                                            (enemy.bullets[i].xy[0] + enemy.bullets[i].size[0] / 2 - 12,
                                             enemy.bullets[i].xy[1] + enemy.bullets[i].size[1] / 2 - 12),
                                            (8 * math.cos(math.radians(deg - 90)),
                                             8 * math.sin(math.radians(deg - 90))))

        #phase 3

        elif enemy.hp > 0:
            if phaseSwitch:
                enemyIFrames += 60
                phaseSwitch = False

            if enemyIFrames == 0:
                a1 = (player.xy[0] + player.size[0] / 2) - (enemy.xy[0] + enemy.size[0] / 2)
                b1 = (player.xy[1] + player.size[1] / 2) - (enemy.xy[1] + enemy.size[1] / 2)
                k = math.sqrt(a1 * a1 + b1 * b1)
                a = 12 * a1 / k
                b = 12 * b1 / k

                enemy.vXY = (a, b)
                if k < 10:
                    enemy.vXY = (0, 0)
                deg = getDegrees(a, b)
                for i in range(4):
                    enemy.straightShoot(redTriangleGlowBulletImg, timer, 30,
                            (enemy.xy[0] + enemy.size[0] / 2 + 45 * i * math.cos(math.radians(deg)) + 45 * math.sin(math.radians(deg)),
                             enemy.xy[1] + enemy.size[1] / 2 + 45 * i * math.sin(math.radians(deg)) - 45 * math.cos(math.radians(deg))),
                            (10 * math.cos(math.radians(deg + 50)),
                             10 * math.sin(math.radians(deg + 50))))

                for i in range(4):
                    enemy.straightShoot(redTriangleGlowBulletImg, timer, 30,
                            (enemy.xy[0] + enemy.size[0] / 2 + 45 * i * math.cos(math.radians(deg)) - 45 * math.sin(math.radians(deg)),
                             enemy.xy[1] + enemy.size[1] / 2 + 45 * i * math.sin(math.radians(deg)) + 45 * math.cos(math.radians(deg))),
                            (10 * math.cos(math.radians(deg - 50)),
                             10 * math.sin(math.radians(deg - 50))))
                for i in range(10):
                    enemy.straightShoot(redArcBulletImg, timer, 30,
                                (enemy.xy[0] + enemy.size[0] / 2,
                                 enemy.xy[1] + enemy.size[1] / 2),
                                (10 * math.cos(math.radians(deg + 36*i)),
                                 10 * math.sin(math.radians(deg + 36*i))))
                    if timer % 30 == 0:
                        enemyShootTick = 5

        # player movement
        playerSpd = 23
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            playerSpd = 11
        if(player.hp <= 0):
            playerSpd = 0
        x = 0
        y = 0
        if keys[pygame.K_a] and not (
                keys[pygame.K_d]) and player.xy[0] >= -player.vXY[0]:
            x = -playerSpd
        elif keys[pygame.K_d] and not (keys[pygame.K_a]) and \
                player.xy[0] <= screenSize[0] - player.vXY[0] - player.size[0]:
            x = playerSpd
        else:
            x = 0
        if keys[pygame.K_w] and not (
                keys[pygame.K_s]) and player.xy[1] >= -player.vXY[1]:
            y = -playerSpd
        elif keys[pygame.K_s] and not (keys[pygame.K_w]) and \
                player.xy[1] <= screenSize[1] - player.vXY[1] - player.size[1]:
            y = playerSpd
        else:
            y = 0


        player.vXY = (x, y)
        if player.hp > 0:
            player.update(enemy, timer, dt, iFrames, enemyIFrames, deathTick)
        if deathTick < 735:
            if enemy.update(player, timer, dt, enemyIFrames, iFrames, deathTick):
                iFrames += 60
            if iFrames > 0:
                iFrames -= 1
            if enemyIFrames > 0:
                enemyIFrames -= 1

        # enemy health bar
        pygame.draw.rect(screen, (0, 0, 0), (10, 10, screenSize[0] - 20, 20), 3)
        screen.blit(hpBarBack, (10, 10))
        if enemy.hp > 0:
            hpBar = pygame.transform.scale(enemyHPImg, (int((screenSize[0] - 20) * (enemy.hp / enemy.maxHP)), 20))
            screen.blit(hpBar, (10, 10))

        # player lives
        for i in range(int(player.hp/2)):
            screen.blit(fullHeart, (10+48 * i, screenSize[1] - 46))
        if player.hp % 2 == 1:
            screen.blit(halfHeart, (10+48*(int(player.hp/2)), screenSize[1] - 46))

        # player death
        if player.hp <= 0:
            pygame.mixer.music.fadeout(1000)
            blit_alpha(screen, playerImg, player.xy, 255 - deathTick)
            blit_alpha(screen, blackScreenImg, (0, 0), deathTick)
            deathTick += 10
            player.xy = (player.xy[0], player.xy[1] + 3)
            if deathTick > 300:
                return 0

        # enemy death
        if enemy.hp <= 0:
            enemy.hitboxSize = (2, 2)
            enemy.vXY = (0, 0)
            if(deathTick < 735):
                blit_alpha(screen, enemyGlowImg, enemy.xy, 255 - deathTick)
                blit_alpha(screen, enemyCracksImg, enemy.xy, deathTick - 315)
                blit_alpha(screen, enemyWhiteImg, enemy.xy, deathTick - 375)
            deathTick += 5
            if deathTick > 735:
                pygame.mixer.music.fadeout(1500)
                xy1 = [64 + -29 + enemy.xy[0] - (deathTick - 730)/3, 66 + -12 + enemy.xy[1] - (deathTick - 730)/5]
                xy2 = [64 + enemy.xy[0], 66 + 32 + enemy.xy[1] + int((deathTick - 730) / 2.5)]
                xy3 = [64 + 26 + enemy.xy[0] + (deathTick - 730)/3, 66 + -13 + enemy.xy[1] - (deathTick - 730)/5]
                r1 = rot_center(enemyShatterImg1, int(rand1 * (deathTick - 735)), xy1[0], xy1[1])
                r2 = rot_center(enemyShatterImg2, int(rand2 * (deathTick - 735)), xy2[0], xy2[1])
                r3 = rot_center(enemyShatterImg3, int(rand3 * (deathTick - 735)), xy3[0], xy3[1])
                img1 = r1[0]
                img2 = r2[0]
                img3 = r3[0]

                blit_alpha(screen, img1, [r1[1].x, r1[1].y], 1000-deathTick)
                blit_alpha(screen, img2, [r2[1].x, r2[1].y], 1000-deathTick)
                blit_alpha(screen, img3, [r3[1].x, r3[1].y], 1000-deathTick)
                blit_alpha(screen, whiteScreenImg, [0, 0], (deathTick - 735))
                if deathTick > 1100:
                    return 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

def gameOverScreen():
    pygame.mixer.music.load('gameover_music.mp3')
    pygame.mixer.music.play(1)
    ticks = 0
    cursorY = True
    screen.blit(gameOverScreenImg, [0, 0])
    screen.blit(retryGlowImg, [0, 0])
    img = pygame.transform.scale(blackScreenImg, (1280, 720))
    screen.blit(img, [0, 0])
    pygame.display.update()
    while True:
        screen.blit(gameOverScreenImg, [0, 0])
        if cursorY:
            screen.blit(retryGlowImg, [0, 0])
        else:
            screen.blit(returnGlowImg, [0, 0])
        blit_alpha(screen, img, [0, 0], 255 - ticks)
        ticks += 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            events = pygame.event.get()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cursorY = True
                elif event.key == pygame.K_RIGHT:
                    cursorY = False
                if event.key == pygame.K_RETURN:
                    if cursorY:
                        return 1 # retry
                    else:
                        return 0 # return to menu
        pygame.display.update()

def gameWinScreen():
    ticks = 0
    screen.blit(gameWinScreenImg, [0, 0])
    screen.blit(retryGlowImg, [0, 0])
    img = pygame.transform.scale(whiteScreenImg, (1280, 720))
    screen.blit(img, [0, 0])
    pygame.display.update()
    while True:
        screen.blit(gameWinScreenImg, [0, 0])
        blit_alpha(screen, img, [0, 0], 255 - ticks)
        ticks += 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            events = pygame.event.get()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        pygame.display.update()

# 0 = play menu
# 1 = skip menu, use player 1
# 2 = skip menu, use player 2
def main(num):
    if num == 0:
        playerNum = menu()
    else:
        playerNum = num
    win = gameScreen(playerNum)
    if win == 0:
        retry = gameOverScreen()
        if retry == 1:
            main(playerNum)
        else:
            main(0)
    else:
        gameWinScreen()
        main(0)

main(0)

pygame.quit()
