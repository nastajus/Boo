#a big thing orbitted by many small things
#thing moves around, has babies, they may gravitate, they more likely get assigned a random orbit, 

#to do list: 
# refactor starting position of head & bullet, somehow.

import pygame 
from pygame.locals import *
import math
import random
import sys

fpsClock = pygame.time.Clock()

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480


class Bullet:
    def __init__(self, bill_barrel, boo):
        self.bullet_original = pygame.image.load("bullet_bill.png")
        self.bullet = pygame.image.load("bullet_bill.png")
        
        self.size = self.bullet.get_size()
        #self.position = [ SCREEN_WIDTH//2, SCREEN_HEIGHT - self.size[1] ]
        
        self.position = bill_barrel.position
        self.target = boo.position


        self.direction = bill_barrel.angle
    
    
    def update( self ):
        global timeDelta
        
        magnitude = 50.5
        
        #trajectory
        x = (magnitude * math.sin(math.radians(self.direction))) * (timeDelta / 1000.0)
        y = (magnitude * math.cos(math.radians(self.direction))) * (timeDelta / 1000.0)        
        
        if self.direction == 0:
            y = 0 
            x = magnitude
        
        if self.direction == 90:
            y = magnitude
            x = 0
            
        self.position = [ self.position[0] - x, self.position[1] - y ]


        






        
    

    def draw(self, target_surface):
        target_surface.blit( self.bullet, self.position )
        #print "drawing at " + str( self.position )
    
        blue = 0, 0, 255
        point1 = self.position
        point2 = self.target
        screen = target_surface
        width = 5
        pygame.draw.line(screen, blue, point1, point2, width)


