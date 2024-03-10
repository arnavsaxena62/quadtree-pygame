import pygame as pg
import random
pg.init()

class Point:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v



    def step(self):
        self.x += self.v[0]
        self.y += self.v[1]
        if self.x>screen.get_width() or self.x<0:
            self.v[0] = -self.v[0]
        if self.y>screen.get_height() or self.y <0:
            self.v[1] = -self.v[1]

    def draw(self, surface):
        pg.draw.circle(surface, (255,255,255), (self.x, self.y), 5)

screen = pg.display.set_mode((600, 800))
screen_buffer = pg.Surface(screen.get_size())
clock = pg.time.Clock()
running = True

vector_points = []

for i in range(10):
    current_point = Point(
        random.randint(0, screen.get_width()), 
        random.randint(0, screen.get_height()), 
        [random.randint(-10, 10)/10, 
         random.randint(-10, 10)/10]
        )
    vector_points.append(current_point)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    screen_buffer.fill((0, 0, 0))
    for current_point in vector_points:
        current_point.step()
        current_point.draw(screen_buffer)

    screen.blit(screen_buffer, (0, 0)) 
    pg.display.flip() 
    
    clock.tick(60) 

pg.quit()
