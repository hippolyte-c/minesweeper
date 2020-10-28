from random import randrange
import pygame
import time


def bombes():
    tablo = [[0 for x in range(9)] for y in range(9)]
    i = 0
    while(i < 10):
        x, y = randrange(9), randrange(9)

        if(tablo[x][y] == 0):
            tablo[x][y] = 9
            i+=1 #+1 une bombe

    return tablo


def bVoisines(tablo):
    for x in range(9):
        for y in range(9):
            nbBombes = 0
            if(tablo[x][y] != 9):
                for a in range((x-1), (x+2)):
                    for b in range(y-1, y+2):
                        if(a >= 0 and b >= 0):
                            try:
                                if(tablo[a][b] == 9):
                                    nbBombes += 1
                            except IndexError as e:
                                pass
                tablo[x][y] = nbBombes


    return tablo


def decouvrirCases(fenetre, tablo, x, y):
    global i
    for a in range((x-1), (x+2)):
        for b in range(y-1, y+2):
            if(a >= 0 and b >= 0):
                try:
                    if(tablo[a][b] == 0):
                        pygame.draw.rect(fenetre, (200, 200, 200), (a*21, 21+b*21, 20, 20))
                        tablo[a][b] = -1
                        decouvrirCases(fenetre, tablo, a, b)
                    elif(tablo[a][b] != -1):
                        remplacerCase(fenetre, tablo, a, b)
                except IndexError as e:
                    pass


def remplacerCase(fenetre, tablo, x, y):
    myfont = pygame.font.Font("mine-sweeper.ttf", 12) #Load font object.

    if(tablo[x][y] == 9):

        pygame.draw.rect(fenetre, (200, 50, 50), (x*21, 21+y*21, 20, 20))
        flag = pygame.image.load("miscellaneous.png").convert_alpha()
        fenetre.blit(flag, (x*21+3, 21+y*21+2))

    else:
        textsurface = myfont.render(str(tablo[x][y]), False, (200, 200, 200))
        pygame.draw.rect(fenetre, (50, 50, 255), (x*21, 21+y*21, 20, 20))
        fenetre.blit(textsurface, (x*21+4, 21+y*21+1))

        tablo[x][y] = -1


def checkDefaite(value):
    if(value == 9):
        print("perdu !")
        return True
    else:
        return False

def checkVictoire(tablo):
    saved = 0
    for i in range(9):
        for j in range(9):
            if(tablo[i][j] == 19):
                saved+=1
    if(saved == 10):
        print("victoire !")
        return True



def flag(fenetre, tablo, x, y):
    tablo[x][y] += 10
    flag = pygame.image.load("flag.png").convert_alpha()
    fenetre.blit(flag, (x*21+3, 21+y*21+2))

    return tablo

def unflag(fenetre, tablo, x, y):
    tablo[x][y] -= 10
    pygame.draw.rect(fenetre, (100, 100, 100), (x*21, 21+y*21, 20, 20))

    return tablo

def affichage(fenetre, nbFlags):
    myfont = pygame.font.SysFont("mine-sweeper.ttf", 24)

    textsurface2 = myfont.render(str(10-nbFlags), False, (200, 50, 50))

    pygame.draw.rect(fenetre, (255, 255, 255), (5, 270, 50, 30))

    pygame.draw.rect(fenetre, (200, 200, 200), ((int(9/2))*21, 0, 20, 20))
    happy = pygame.image.load("happy.png").convert_alpha()
    fenetre.blit(happy, ((int(9/2))*21+2, +2))

    pygame.draw.rect(fenetre, (255, 255, 255), (0, 0, 3*21, 21))
    fenetre.blit(textsurface2, (2*21, 0))

def affichageM(fenetre):
    pygame.font.init()
    myfont = pygame.font.SysFont("mine-sweeper.ttf", 24)

    fenetre.fill((255, 255, 255))

    pygame.draw.rect(fenetre, (200, 200, 200), (250, 200, 100, 50))
    textsurface = myfont.render("Lancer une partie", False, (255, 255, 255))
    fenetre.blit(textsurface, (250, 220))

    pygame.draw.rect(fenetre, (200, 200, 200), (250, 300, 100, 50))

    pygame.display.flip()


def timer(fenetre, sec):
    myfont = pygame.font.SysFont("mine-sweeper.ttf", 24)

    pygame.draw.rect(fenetre, (255, 255, 255), ((1+int(9/2))*21, 0, 9*21, 21))

    textsurface = myfont.render(str(sec), False, (200, 50, 50))

    fenetre.blit(textsurface, (6*21+4, 0))

    pygame.display.flip()


def afficherScore(fenetre):
    fenetre.fill((255, 255, 255))

    LB = {}

    with open("scores.txt") as scores:
        for line in scores:
            tablo = []
            for word in line.split():
                tablo.append(word)
            LB.setdefault(tablo[0], tablo[1])

        LB = {k: v for k, v in sorted(LB.items(), key=lambda item: item[1])}

    myfont = pygame.font.SysFont("mine-sweeper.ttf", 24)
    textsurface = myfont.render("SCORES", False, (0, 0, 0))
    fenetre.blit(textsurface, (10*21+4, 2*21-4))

    pygame.draw.rect(fenetre, (200, 200, 200), (250, 450, 100, 50))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONUP):
                x, y = pygame.mouse.get_pos()
                if(event.type == pygame.MOUSEBUTTONUP):
                    if(x > 250 and x < 350 and y > 450 and y < 500):
                        running = False

def allBombes(fenetre, tablo):
    for i in range(9):
        for j in range(9):
            if(tablo[i][j] == 9):
                flag = pygame.image.load("miscellaneous.png").convert_alpha()
                fenetre.blit(flag, (i*21+3, 21+j*21+2))

                pygame.display.flip()
