
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
    
    def __init__(self, normal_img, hover_img, select_img, action, disable_img="", text_parameters=["", "arial", 10, "#000000", False, [0, 0], None]):

        """
        Una clase para un ImageButton

        Cada parametro es obligatorio a excepción de las imagenes "disable"

        :normal_img: Imagen por defecto
        :hover_img: Es la imagen que se usa al pasar el cursor por encima
        :select_img: Es la imagen que se usa si el usuario da un clic
        :action: Las acciones que puede hacer el boton, usando la clase UIaction o puede colocar True para crear sus propias acciones.

        :disable_img: Si se especifica se usara la imagen colocada cuando el boton este desactivado
        
        """

        self.antialising = False
        self.scale = 1.0

        self.n_img = pygame.image.load(normal_img).convert_alpha()
        self.h_img = pygame.image.load(hover_img).convert_alpha()
        self.s_img = pygame.image.load(select_img).convert_alpha()

        # Obtiene los alto y ancho de cada botón
        self.n_width = self.n_img.get_width()
        self.n_height = self.n_img.get_height()

        self.h_width = self.h_img.get_width()
        self.h_height = self.h_img.get_height()

        self.s_width = self.s_img.get_width()
        self.s_height = self.s_img.get_height()

        #######################################

        self.normal_image = pygame.transform.scale(self.n_img, (self.n_width * self.scale, self.n_height * self.scale))
        self.hover_image = pygame.transform.scale(self.h_img, (self.h_width * self.scale, self.h_height * self.scale))
        self.select_image = pygame.transform.scale(self.s_img, (self.s_width * self.scale, self.s_height * self.scale))

        #####################

        # Si el botón está deshabilitado, entonces...

        self.disable = False

        if not disable_img == "":
        
            self.d_img = pygame.image.load(disable_img).convert_alpha()

        else:

            self.d_img = pygame.image.load(normal_img).convert_alpha()

        self.d_width = self.d_img.get_width()
        self.d_height = self.d_img.get_height()
            
        self.disable_image = pygame.transform.scale(self.d_img, (self.d_width * self.scale, self.d_height * self.scale))

        #############

        self.get_action = action
        self.return_action = False
        self.action = []
        self.clicked = False

        self.image = self.normal_image

        self.font = pygame.font.SysFont(text_parameters[1], text_parameters[2])
        self.text = text_parameters[0]
        self.text_color = text_parameters[3]
        self.text_visible = text_parameters[4]
        self.text_pos_value = text_parameters[5]

        if len(text_parameters) >= 7 and not text_parameters[6] == None:

            self.font_dir = text_parameters[6]
            self.font = pygame.font.Font(f"{self.font_dir}/{text_parameters[1]}", text_parameters[2])

        self.text_img = None
        
    def draw(self, surface, x, y, scale=1.0, antialising=True):

        """
        Los tres parametros principales son obvios, y claro que son obligatorios

        :scale: Por defecto la escala del boton será la misma que la de su imagen pero puedes cambiarlo subiendo o bajando la escala,
                está requiere numeros en coma flotante(0.0) no enteros.

        :antialising: Por defecto Len'Py usa la función "pygame.transform.smoothscale()" para escalar los objetos, pero el problema
                      es que aumenta un poco el consumo de recursos, así que puedes colocar False para mejorar el rendimiento, pero
                      la imagen se verá un poco pixelada.
        """

        self.antialising = antialising
        self.scale = scale

        if self.antialising:

            self.normal_image = pygame.transform.smoothscale(self.n_img, (self.n_width * self.scale, self.n_height * self.scale))
            self.hover_image = pygame.transform.smoothscale(self.h_img, (self.h_width * self.scale, self.h_height * self.scale))
            self.select_image = pygame.transform.smoothscale(self.s_img, (self.s_width * self.scale, self.s_height * self.scale))
            self.disable_image = pygame.transform.smoothscale(self.d_img, (self.d_width * self.scale, self.d_height * self.scale))

        else:

            self.normal_image = pygame.transform.scale(self.normal_image, (self.n_width * self.scale, self.n_height * self.scale))
            self.hover_image = pygame.transform.scale(self.hover_image, (self.h_width * self.scale, self.h_height * self.scale))
            self.select_image = pygame.transform.scale(self.select_image, (self.s_width * self.scale, self.s_height * self.scale))
            self.disable_image = pygame.transform.scale(self.d_img, (self.d_width * self.scale, self.d_height * self.scale))

        self.rect = self.normal_image.get_rect()
        self.rect.topleft = (x, y)

        self.text_img = self.font.render(self.text, True, self.text_color)

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

        if self.text_visible:

            surface.blit(self.text_img, [x + self.text_pos_value[0], y + self.text_pos_value[1]])

        if self.return_action == True:

            return self.return_action

