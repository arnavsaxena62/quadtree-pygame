import pygame as pg
import random

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
    

            

class rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pg.draw.rect(screen_buffer, (255, 255, 255), (self.x - self.w/2, self.y - self.h/2 , self.w, self.h), 2)



class Quadtree:
    MAX_CAPACITY = 1  
    
    def __init__(self, boundary, parent=None):
        self.boundary = boundary
        self.points = []
        self.subdivided = False
        self.ne = None
        self.se = None
        self.nw = None
        self.sw = None
        self.parent = parent

    def insert_point(self, point):
        if not self.boundary_contains_point(point):
            return False  
          
        if len(self.points) < self.MAX_CAPACITY and not self.subdivided:
            self.points.append(point)
            return True  
          
        if not self.subdivided:
            self.subdivide()

        if self.ne.insert_point(point):
            return True
        if self.se.insert_point(point):
            return True
        if self.nw.insert_point(point):
            return True
        if self.sw.insert_point(point):
            return True
          
        return False 

    def boundary_contains_point(self, point):
        return (self.boundary.x - self.boundary.w/2 <= point.x <= self.boundary.x + self.boundary.w/2 and
                self.boundary.y - self.boundary.h/2 <= point.y <= self.boundary.y + self.boundary.h/2)

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h
        
        rne = rectangle(x + w/4, y - h / 4, w / 2, h / 2)
        rse = rectangle(x + w / 4, y + h / 4, w / 2, h / 2)
        rnw = rectangle(x - w / 4, y - h / 4, w / 2, h / 2)
        rsw = rectangle(x - w / 4, y + h / 4, w / 2, h / 2)
        
        self.ne = Quadtree(rne, self)
        self.se = Quadtree(rse, self)
        self.nw = Quadtree(rnw, self)
        self.sw = Quadtree(rsw, self)
        
        self.subdivided = True

    def draw(self):
        self.boundary.draw()
        if self.subdivided:
            self.ne.draw()
            self.se.draw()
            self.nw.draw()
            self.sw.draw()

    




pg.init()
screen = pg.display.set_mode((600, 600))
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



boundary = rectangle(300, 300, 600, 600)
qtree = Quadtree(boundary, None)

screen_buffer.fill((0, 0, 0))
for current_point in vector_points:
    qtree.insert_point(current_point)
    current_point.draw(screen_buffer)
qtree.draw()




while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    


    screen.blit(screen_buffer, (0, 0)) 
    pg.display.flip() 
    
    clock.tick(60) 

pg.quit()
