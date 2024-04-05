import pygame
import sys

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Crear un círculo como sprite del jugador
        self.image = pygame.Surface([50, 50], pygame.SRCALPHA)  # SRCALPHA para canal alfa
        pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 25)
        # Obtener el rectángulo del sprite
        self.rect = self.image.get_rect()
        # Establecer la posición inicial del jugador
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        # Mover el jugador según las teclas presionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Rebotar si el jugador sale de la pantalla
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

def main():
    pygame.init()

    # Inicializar la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Move the Circle")

    # Crear un grupo de sprites y añadir el jugador
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    clock = pygame.time.Clock()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar los sprites
        all_sprites.update()

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar los sprites en la pantalla
        all_sprites.draw(screen)

        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar la velocidad de fotogramas
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()