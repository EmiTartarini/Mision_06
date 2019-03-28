#Emiliano Tartarini A01372663
#Mision 6

import pygame
import math
import random

ancho=850
alto=850
blanco=(255,255,255)
negro=(0,0,0)

def adquirirColor():
    
    Rojo=random.randrange(0,255)
    Verde=random.randrange(0,255)
    
    Azul=random.randrange(0,255)
    colorX=(Rojo,Verde,Azul)
    return colorX

def dibujar(r,R,l):

    pygame.init()
    ventana=pygame.display.set_mode((ancho,alto))
    reloj=pygame.time.Clock()
    termina=False

    while not termina

        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                termina=True

        ventana.fill(negro)
        for angulo in range(0,(360*(r//math.gcd(r, R))+1))

            color=adquirirColor()
           
            a=math.radians(((angulo)))
            k=r/R
            
            x=int(R*((1-k)*math.cos(a)+l*k*math.cos(((1-k)/k)*a))
            y=int(R * ((1 - k) * math.sin(a) + L * k * math.sin(((1-k) /k)*a)))
            pygame.draw.circle(ventana, color, (x + ANCHO // 2, ALTO // 2 - y), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def main():
    r=int(input("introduce r:"))
    R=int(input("introduce R:"))
    L=float(input("introduce L:"))


    dibujar(r,R,L)


main()