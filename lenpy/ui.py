
# Un modulo que te permitira trabajar con elementos en la pantalla.

# Aún sigue en desarrollo por lo que puede estar incompleto.

import pygame, sys
from lenpy.text import Text 

class TextButton():
    
    def __init__(self, text:str, font:str, size:int, normal_color:str, select_color:str, hover_color:str, action=None, font_dir=None, italic=False, bold=False, underline=False, sysfont=False):

        # Si muchas variables
        self.x = int
        self.y = int
        self.font = font
        self.font_dir = font_dir
        self.size = size
        self.normal_color = normal_color
        self.select_color = select_color
        self.hover_color = hover_color
        self.action = []
        self.get_action = action
        self.italic = italic
        self.bold = bold
        self.underline = underline
        self.sysfont = sysfont
        self.clicked = False
        self.color = [self.normal_color, self.select_color, self.hover_color]
        self.color_number = 0
        self.get_text = text

        self.text = Text(self.get_text, self.font, self.size, font_dir=self.font_dir, color=pygame.Color(self.color[self.color_number]), italic=self.italic, bold=self.bold, underline=self.underline, sysfont=self.sysfont)
        self.return_action = False

    def draw(self, surface, x, y):

        self.rect = self.text.get_text_rect()
        self.rect.topleft = (x, y)

        pos = pygame.mouse.get_pos()

        # El boton colisiona con el mouse?
        if self.rect.collidepoint(pos):

            # Cambia al color hover
            self.color_number = 2
            self.text = Text(self.get_text, self.font, self.size, font_dir=self.font_dir, color=pygame.Color(self.color[self.color_number]), italic=self.italic, bold=self.bold, underline=self.underline, sysfont=self.sysfont)

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                
                self.clicked = True
                
                if self.get_action == True:

                    # Si el parametro action es True, Len'Py devolvera True al presionar el boton lo que te permitira crear tus propias acciones.

                    if self.clicked == True:

                        self.return_action = True

                    # print("Click")

                else:
                    
                    self.action = UIaction(self.get_action)

            if pygame.mouse.get_pressed()[0] == 1:

                # Cambia al color select
                self.color_number = 1
                self.text = Text(self.get_text, self.font, self.size, font_dir=self.font_dir, color=pygame.Color(self.color[self.color_number]), italic=self.italic, bold=self.bold, underline=self.underline, sysfont=self.sysfont)

        else:
            
            # Regresa al color normal
            self.color_number = 0
            self.text = Text(self.get_text, self.font, self.size, font_dir=self.font_dir, color=pygame.Color(self.color[self.color_number]), italic=self.italic, bold=self.bold, underline=self.underline, sysfont=self.sysfont)

        # No se esta presionando el boton?
        if pygame.mouse.get_pressed()[0] == 0:

            self.return_action = False
            
            self.clicked = False
        
        # Dibuja el botón
        self.text.draw(surface, x, y)

        if self.return_action:

            # Retorna True
            return self.return_action

# Dibuja un boton pero con imagenes

class ImageButton():
    
    def __init__(self, normal_img, hover_img, select_img, action, scale=1.0, disable_img=""):

        normal_image = pygame.image.load(normal_img).convert_alpha()
        hover_image = pygame.image.load(hover_img).convert_alpha()
        select_image = pygame.image.load(select_img).convert_alpha()

        n_width = normal_image.get_width()
        n_height = normal_image.get_height()

        h_width = hover_image.get_width()
        h_height = hover_image.get_height()

        s_width = select_image.get_width()
        s_height = select_image.get_height()

        self.normal_image = pygame.transform.scale(normal_image, (n_width * scale, n_height * scale))
        self.hover_image = pygame.transform.scale(hover_image, (h_width * scale, h_height * scale))
        self.select_image = pygame.transform.scale(select_image, (s_width * scale, s_height * scale))

        self.disable = False

        if not disable_img == "":
        
            disable_image = pygame.image.load(disable_img).convert_alpha()

        else:

            disable_image = pygame.image.load(normal_img).convert_alpha()

        d_width = disable_image.get_width()
        d_height = disable_image.get_height()
            
        self.disable_image = pygame.transform.scale(disable_image, (d_width * scale, d_height * scale))

        self.get_action = action
        self.return_action = False
        self.action = []
        self.clicked = False

        self.image = self.normal_image
        
    def draw(self, surface, x, y):
        
        self.rect = self.normal_image.get_rect()
        self.rect.topleft = (x, y)

        pos = pygame.mouse.get_pos()

        if not self.disable:

            if self.rect.collidepoint(pos):

                self.image = self.hover_image

                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    
                    self.clicked = True

                    if self.get_action == True:

                        # Si el parametro action es True, Len'Py devolvera True al presionar el boton lo que te permitira crear tus propias acciones.

                        if self.clicked == True:

                            self.return_action = True

                        # print("Click")

                    else:

                        self.action = UIaction(self.get_action)

                if pygame.mouse.get_pressed()[0] == 1:

                    self.image = self.select_image

            else:

                self.image = self.normal_image


            if pygame.mouse.get_pressed()[0] == 0:

                self.return_action = False
                
                self.clicked = False

        elif self.disable:

            self.image = self.disable_image

        surface.blit(self.image, [x, y])

        if self.return_action == True:

            return self.return_action

# Aun sigo trabajando en está caracteristica, ¿Que más se puede agregar?

class UIaction():

    def __init__(self, action):

        self.action = action

        if self.action == "quit":
            self.Quit()

    def Quit(self):

        pygame.quit()
        sys.exit()