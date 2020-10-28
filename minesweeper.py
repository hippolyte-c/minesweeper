import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import msvcrt
from random import randrange
import time

from fonctions import bombes, bVoisines, decouvrirCases, remplacerCase, checkDefaite, checkVictoire, flag, unflag, affichage, affichageM, timer, afficherScore, allBombes



def main():
    pygame.init()
    fenetre = pygame.display.set_mode((9*21-1,10*21-1))
    white = (255, 255, 255)
    fenetre.fill(white) #r = 255 b = 255 g 255

    tablo = bombes()
    tablo = bVoisines(tablo)

    for raws in range(9):
        for col in range(9):
            pygame.draw.rect(fenetre, (100, 100, 100), (raws*21, 21+col*21, 20, 20))

    nbFlags = 0

    affichage(fenetre, nbFlags)
    pygame.display.flip()

    debut = int(time.process_time())
    sec = int(time.process_time())

    defaite = False
    running = True

    while running:
        if(not defaite):
            if(int(time.process_time()) > (sec+1)):
                sec +=1
                timer(fenetre, sec-debut)

        for event in pygame.event.get():

            x, y = pygame.mouse.get_pos()
            x = x//21
            y = y//21-1

            if(not defaite and y >= 0):
                if(event.type == pygame.MOUSEBUTTONUP):
                    try:
                        if(tablo[x][y] >= 10 or tablo[x][y] == -1): #10 case déjà découverte et >10 case déminée
                            pass
                        elif(tablo[x][y] == 0):
                            decouvrirCases(fenetre, tablo, x, y)
                        else:
                            remplacerCase(fenetre, tablo, x, y)
                        pygame.display.flip()
                        defaite = checkDefaite(tablo[x][y])

                        if(defaite):
                            allBombes(fenetre, tablo)
                    except IndexError as e:
                        pass

                if(pygame.key.get_mods() and pygame.KMOD_CTRL):
                    if(tablo[x][y] >= 0 and tablo[x][y] < 10):
                        tablo = flag(fenetre, tablo, x, y)
                        nbFlags += 1
                    elif(tablo[x][y] > 10 and tablo[x][y] < 20):
                        tablo = unflag(fenetre, tablo, x, y)
                        nbFlags -= 1

                    affichage(fenetre, nbFlags)

                    pygame.display.flip()

                if(nbFlags == 10):
                    defaite = checkVictoire(tablo)

            if(x == int(9/2) and y == -1):
                if(event.type == pygame.MOUSEBUTTONUP):
                    main()

            if(event.type == pygame.QUIT):
                print("fin du jeu")
                pygame.quit()
                exit()


main()