class CheckButton():

    """
    Una clase para un check_button

    Cada parametro es obligatorio a excepción de las imagenes "disable"

    :normal_img: Imagen por defecto
    :hover_img: Es la imagen que se usa al pasar el cursor por encima
    :select_img: Es la imagen que se usa si el usuario da un clic

    :check_img: Está imagen es la que se usa cuando el check está activo.
    :check_hover_img: Está es la imagen que se usa al pasar el cursor por encima cuando el check está activo.
    :check_select_img: Es la imagen que se usa si el usuario da un clic cuando el check está activo.

    :disable_img: Si se especifica se usara la imagen colocada cuando el check este desactivado
    :disable_check_img: Si se especifica se usara la imagen colocada cuando el check este desactivado si previamente estaba activo.

    El check, no permite acciones, por lo que deberas crear lo que el hace cuando está activo.
    """
    
    def __init__(self, normal_img, hover_img, select_img, check_img, check_hover_img, check_select_img, disable_img="", disable_check_img=""):
        
        self.scale = 1.0

        self.n_img = pygame.image.load(normal_img).convert_alpha()
        self.h_img = pygame.image.load(hover_img).convert_alpha()
        self.s_img = pygame.image.load(select_img).convert_alpha()

        self.c_img = pygame.image.load(check_img).convert_alpha()
        self.ch_img = pygame.image.load(check_hover_img).convert_alpha()
        self.cs_img = pygame.image.load(check_select_img).convert_alpha()

        # Obtiene el ancho y alto de las imagenes

        self.n_width = self.n_img.get_width()
        self.n_height = self.n_img.get_height()

        self.h_width = self.h_img.get_width()
        self.h_height = self.h_img.get_height()

        self.s_width = self.s_img.get_width()
        self.s_height = self.s_img.get_height()

        # Check alto y ancho

        self.c_width = self.c_img.get_width()
        self.c_height = self.c_img.get_height()

        self.ch_width = self.ch_img.get_width()
        self.ch_height = self.ch_img.get_height()

        self.cs_width = self.cs_img.get_width()
        self.cs_height = self.cs_img.get_height()

        #######################################

        self.normal_image = pygame.transform.scale(self.n_img, (self.n_width * self.scale, self.n_height * self.scale))
        self.hover_image = pygame.transform.scale(self.h_img, (self.h_width * self.scale, self.h_height * self.scale))
        self.select_image = pygame.transform.scale(self.s_img, (self.s_width * self.scale, self.s_height * self.scale))
        
        self.check_image = pygame.transform.scale(self.c_img, (self.c_width * self.scale, self.c_height * self.scale))
        self.check_hover_image = pygame.transform.scale(self.ch_img, (self.ch_width * self.scale, self.ch_height * self.scale))
        self.check_select_image = pygame.transform.scale(self.cs_img, (self.cs_width * self.scale, self.cs_height * self.scale))

        #####################

        # Si el botón está deshabilitado, entonces...

        self.disable = False

        if not disable_img == "":
        
            self.d_img = pygame.image.load(disable_img).convert_alpha()

        else:

            self.d_img = pygame.image.load(normal_img).convert_alpha()


        if not disable_check_img == "":
        
            self.dc_img = pygame.image.load(disable_check_img).convert_alpha()

        else:

            self.dc_img = pygame.image.load(check_img).convert_alpha()

        self.d_width = self.d_img.get_width()
        self.d_height = self.d_img.get_height()

        self.dc_width = self.dc_img.get_width()
        self.dc_height = self.dc_img.get_height()
            
        self.disable_image = pygame.transform.scale(self.dc_img, (self.dc_width * self.scale, self.dc_height * self.scale))
        self.disable_check_image = pygame.transform.scale(self.dc_img, (self.dc_width * self.scale, self.dc_height * self.scale))

        #######################################

        self.get_action = True
        self.return_action = False
        self.clicked = False
        self.check = False

        self.image = self.normal_image

    def draw(self, surface, x, y, scale=1.0, antialising=True):
        """
        Los tres parametros principales son obvios, y claro que son obligatorios

        :scale: Por defecto la escala del boton será la misma que la de su imagen pero puedes cambiarlo subiendo o bajando la escala,
                está requiere numeros en coma flotante(0.0) no enteros.

        :antialising: Por defecto Len'Py usa la función "pygame.transform.smoothscale()" para escalar los objetos, pero el problema
                      es que aumenta un poco el consumo de recursos, así que puedes colocar False para mejorar el rendimiento, pero
                      la imagen se verá un poco pixelada.
        """

        self.antialising = antialising
        self.scale = scale

        if self.antialising:

            self.normal_image = pygame.transform.smoothscale(self.n_img, (self.n_width * self.scale, self.n_height * self.scale))
            self.hover_image = pygame.transform.smoothscale(self.h_img, (self.h_width * self.scale, self.h_height * self.scale))
            self.select_image = pygame.transform.smoothscale(self.s_img, (self.s_width * self.scale, self.s_height * self.scale))
            self.disable_image = pygame.transform.smoothscale(self.d_img, (self.d_width * self.scale, self.d_height * self.scale))

            self.check_normal_image = pygame.transform.smoothscale(self.c_img, (self.c_width * self.scale, self.c_height * self.scale))
            self.check_hover_image = pygame.transform.smoothscale(self.ch_img, (self.ch_width * self.scale, self.ch_height * self.scale))
            self.check_select_image = pygame.transform.smoothscale(self.cs_img, (self.cs_width * self.scale, self.cs_height * self.scale))
            self.disable_check_image = pygame.transform.smoothscale(self.dc_img, (self.dc_width * self.scale, self.dc_height * self.scale))

        else:

            self.normal_image = pygame.transform.scale(self.normal_image, (self.n_width * self.scale, self.n_height * self.scale))
            self.hover_image = pygame.transform.scale(self.hover_image, (self.h_width * self.scale, self.h_height * self.scale))
            self.select_image = pygame.transform.scale(self.select_image, (self.s_width * self.scale, self.s_height * self.scale))
            self.disable_image = pygame.transform.scale(self.d_img, (self.d_width * self.scale, self.d_height * self.scale))

            self.check_normal_image = pygame.transform.scale(self.c_img, (self.c_width * self.scale, self.c_height * self.scale))
            self.check_hover_image = pygame.transform.scale(self.ch_img, (self.ch_width * self.scale, self.ch_height * self.scale))
            self.check_select_image = pygame.transform.scale(self.cs_img, (self.cs_width * self.scale, self.cs_height * self.scale))
            self.disable_check_image = pygame.transform.scale(self.dc_img, (self.dc_width * self.scale, self.dc_height * self.scale))

        self.rect = self.normal_image.get_rect()
        self.rect.topleft = (x, y)

        pos = pygame.mouse.get_pos()

        if not self.disable:

            if self.rect.collidepoint(pos):

                if not self.check:

                    self.image = self.hover_image

                elif self.check:

                    self.image = self.check_hover_image

                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and not self.check:
                    
                    self.clicked = True
                    self.check = True

                    # print("Click")

                elif pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.check: 

                    self.clicked = True
                    self.check = False

                if pygame.mouse.get_pressed()[0] == 1:

                    if not self.check:

                        self.image = self.select_image

                    elif self.check:

                        self.image = self.check_select_image

            else:

                if not self.check:

                    self.image = self.normal_image

                elif self.check:

                    self.image = self.check_normal_image

            if pygame.mouse.get_pressed()[0] == 0:

                self.clicked = False

        elif self.disable:

            if not self.check:

                self.image = self.disable_image

            elif self.check:

                self.image = self.disable_check_image


        surface.blit(self.image, [x, y])

        return self.check

