
import pygame, os, sys
import lenpy

pygame.init()

# Colores
WHITE = pygame.Color("#ffffff")
BLACK = pygame.Color("#000000")
RED = pygame.Color("#FF0000")
GREEN = pygame.Color("#25914C")
BLUE = pygame.Color("#0000FF")

# Tamaño de la pantalla
screen_size = [800, 480]

screen = lenpy.config.set_display(screen_size)
pygame.display.set_caption("Test Len'Py Button")

# Localiza el directorio de ejecución
source_dir = os.path.split(os.path.abspath(__file__))[0]

# Define los botones de texto
buttontext_a = lenpy.ui.TextButton("Boton", "arial.ttf", 24, "#FF0000", "#25914C", "#0000FF", "quit", font_dir=f"{source_dir}\\fonts\\")
buttontext_b = lenpy.ui.TextButton("Otro boton", "arial.ttf", 24, "#FF0000", "#25914C", "#0000FF", True, font_dir=f"{source_dir}\\fonts\\")

# Define los botones de imagen
buttonimage_a = lenpy.ui.ImageButton(f"{source_dir}\\button_example\\normal.png", f"{source_dir}\\button_example\\hover.png", f"{source_dir}\\button_example\\select.png", "quit", 0.2)
buttonimage_b = lenpy.ui.ImageButton(f"{source_dir}\\button_example\\normal.png", f"{source_dir}\\button_example\\hover.png", f"{source_dir}\\button_example\\select.png", True, 0.2)


# Texto de los botones
text_a = lenpy.Text("Image Button A", "arial", 24, None, BLACK, sysfont=True)
text_b = lenpy.Text("Image Button B", "arial", 24, None, BLACK, sysfont=True)

while True:
    
    # Obtiene los eventos
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # Dibuja los textos
    buttontext_a.draw(screen, 20, 20)
    buttontext_b.draw(screen, 400, 20)

    text_a.draw(screen, 20, 160)
    text_b.draw(screen, 400, 160)

    # Dibuja los ImageButtons en la pantalla
    buttonimage_a.draw(screen, 20, 200)
    buttonimage_b.draw(screen, 400, 200)

    # Esto te servira para crear tus propias acciones
    if buttontext_b.draw(screen, 400, 20):
        print("El boton se esta presionando...")

    if buttonimage_b.draw(screen, 400, 200):
        print("El boton de imagen se esta presionando...")

    pygame.display.flip()
    lenpy.config.clock.tick(60)