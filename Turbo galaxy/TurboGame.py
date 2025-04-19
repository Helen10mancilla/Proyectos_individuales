import pygame
import sys
import os
import random

# Inicialización
pygame.init()

# Pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turbo Galaxy")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
YELLOW = (255, 255, 100)

# Cargar imágenes
bg_path = os.path.join("img", "background.png")
car_path = os.path.join("img", "cars.png")

background = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Cargar nave con transparencia
car_image = pygame.image.load(car_path).convert_alpha()
car_image = pygame.transform.scale(car_image, (60, 60))

# Fuentes
pygame.font.init()
title_font = pygame.font.SysFont("Orbitron", 70)
button_font = pygame.font.SysFont("Orbitron", 40)

# Función para mostrar texto centrado
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Colisión circular
def circle_collision(rect1, rect2):
    center1 = rect1.center
    center2 = rect2.center
    distance = ((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2) ** 0.5
    radius1 = rect1.width // 2
    radius2 = rect2.width // 2
    return distance < radius1 + radius2

# Menú principal
def main_menu():
    title_y_offset = 0
    direction = 1
    button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 100, 200, 60)

    while True:
        screen.blit(background, (0, 0))

        # Animación del título
        title_y_offset += direction * 0.5
        if title_y_offset > 10 or title_y_offset < -10:
            direction *= -1

        draw_text("TURBO GALAXY", title_font, YELLOW, screen, WIDTH // 2, HEIGHT // 2 - 100 + title_y_offset)

        # Botón interactivo
        mouse = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (200, 200, 50), button_rect)
        else:
            pygame.draw.rect(screen, (100, 100, 255), button_rect)

        draw_text("COMENZAR", button_font, WHITE, screen, button_rect.centerx, button_rect.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

        pygame.display.flip()
        clock.tick(60)

# Juego principal
def game_loop():
    angle = 0
    speed = 0
    car_rect = car_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    obstacles = []

    def create_obstacle():
        obstacle = pygame.Rect(random.randint(0, WIDTH-50), -50, 50, 50)
        obstacles.append(obstacle)

    running = True
    while running:
        screen.blit(background, (0, 0))

        # Generar obstáculos aleatorios
        if random.randint(1, 100) > 98:
            create_obstacle()

        for obstacle in obstacles[:]:
            obstacle.y += 5
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
            pygame.draw.rect(screen, (255, 0, 0), obstacle)

        # Movimiento de la nave
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            angle += 5
        if keys[pygame.K_RIGHT]:
            angle -= 5
        if keys[pygame.K_UP]:
            speed = 5
        else:
            speed = 0

        direction = pygame.math.Vector2(0, -1).rotate(angle)
        car_rect.centerx += direction.x * speed
        car_rect.centery += direction.y * speed

        # Dibujar la nave rotada
        rotated_image = pygame.transform.rotate(car_image, angle)
        rotated_rect = rotated_image.get_rect(center=car_rect.center)
        screen.blit(rotated_image, rotated_rect)

        # Detección de colisión
        for obstacle in obstacles:
            if circle_collision(rotated_rect, obstacle):
                print("¡Colisión! GAME OVER")
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Punto de entrada del juego
if __name__ == "__main__":
    main_menu()
    game_loop()
