import pygame
import numpy as np
from utils import checkmousebox, clamp
'''
the slider goes form 0 to 100
the multiplier is the multiplier for the display value
onlyints is what it says it is

roundnumber is the number to round to. So if roundNumber=3, then only multiples of 3 will show
odd = only odd numbers will appear

'''
class slider:
    def __init__(self, world, x, y, label, multiplier=1, startSlide=0, onlyints=False, roundNumber=0, odd=False):
        self.world=world
        self.x=x
        self.y=y
        self.label=label
        self.multiplier=multiplier
        
        self.slide=startSlide
        self.slideValue=5
        self.previous_slie=-1
        self.onlyints=onlyints
        self.roundNumber=roundNumber
        self.odd=odd
        
        self.sliderw=100
        self.sliderh=10
        
        self.slidew=self.sliderw/10
        self.slideh=self.sliderh*2
        
        self.clicked=False
        
        #get inititial slider value
        self.getSliderValue()
        
    
    def getSliderValue(self):
        self.slideValue=self.slide*self.multiplier
        if self.onlyints:
            self.slideValue = int(self.slideValue)
        if self.roundNumber!=0:
            self.slideValue = int(round(self.slideValue/self.roundNumber)*self.roundNumber)
        
        if self.odd:
            if self.slideValue%2!=1:
                self.slideValue+=1
        
    def draw(self):
        self.previous_slie=self.slide
        xx=0#self.controller.xx
        yy=0#self.controller.yy
        
        pygame.draw.rect(self.world.screen, (220,220,220),(self.x-10,self.y-25,130,50), 0)
        
        box=[self.x+xx,self.y+yy,self.sliderw,self.sliderh]
        
        pygame.draw.rect(self.world.screen, (200,200,200),(box[0]+1, box[1]+1, box[2]-1, box[3]-1), 0)
        pygame.draw.rect(self.world.screen, (0,0,0),(box[0], box[1], box[2], box[3]), 1)
        
        sliderbox=[self.x+xx+self.slide-self.slidew/4,self.y+yy-self.slideh/4,self.sliderw/10,self.sliderh*2]
        slidercolor=(200,200,200)
        if checkmousebox(sliderbox,[self.world.mouse_x,self.world.mouse_y]):
            slidercolor=(175,175,175)
            if self.world.mouse_left:
                self.clicked=True
                
        if not self.world.mouse_left:
            self.clicked=False
        if self.clicked:
            slidercolor=(150,150,150)
            self.slide=clamp(self.world.mouse_x-(self.x+xx),0,100)
            self.getSliderValue()
            
        pygame.draw.rect(self.world.screen, slidercolor,(sliderbox[0]+1, sliderbox[1]+1, sliderbox[2]-1, sliderbox[3]-1), 0)
        pygame.draw.rect(self.world.screen, (0,0,0),(sliderbox[0], sliderbox[1], sliderbox[2], sliderbox[3]), 1)
        
        self.world.screen.blit(self.world.fontobject.render(self.label+": "+str(self.slideValue), 1, (0,0,0)),(self.x+xx, self.y+yy-20))
        
        