# Aun sigo trabajando en está caracteristica, ¿Que más se puede agregar?

class UIaction():

    """
    La clase UIaction en futuras versiones de Len'Py se espera que sea más completa, para realizar acciones en la ¿UI?

    """

    def __init__(self, action):
        """
        :action: El unico parametro puede realizar las acciones de aqui abajo:

                :play: : reproducira la música dada, el nombre de la música no puede contener un espacio seguido del comando "play:"
                ejemplo:
                    Si. "play:Think" 
                    No. "play: Think"

                Solo hay que colocar el nombre de la música el formato será colocado por la función play_music, el formato debe de 
                ser .ogg para que no haiga problemas.
        """
        self.action = action

        if self.action == "quit":
            self.Quit()

        elif "play:" in self.action:

            music = self.action.strip("play:")
            self.play_music(music)

        elif self.action == "stop_music":

            self.stop_music()

        elif "play_sound:" in self.action:

            sound = self.action.strip("play_sound:")
            self.play_sound(sound)

        elif self.action == "stop_sound":

            self.stop_sound()

    def play_music(self, file):

        music = pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)

    def stop_music(self):

        pygame.mixer.music.stop()

    def play_sound(self, file):

        sound_channel = pygame.mixer.Channel(2)
        sound = pygame.mixer.Sound(file)

        sound_channel.play(sound)

    def stop_sound(self):

        sound_channel = pygame.mixer.Channel(2)
        sound_channel.stop()

    def get_busy_sound(self):

        sound_channel = pygame.mixer.Channel(2)

        return sound_channel.get_busy()

    def Quit(self):

        pygame.quit()
        sys.exit()

