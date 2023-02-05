import pygame
pygame.init()
win=pygame.display.set_mode((1000,500))
pygame.mixer.init()
pygame.mixer.music.load("./Assets/The Neighbourhood- The Beach.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("space game")
def frames(shoot,lazerShot,posShotx,posShoty,posX,posX1,posY,posY1):
    win.blit(bg,(0,0))
    pygame.draw.rect(win,(0,0,0),(500,0,10,510))
    win.blit(shipRed,(posX,posY))
    win.blit(shipYellow,(posX1,posY1))
    if shoot:
        win.blit(lazerShot,(posShotx,posShoty))
    pygame.display.update()
def mainFunction():
    global bg,shipRed,shipYellow
    bg=pygame.image.load('./Assets/space.png')
    shipRed=pygame.image.load("./Assets/spaceship_red.png")
    shipYellow=pygame.image.load("./Assets/spaceship_yellow.png")
    lazerShot=pygame.image.load("./Assets/dot1.png")
    run=True
    posX1=1000/4
    posY1=500/3
    posX=1000-(1000/4)
    posY=500/3
    space_width=83
    shotMovement=0
    space_height=100
    clock=pygame.time.Clock()
    while run:
        shoot=False
        posShotx1=posX1+space_width
        posShoty1=posY1+space_height/2-8
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if 520<=posX-5:
                posX-=5
        if key[pygame.K_RIGHT]:
            if 915>posX:
                posX+=5
        if key[pygame.K_UP]:
            if 10<=posY:
                posY-=5
        if key[pygame.K_DOWN]:
            if 500>posY+space_height+5:
                posY+=5
        if key[pygame.K_0]:
            posShotx=posX
            posShoty=posY+space_height/2
        if key[pygame.K_a] or key[pygame.K_q] :
            if 15<posX1:
                posX1-=5
        if key[pygame.K_d]:
            if 410>posX1:
                posX1+=5
        if key[pygame.K_w] or key[pygame.K_z] :
            if 15<posY1:
                posY1-=5
        if key[pygame.K_s]:
            if 500>posY1+space_height+5:
                posY1+=5
        if key[pygame.K_SPACE]:
            shoot=True
        if shoot:
            posShotx1+=10
            if posShotx1>=1000 or  (posX<= posShotx1<=posX+space_width and posY<=posShoty1<=posY+space_height):
                posShotx1=posX1+space_width
        frames(shoot,lazerShot,posShotx1,posShoty1,posX,posX1,posY,posY1)
        
mainFunction()
pygame.quit()