class BillBarrel:
    def __init__(self):
        self.bill_barrel_image_original = pygame.image.load("bullet_bill_launcher_barrel.png")
        self.bill_barrel_image = pygame.image.load("bullet_bill_launcher_barrel.png")
    
        self.size = self.bill_barrel_image.get_size()
        self.height = self.size[1]
        self.width = self.size[0]
        self.position = [ SCREEN_WIDTH//2, SCREEN_HEIGHT - self.height ]
        self.angle = 0
        
        #self.pivotx 
        #self.pivoty 
        
    def update( self, bill_base, boo  ):
        #get top left posi of BillBase, draw it with it's magic number offset


        angle = math.atan2(bill_base.position[0] - boo.position[0], bill_base.position[1] - boo.position[1])
        print str(bill_base.position[0]) + "," + str(bill_base.position[1]) + "..." + str(boo.position[0]) +","+ str(boo.position[0])
                
        angle = math.degrees(angle)
        
        self.angle = angle
        
        #print self.angle
        


        self.bill_barrel_image = pygame.transform.rotate(self.bill_barrel_image_original, angle - 90)

        self.position = [ bill_base.position[0] + bill_base.point_of_rotation[0]  - self.width//2, bill_base.position[1] +  bill_base.point_of_rotation[1] - self.height//2 ]
        
        

        
    def draw( self, target_surface ):
        target_surface.blit( self.bill_barrel_image, self.position )
        
        


class BillBase:
    def __init__(self):
        self.bill_base_image = pygame.image.load("bullet_bill_launcher_base.png")
        self.size = self.bill_base_image.get_size()
        self.height = self.size[1]
        self.width = self.size[0]
        self.position = [ SCREEN_WIDTH//2, SCREEN_HEIGHT - self.height ]
        self.inverted = False
        #self.rotation_needed = False 
        self.point_of_rotation = [ 24, 3 ]   #magic number offset
        #Alex's stuff, delete this intrusion later!
        self.angle = 0.0

    #note: not really vectors
    def update(self, vector_x, vector_y):
    
    
    
        #receives current mouse position, snaps to top or bottom following mouse, whichever is closer
        if vector_y > SCREEN_HEIGHT // 2: 
            self.posy = SCREEN_HEIGHT - self.height
            self.inverted = False
        else:
            self.posy = 0 
            self.inverted = True
            
        if vector_x + self.width > SCREEN_WIDTH:
            self.posx = SCREEN_WIDTH - self.width - self.width//2
        elif vector_x - self.width//2 < self.width//2:
            self.posx = self.width//2
        else:
            self.posx = vector_x - self.width//2
            
        self.position = [ self.posx , self.posy  ]
    
        self.angle = math.atan2( self.posx, self.posy )
    #print self.angle
    
        
    def draw(self, target_surface):

        #if self.inverted == True:
            #self.bill_base_image = pygame.transform.rotate(self.bill_base_image, 180)
        
        target_surface.blit( self.bill_base_image, self.position )
        





#controls the big circle
class Boo:
    def __init__( self ):  #diam
        self.DELTA = 5
        #self.diam = diam
        self.position = [300,200]
        
        #pygame.draw.circle(Surface, color, pos, radius, width=0)
        self.boo_image = pygame.image.load("boo_big.png")
        self.size = self.boo_image.get_size()
        
        # Create the surface of (width, height), and its window.
        #self.boo_surface = pygame.display.set_mode( [320*3, 240*3])
        
        
        
    
    #top level methods
    def update(self, vector_x, vector_y  ): 
        self.position = [self.position[0] + vector_x * self.DELTA, self.position[1] + vector_y * self.DELTA]
        
        
    def draw(self, target_surface):
        target_surface.blit( self.boo_image, self.position )
        #print self.position 
        


class Orbit:
    def __init__(self):
    #loaded_boos_array
        pass


class Baby:
    def __init__(self, boo):
    
        self.baby_image = pygame.image.load("pics/Untitled" + str( random.randint(1,5) ) + ".png")
        self.size = self.baby_image.get_size()
        self.height = self.size[1]
        self.width = self.size[0]
        
        #x = 100 + random.randint(-100,100)
        #y = 100 + random.randint(-100,100)
        #print x, y
        #self.position = [x,y]
        
        x = boo.position[0] + random.randint(-100,100)
        y = boo.position[1] + random.randint(-100,100)
        #print x, y 
        self.position = [x,y]
    
        
        #self.position = [ 100 + random.randint(-100,100), 100 + random.randint(-100,100) ]
        
        #self.x = boo.position[0] 
        #self.y = boo.position[1]  
        #self.position = [ self.x , self.y ]
        #self.position = [100,100]  
    
    
    def draw(self, target_surface):
        target_surface.blit( self.baby_image, self.position )
    
        
        
keysDown = [False for x in range(0, 511)]
        
timeDelta = 0.0
prevTime = 0.0
curTime = pygame.time.get_ticks()                

class WorldThing: 
    
    def __init__(self):
    
        pygame.init()
        self.world_surface = pygame.display.set_mode( [SCREEN_WIDTH, SCREEN_HEIGHT] )
    
    
        self.boo = Boo()
        self.bill_base = BillBase()
        self.bill_barrel = BillBarrel()
        
        

        self.babies = []
        #redesign array to plot on a circle with equal distance with minor variations
        self.babies.append( Baby( self.boo ))
        self.babies.append( Baby( self.boo ))
        self.babies.append( Baby( self.boo ))
        self.babies.append( Baby( self.boo ))
        self.babies.append( Baby( self.boo ))
        
        #self.babies = [Baby() for count in xrange(1)]
        #self.baby1 = Baby()


        self.bullet_exists = False
    
        self.bullets = []

    
    def run(self):

    
        #main game loop
        while True:
            
            global prevTime
            global curTime
            global timeDelta
            prevTime = curTime
            curTime = pygame.time.get_ticks()
            timeDelta = curTime - prevTime
            
            #print timeDelta
            
            #print fpsClock.get_fps()
            # events   &   updates   intermingled
            self.ev = pygame.event.poll()


            self.world_surface.fill( (127,63,247) )


            
            if self.ev.type == pygame.QUIT:
                break;
            
            if self.ev.type == pygame.KEYDOWN:
                
                self.key = self.ev.dict["key"]
                keysDown[self.key] = True
                if self.key == 27:                 # On Escape key ...
                    break                          #   leave the game loop.
                
            if self.ev.type == pygame.KEYUP:
                self.key = self.ev.dict["key"]
                keysDown[self.key] = False
                
            
            if(keysDown[K_a]):
                self.boo.update( -1.0,0.0 ) 
                self.bill_barrel.update( self.bill_base, self.boo )
            elif(keysDown[K_d]):
                self.boo.update( 1.0,0.0 )
                self.bill_barrel.update( self.bill_base, self.boo )
            if(keysDown[K_w]):
                self.boo.update( 0.0,-1.0 )
                self.bill_barrel.update( self.bill_base, self.boo )
            elif(keysDown[K_s]):
                self.boo.update( 0.0,1.0 )
                self.bill_barrel.update( self.bill_base, self.boo )
                
                
                
            if self.ev.type == pygame.MOUSEMOTION:
                mousex, mousey = self.ev.pos
                self.bill_base.update( mousex, mousey )

                self.bill_barrel.update( self.bill_base, self.boo ) 
        
                
            if self.ev.type == pygame.MOUSEBUTTONDOWN:
                
                if pygame.mouse.get_pressed()[0] == 1:
                    #print "LEFT MOUSE PRESSED  " + str(self.bill_barrel.angle)
                    
                    #first draw
                    
                    self.bullets.append (  Bullet( self.bill_barrel, self.boo ) )

                    self.bullet_exists = True
                    #for bullet in self.bullets:
                    #    print bullets.get_size()
                    #    self.bullet.update( )


            if self.bullet_exists == True:
                for bullet in self.bullets:
                    bullet.update(  )
                    bullet.draw( self.world_surface )

            
            # draws.
            self.boo.draw( self.world_surface ) 
            self.bill_base.draw ( self.world_surface )
            self.bill_barrel.draw ( self.world_surface )

            
            for baby in self.babies:
                baby.draw(self.world_surface)
                #self.baby1.draw( self.world_surface )





            
            fpsClock.tick(60)
            pygame.display.flip() #update the entire screen


            
        pygame.quit()
        sys.exit()
        # returns to IDLE Python Shell. 
            

if __name__ == "__main__":
    world = WorldThing()
    world.run()