class Screen_Notify():
   
    def __init__(self, surface, x, y, color, font, font_color, size, notify_box=None, font_dir=None):
        
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.font = font
        self.font_color = font_color
        self.size = size
        self.message = ""
        self.screen_notify_show = False
        self.notify_box = notify_box
        self.font_dir = font_dir

        if not self.font_dir == None and "." in self.font:

            self.text = Text(self.message, self.font, self.size, font_dir=self.font_dir, color=pygame.Color(self.font_color), sysfont=False)

        else:

            self.text = Text(self.message, self.font, self.size, color=pygame.Color(self.font_color), sysfont=True)

    def notify(self, message, visible):

        self.message = message

        if not self.font_dir == None and "." in self.font:

            self.text = Text(self.message, self.font, self.size, font_dir=self.font_dir, color=pygame.Color(self.font_color), sysfont=False)

        else:

            self.text = Text(self.message, self.font, self.size, color=pygame.Color(self.font_color), sysfont=True)

        self.screen_notify_show = visible

        text_width = self.text.get_text_rect()[2]
        text_height = self.text.get_text_rect()[3]

        if self.screen_notify_show:

            if self.notify_box == None:

                pygame.draw.rect(self.surface, self.color, [self.x, self.y, text_width * 1.1, text_height * 1.4])

            else:

                notify_box = pygame.image.load(self.notify_box).convert_alpha()
                notify_img = pygame.transform.scale(notify_box, (text_width * 1.1, text_height * 1.4))

                self.surface.blit(notify_img, [self.x, self.y])
            
            self.text.draw(self.surface, self.x + 4, self.y + 4)