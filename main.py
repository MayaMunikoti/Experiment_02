import pygame
pygame.init()

screen = pygame.display.set_mode((3840,2160),pygame.FULLSCREEN)

exitImg = pygame.image.load('realexitsymbol.png')
startImg = pygame.image.load('startbg.png')
lab = pygame.image.load('lab.png')
stairs = pygame.image.load('stairs.png')
laboverlay = pygame.image.load('laboverlay.png')
up = pygame.image.load('upbutton.png')
down = pygame.image.load('downbutton.png')
gameoverbg = pygame.image.load('gameoverbg.png')
gameoveroverlay = pygame.image.load('gameovertxt.png')
toxicoverlay = pygame.image.load('toxicoverlay.png')
stairsoverlay = pygame.image.load('stairsoverlay.png')
darkoverlay = pygame.image.load('darkoverlay.png')
back = pygame.image.load('backbutton.png')
sides = pygame.image.load('sidesbutton.png')
secret = pygame.image.load('secretbutton.png')
off = pygame.image.load('offbutton.png')
on = pygame.image.load('onbutton.png')
explanation1 = pygame.image.load('explanationactually1.png')
explanation2 = pygame.image.load('explanation2.png')
explanation3 = pygame.image.load('explanation1.png')
winbg = pygame.image.load('winbg.png')
toxicbg = pygame.image.load('toxicbg.png')
darkbg = pygame.image.load('darkbg.png')
win1 = pygame.image.load('gamewin1.png')
win2 = pygame.image.load('gamewin2.png')
escape = pygame.image.load('escape.png')
retry = pygame.image.load('retry.png')
playagain = pygame.image.load('playagain.png')
start = pygame.image.load('startbttn.png')

startImg = pygame.transform.scale(startImg, (screen.get_width(), screen.get_height()))
lab = pygame.transform.scale(lab, (screen.get_width(), screen.get_height()))
stairs = pygame.transform.scale(stairs, (screen.get_width(), screen.get_height()))
winbg = pygame.transform.scale(winbg, (screen.get_width(), screen.get_height()))
toxicbg = pygame.transform.scale(toxicbg, (screen.get_width(), screen.get_height()))
darkbg = pygame.transform.scale(darkbg, (screen.get_width(), screen.get_height()))
gameoverbg = pygame.transform.scale(gameoverbg, (screen.get_width(), screen.get_height()))

