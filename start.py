import pygame
import os
import time
import webbrowser





pygame.init()
WIDTH, HEIGHT = 760, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T++ COMPILER")
clock = pygame.time.Clock()
black = (0,0,0)
bright_green =(169, 214, 229)
bright_blue = (44, 125, 160)
bright_red = (1, 42, 74)




# Data needed for project as colors and images
WHITE = (255,255,255)
DRACULA = (57,57,57)
SIDEBAR_DRACULA = (77, 80, 82)
FPS = 60
LOGO_IMG = pygame.image.load(os.path.join('images','compiler.jpg'))
BACKGROUND_IMG = pygame.image.load(os.path.join('images','background.png'))
LOGO = pygame.transform.scale(LOGO_IMG,(120,120))
BACK = pygame.transform.scale(BACKGROUND_IMG,(760,500))




def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(WIN,ac,(x,y,w,h))
        if click[0] == 1 and action!= None:
            if action == "play":
                main()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()

    else:
        pygame.draw.rect(WIN,ic,(x,y,w,h))
    smalltext = pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect = text_objects(msg,smalltext,WHITE)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    WIN.blit(textsurf, textrect)


def text_objects(text,font,color):
    textsurface = font.render(text,True,color)
    return textsurface,textsurface.get_rect()




def intro_loop():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        WIN.blit(BACK,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf , TextRect = text_objects("T++ Compiler",largeText,black)
        TextRect.center = (400,100)
        WIN.blit(TextSurf,TextRect)
        button("START",150,420,100,50,(111, 114, 117),bright_blue,"play")
        button("QUIT",550,420,100,50,bright_red,(111, 114, 117),"quit")
        button("INSTRUCTION",300,420,200,50,bright_blue,bright_red,"intro")
        pygame.display.update()
        clock.tick(FPS)

def draw_window(color,pos):
    WIN.fill(color)
    WIN.blit(LOGO,pos)
    pygame.display.update()


def main():
     # intro = True
     #
     # while intro:
     #     for event in pygame.event.get():
     #         if event.type == pygame.QUIT:
     #             pygame.quit()
     #             quit()
     #             sys.exit()
     #     WIN.fill(DRACULA)
     #     WIN.blit(LOGO,(320,0))
     #     button("BACK",10,400,100,50,bright_green,bright_blue,"menu")
     #     pygame.display.update()
     #     clock.tick(FPS)
     # print("Hello man")
     def exec_full(filepath):

         global_namespace = {
             "__file__": filepath,
             "__name__": "__main__",
         }
         with open(filepath, 'rb') as file:
             exec(compile(file.read(), filepath, 'exec'), global_namespace)

     exec_full("main.py")






def introduction():
    intro = True
    link_color = (0, 0, 0)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        WIN.fill(WHITE)
        WIN.blit(LOGO,(320,0))
        button("BACK",30,400,100,50,bright_green,bright_blue,"menu")
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf , TextRect = text_objects("Our Language Documentation : ",largeText,black)
        link_font = pygame.font.SysFont('Consolas', 50)
        rect = WIN.blit(link_font.render("Click Here", True, link_color), (220, 250))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if rect.collidepoint(pos):
                    webbrowser.open(r"https://github.com/Ayoubkassi/Tamazight")

        if rect.collidepoint(pygame.mouse.get_pos()):
            link_color = (70, 29, 219)

        else:
            link_color = (0, 0, 0)

        TextRect.center = (400,160)
        WIN.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(FPS)


#

intro_loop()
