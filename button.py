import pygame as pg

class Button:
    def __init__(self, Rot, x, y, width, height, color, text=""):
        self.Rot = Rot
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.colorbase = color
        self.colorhighlight = (color[0] + 50, color[1] + 50, color[2] + 50)
        self.text = text
        self.rect = pg.Rect(x, y, width, height)

    def update(self):
        pass
    
    def draw(self):
        pg.draw.rect(self.Rot.screen, self.color, self.rect)
        pg.draw.rect(self.Rot.screen, "white", self.rect, 3)
        if self.text != "":
            font = pg.font.SysFont("comicsans", 30)
            text = font.render(self.text, 1, (200, 200, 200))
            self.Rot.screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                                    self.y + (self.height/2 - text.get_height()/2)))

class Button2D(Button):
    def __init__(self, Rot, x, y, width, height, color, text=""):
        super().__init__(Rot, x, y, width, height, color, text)

    def update(self):
        mouse = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            self.color = self.colorhighlight
            if self.Rot.is_mouse_released:
                self.Rot.dimension = 2    
                self.Rot.vertex_count = 5
                self.Rot.setup()
                self.Rot.in_menu = False  
        else:
            self.color = self.colorbase

class Button3D(Button):
    def __init__(self, Rot, x, y, width, height, color, text=""):
        super().__init__(Rot, x, y, width, height, color, text)
    
    def update(self):
        mouse = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            self.color = self.colorhighlight
            if self.Rot.is_mouse_released:
                self.Rot.dimension = 3   
                self.Rot.setup()
                self.Rot.in_menu = False  
        else:
            self.color = self.colorbase
            
class ButtonBack(Button):
    def __init__(self, Rot, x, y, width, height, color, text=""):
        super().__init__(Rot, x, y, width, height, color, text)
    
    def update(self):
        mouse = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            self.color = self.colorhighlight
            if self.Rot.is_mouse_released:
                self.Rot.in_menu = True  
        else:
            self.color = self.colorbase

class Button3Dax(Button):
    def __init__(self, Rot, x, y, width, height, color, text="", ax="x"):
        super().__init__(Rot, x, y, width, height, color, text)
        self.ax = ax
        self.colorhighlight = (69, 191, 103)
    
    def update(self):
        mouse = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse) and self.Rot.is_mouse_released:
            if self.ax == "x":   
                self.Rot.axis3d[0] = 1 - self.Rot.axis3d[0]
            if self.ax == "y":
                self.Rot.axis3d[1] = 1 - self.Rot.axis3d[1]
            if self.ax == "z":
                self.Rot.axis3d[2] = 1 - self.Rot.axis3d[2]
        if self.ax == "x":
            if self.Rot.axis3d[0] == 1:
                self.color = self.colorhighlight
            else:
                self.color = self.colorbase
        if self.ax == "y":
            if self.Rot.axis3d[1] == 1:
                self.color = self.colorhighlight
            else:
                self.color = self.colorbase
        if self.ax == "z":
            if self.Rot.axis3d[2] == 1:
                self.color = self.colorhighlight
            else:
                self.color = self.colorbase
