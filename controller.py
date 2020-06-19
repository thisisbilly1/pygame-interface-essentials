import numpy as np
import cv2
import pygame

from utils import clamp, cvimage_to_pygame, returnCameraIndexes
from dropdown import dropdown
from radialbutton import radialbutton
from slider import slider

from camera import camera


class controller:
    def __init__(self,world):
        self.world=world
        
        cameralist=returnCameraIndexes()
        self.cameradropdown=dropdown(self.world,50,50, cameralist, label="Cameras")
        self.previouscamera=cameralist[0]
        
        self.rotateiondropdown=dropdown(self.world,182,50, [0,90,180,270],label="Rotation")
        
        self.flipx=radialbutton(self.world, 314 ,50, label="Flip X")
        self.flipy=radialbutton(self.world, 354 ,50, label="Flip Y")
        
        self.edge=radialbutton(self.world, 394 ,50, label="Edge")
        
        self.cannySliderMax=slider(self.world,394,100,"maxVal",multiplier=2.5,startSlide=40)
        self.cannySliderMin=slider(self.world,394,175,"minVal",multiplier=2.5,startSlide=20)
        
        self.camera=camera().start()
        
        #for dragging the image
        self.xx=0
        self.yy=0
        self.mouse_clicked=(0,0)
        self.zoom=100
        self.previous_zoom=0
        
    def stop(self):
        self.camera.stop()
        
    def update(self):
        #dragging around
        if self.world.mouse_right_down or self.world.mouse_right_up:
            self.mouse_clicked=(self.world.mouse_x,self.world.mouse_y)
        if self.world.mouse_right:
            self.xx+=self.world.mouse_x-self.mouse_clicked[0]
            self.yy+=self.world.mouse_y-self.mouse_clicked[1]
            self.mouse_clicked=(self.world.mouse_x,self.world.mouse_y)
            
        if self.world.mouse_scroll_up:
            self.zoom=clamp(self.zoom+5,1,500)
        if self.world.mouse_scroll_down:
            self.zoom=clamp(self.zoom-5,1,500)
            

        if self.previouscamera!=self.cameradropdown.selected:
            self.camera.updateCap(self.cameradropdown.selected)
        
        self.previouscamera=self.cameradropdown.selected
            
       
            
    def draw(self):
        img=self.camera.getImg()
        
        #rotate the image
        img=np.rot90(img,self.rotateiondropdown.selected)
        if self.flipx.selected:
            img=np.flip(img,1)
        if self.flipy.selected:
            img=np.flip(img,0)
            
        #edges
        if self.edge.selected:
            self.cannySliderMax.draw()
            self.cannySliderMin.draw()
            
            img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            img=cv2.Canny(img,self.cannySliderMin.slide*self.cannySliderMin.multiplier,self.cannySliderMax.slide*self.cannySliderMax.multiplier)
            img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        self.world.screen.blit(cvimage_to_pygame(img),(200,300))
        
        self.rotateiondropdown.draw()
        self.cameradropdown.draw()
        self.flipx.draw()
        self.flipy.draw()
        self.edge.draw()
        