overlay_reference = pygame.transform.scale(laboverlay, (screen.get_width()//1.6, screen.get_height()//2.5))

class Scene:
    def __init__(self, image, overlay):
        self.image = image
        self.overlay = overlay


    def draw(self):
        screen.fill((0, 0, 0))
        screen.blit(self.image,(0, 0))
        pygame.display.flip()
        pygame.time.delay(1000)
        screen.blit(pygame.transform.scale(self.overlay, (screen.get_width()//1.6, screen.get_height()//2.5)), (screen.get_width()//5.3, screen.get_height()//4))
        pygame.display.flip()
class gameoverScene:
    def __init__(self, bg, explanation,gameover):
        self.explanation = explanation
        self.gameover = gameover
        self.bg = bg


    def draw(self):
        screen.fill((0, 0, 0))
        screen.blit(self.bg,(0,0))
        screen.blit(pygame.transform.scale(self.explanation, (screen.get_width() // 2, screen.get_height() // 1.2)),(screen.get_width() // 3.9, screen.get_height() // 10))
        pygame.display.flip()
        pygame.time.delay(1000)
        screen.blit(pygame.transform.scale(self.gameover, (screen.get_width() // 2, screen.get_height() // 1.2)),(screen.get_width() // 3.9, screen.get_height() // 10))
        pygame.display.flip()
class Button:
    def __init__(self, w, h, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
        self.rect.size = (w,h)

    def draw(self):
        screen.blit(pygame.transform.scale(self.image, (self.rect.w, self.rect.h)), (self.rect.x, self.rect.y))
        pygame.display.flip()

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)



exitbuttonparam = (
    screen.get_width() //16,
    screen.get_height() // 11,
    overlay_reference.get_width()//.615, overlay_reference.get_height()//20.5,
    exitImg
)

leftbuttonparam = (
    overlay_reference.get_width() // 6,
    overlay_reference.get_height() // 4,
    overlay_reference.get_width()//1.25,
    overlay_reference.get_height() // .75,
)

rightbuttonparam = (
    overlay_reference.get_width() // 6,
    overlay_reference.get_height() // 4,
    overlay_reference.get_width()//.98,
    overlay_reference.get_height() // .75,
)
exit_button = Button(*exitbuttonparam)

start_button = Button(overlay_reference.get_width() // 6,overlay_reference.get_height() // 8,
                      screen.get_width()//1.6, screen.get_height() // 2, start)

up_button = Button(*leftbuttonparam, up)

down_button = Button(*rightbuttonparam, down)

sides_button = Button(*leftbuttonparam, sides)

back_button = Button(*rightbuttonparam, back)

downstairs_button = Button(*leftbuttonparam, down)

secret_button = Button(*rightbuttonparam, secret)

on_button = Button(*leftbuttonparam, on)

off_button = Button(*rightbuttonparam, off)

retry_button = Button(overlay_reference.get_width() // 5,overlay_reference.get_height() // 5,
                      screen.get_width()//1.57, screen.get_height() //1.4, retry)

playagain_button = Button(overlay_reference.get_width() // 5,overlay_reference.get_height() // 5,
                      screen.get_width()//1.57, screen.get_height() //1.88, playagain)

scene1 = Scene(lab, laboverlay)

scene2 = Scene(toxicbg, toxicoverlay)

scene3 = Scene(stairs, stairsoverlay)

scene4 = Scene(darkbg, darkoverlay)

gameover1 = gameoverScene(gameoverbg, explanation1,gameoveroverlay)

gameover2 = gameoverScene(gameoverbg, explanation2,gameoveroverlay)

gameover3 = gameoverScene(gameoverbg, explanation3,gameoveroverlay)

gamewon1 = gameoverScene(winbg,win1,escape)

gamewon2 = gameoverScene(winbg,win2, escape)

screen.blit(startImg,(0,0))

start_button.draw()

running = True

current_scene = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if exit_button.is_clicked(event.pos):
                running = False
            elif start_button.is_clicked(event.pos):
                    scene1.draw()
                    up_button.draw()
                    down_button.draw()
                    current_scene = scene1
            elif current_scene == scene1:
                if up_button.is_clicked(event.pos):
                    scene2.draw()
                    sides_button.draw()
                    back_button.draw()
                    current_scene = scene2
                elif down_button.is_clicked(event.pos):
                    gameover1.draw()
                    retry_button.draw()
                    current_scene = gameover1
            elif current_scene == scene2:
                if back_button.is_clicked(event.pos):
                    scene3.draw()
                    downstairs_button.draw()
                    secret_button.draw()
                    current_scene = scene3
                elif sides_button.is_clicked(event.pos):
                    gameover2.draw()
                    retry_button.draw()
                    current_scene = gameover2
            elif current_scene == scene3:
                if downstairs_button.is_clicked(event.pos):
                    scene4.draw()
                    on_button.draw()
                    off_button.draw()
                    current_scene = scene4
                elif secret_button.is_clicked(event.pos):
                    gamewon1.draw()
                    playagain_button.draw()
                    current_scene = gamewon1
            elif current_scene == scene4:
                if off_button.is_clicked(event.pos):
                    gameover3.draw()
                    retry_button.draw()
                    current_scene = gameover3
                elif on_button.is_clicked(event.pos):
                    gamewon2.draw()
                    playagain_button.draw()
                    current_scene = gamewon2
            elif current_scene == gameover1 or current_scene == gameover2 or current_scene == gameover3 or current_scene == gamewon1 or current_scene == gamewon2:
                if retry_button.is_clicked(event.pos) or playagain_button.is_clicked(event.pos):
                    scene1.draw()
                    up_button.draw()
                    down_button.draw()
                    current_scene = scene1

    exit_button.draw()
    pygame.display.flip()