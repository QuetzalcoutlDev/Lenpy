
# Este modulo sigue en desarrollo
import pygame

pygame.display.init()

# Reloj
clock = pygame.time.Clock()

# Está función crea la superficie de la pantalla
def set_display(screen_size, fullscreen=False, resizable=True):

	# Usa un operador binario para colocar los flags por defecto
	flags = pygame.HWSURFACE|pygame.DOUBLEBUF

	if fullscreen:
		Surface = pygame.display.set_mode(screen_size, flags|pygame.FULLSCREEN)

	else:
		Surface = pygame.display.set_mode(screen_size, flags)

	if resizable:
		Surface = pygame.display.set_mode(screen_size, flags|pygame.RESIZABLE)

	else:
		Surface = pygame.display.set_mode(screen_size, flags)

	if fullscreen and not resizable:

		Surface = pygame.display.set_mode(screen_size, flags|pygame.FULLSCREEN)

	elif not fullscreen and resizable:
		Surface = pygame.display.set_mode(screen_size, flags|pygame.RESIZABLE)

	elif fullscreen and resizable:

		Surface = pygame.display.set_mode(screen_size, flags|pygame.FULLSCREEN|pygame.RESIZABLE)

	elif not fullscreen and not resizable:

		Surface = pygame.display.set_mode(screen_size, flags)

	return Surface

# screen_size = [640, 480]

# screen = set_display(screen_size)