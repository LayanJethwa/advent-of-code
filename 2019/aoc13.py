import math
import adj
import intcode
import pygame
import time

ll = open("input.txt",'r').read().splitlines()
for l in ll:
    l = [int(l) for l in l.split(',')]

ol = l.copy()
p = 0
b = 0
running = True
c = 0
out = []
g = {}
lenl = len(l)

while running:
    o = intcode.run(l.copy(),[0],True,p,b,lenl,1000)
    if len(o) < 5:
        running = False
    else:
        l = o[0]
        p = o[1]
        b = o[4]
        c += 1
        out.append(o[3][0])
        if c%3 == 0:
            g[(out[0],out[1])] = out[2]
            out = []

print(list(g.values()).count(2))

maxx = (max([x[0] for x in (list(g.keys()))])+1)
maxy = (max([x[1] for x in (list(g.keys()))])+1)




pygame.init()
screen = pygame.display.set_mode((maxx*20, (maxy*20)+100))
pygame.display.set_caption('Advent of Code 2019 Day 13 Part 2')

l = ol.copy()       
l[0] = 2
p = 0
b = 0
running = True
co = 0
out = []
g = {}
lenl = len(l)
pd = 0
by = 0
py = 0
s = 0
ot = time.time()

while running:
    o = intcode.run(l.copy(),[pd],True,p,b,lenl,1000)
    if len(o) < 5:
        running = False
    else:
        l = o[0]
        p = o[1]
        b = o[4]
        co += 1
        out.append(o[3][0])
        if co%3 == 0 and len(out) == 3:
            if out[0] != -1:
                g[(out[0],out[1])] = out[2]
                out = []

                dt = time.time()
                screen.fill((0,0,0))
                for i in range(maxx):
                    for j in range(maxy):
                        t = pygame.Rect(i*20, (j*20), 20, 20)
                        c = str(g.get((i,j),0))
                        if c == '0':
                            pygame.draw.rect(screen, (255,255,255), t)
                        elif c == '1':
                            pygame.draw.rect(screen, (0,0,0), t)
                        elif c == '2':
                            pygame.draw.rect(screen, (219,55,55), t)
                        elif c == '3':
                            pygame.draw.rect(screen, (43,224,70), t)
                            py = i
                        elif c == '4':
                            pygame.draw.rect(screen, (0,0,0), t)
                            by = i

                if len(g) >= (maxx*maxy):
                    secs = time.time()-ot
                    if secs > 300:
                        sl = 0
                    else:
                        sl = 0.5/(secs*10)
                    time.sleep(sl)

                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        exit()

                if len(g) >= (maxx*maxy):
                    if py < by:
                        pd = 1
                    elif py > by:
                        pd = -1
                    else:
                        pd = 0
                
            if len(out) == 3:
                if (out[0],out[1]) == (-1,0):
                    s = out[2]
                out = []

            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(str(s), True, (0,255,0), (0,0,0))
            textRect = text.get_rect()
            textRect.center = ((maxx*20)//2,(maxy*20)+50)
            screen.blit(text,textRect)

            pygame.display.update()

                

