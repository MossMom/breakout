import pygame #lib
pygame.init()

class Brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
    def draw(self):
        if self.alive:
            pygame.draw.rect(screen, (20, 122, 217), (self.xpos, self.ypos, 50, 20))
    def collide(self, x, y):
        if self.alive:
            if x+20>self.xpos and x<self.xpos+50 and y+20>self.ypos and y<self.ypos+20:
                self.alive = False
                return True

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("breakout")
clock = pygame.time.Clock()

#game variables
doExit = False
px = 300
py = 450

bx = 200
by = 200
bVx = 5
bVy = 5

#create brick copies
b1 = Brick(20, 20)
b2 = Brick(75, 20)
b3 = Brick(130, 20)
b4 = Brick(185, 20)
b5 = Brick(240, 20)
b6 = Brick(295, 20)
b7 = Brick(350, 20)
b8 = Brick(405, 20)
b9 = Brick(460, 20)
b10 = Brick(515, 20)
b11 = Brick(570, 20)
b12 = Brick(625, 20)

while not doExit: #start of game loop -----------------------------------
    
    #input/output section.................................
    clock.tick(60)
    
    #quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    
    #player movement        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        px -= 5
    if keys[pygame.K_RIGHT]:
        px += 5
    
    
    
    
    #physics section......................................
    #moves ball
    bx += bVx
    by += bVy
    
    #bouce ball off walls
    if bx < 0 or bx+20 > 700:
        bVx *= -1
    if by < 0 or by+20 > 500:
        bVy *= -1
        
    #bounce ball off paddle
    if by+20 > py and bx+20 > px and bx < px+100:
        bVy *= -1
    
    if b1.collide(bx, by):
        bVy *= -1
    if b2.collide(bx, by):
        bVy *= -1
    if b3.collide(bx, by):
        bVy *= -1
    if b4.collide(bx, by):
        bVy *= -1
    if b5.collide(bx, by):
        bVy *= -1
    if b6.collide(bx, by):
        bVy *= -1
    if b7.collide(bx, by):
        bVy *= -1
    if b8.collide(bx, by):
        bVy *= -1
    if b9.collide(bx, by):
        bVy *= -1
    if b10.collide(bx, by):
        bVy *= -1
    if b11.collide(bx, by):
        bVy *= -1
    if b12.collide(bx, by):
        bVy *= -1


    #render section.......................................
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255, 255, 255), (px, py, 100, 20))
    pygame.draw.rect(screen, (255, 255, 255), (bx, by, 20, 20))
    
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
    b11.draw()
    b12.draw()

    pygame.display.flip()
    
#end of game loop -------------------------------------------------------
pygame.quit()