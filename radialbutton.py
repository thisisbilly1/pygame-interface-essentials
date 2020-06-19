from utils import  drawbox


class radialbutton:
    def __init__(self, world, x, y, label="", defaultSelected=False):
        self.world = world
        self.x = x
        self.y = y
        
        self.selected=defaultSelected
        self.label=label
        
        
    def updateclicked(self,args=()):
        self.selected = not self.selected
        
    def draw(self):
        box=[self.x,self.y,15,15]
        
        self.world.screen.blit(self.world.fontobject.render(str(self.label), 1, (0,0,0)),(box[0], box[1]-15))
        
        if self.selected:
            drawbox(box,self.world,(0,200,0),(0,175,0),self.updateclicked)
        else:
            drawbox(box,self.world,(200,200,200),(175,175,175),self.updateclicked)