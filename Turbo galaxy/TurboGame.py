import pygame
import random
import sys

# Inicializar pygame y mixer
pygame.init()
pygame.mixer.init()

# Dimensiones
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Turbo Galaxy")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
TURQUESA = (64, 224, 208)

# Cargar imágenes
bg = pygame.image.load("img/background.png").convert()
player_img = pygame.image.load("img/cars.png").convert_alpha()
coco_img = pygame.image.load("img/coco.png").convert_alpha()
heart_img = pygame.image.load("img/heart.png").convert_alpha()

# Escalado de imágenes
player_img = pygame.transform.scale(player_img, (60, 60))
coco_img = pygame.transform.scale(coco_img, (40, 40))
heart_img = pygame.transform.scale(heart_img, (30, 30))

# Música
try:
    pygame.mixer.music.load("assets/music.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
except:
    print("No se pudo cargar la música.")

# Reloj
clock = pygame.time.Clock()
FPS = 60

# Jugador
player_rect = player_img.get_rect()
player_rect.center = (ANCHO // 2, ALTO - 80)
velocidad_jugador = 5

# Cocos
cocos = []
for _ in range(5):
    coco_rect = coco_img.get_rect()
    coco_rect.x = random.randint(0, ANCHO - coco_rect.width)
    coco_rect.y = random.randint(-600, -40)
    cocos.append(coco_rect)

# HUD
vidas = 3
puntuacion = 0
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont("Arial", 60)

# Funciones de ayuda
def mostrar_texto(texto, x, y, color=BLANCO, fuente=font):
    render = fuente.render(texto, True, color)
    pantalla.blit(render, (x, y))

def mostrar_vidas():
    for i in range(vidas):
        pantalla.blit(heart_img, (10 + i * 35, 10))

def reiniciar_juego():
    global vidas, puntuacion, player_rect, cocos
    vidas = 3
    puntuacion = 0
    player_rect.center = (ANCHO // 2, ALTO - 80)
    cocos.clear()
    for _ in range(5):
        coco_rect = coco_img.get_rect()
        coco_rect.x = random.randint(0, ANCHO - coco_rect.width)
        coco_rect.y = random.randint(-600, -40)
        cocos.append(coco_rect)

# Pantalla de Inicio
def pantalla_inicio():
    boton_rect = pygame.Rect(ANCHO//2 - 100, ALTO//2 + 50, 200, 60)
    portada = pygame.image.load("img/background.png").convert()

    while True:
        pantalla.blit(portada, (0, 0))  # Fondo playa espacial

        # Título
        mostrar_texto("🌴 TURBO GALAXY 🚀", ANCHO//2 - 200, ALTO//3 - 60, BLANCO, big_font)

        # Mouse y botón
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if boton_rect.collidepoint(mouse_pos):
            pygame.draw.rect(pantalla, (0, 180, 180), boton_rect)
            if mouse_click[0]:
                pygame.time.delay(200)
                return
        else:
            pygame.draw.rect(pantalla, TURQUESA, boton_rect)

        mostrar_texto("Comenzar", boton_rect.x + 45, boton_rect.y + 15, NEGRO)

        mostrar_texto("Presiona ESC para salir", ANCHO//2 - 160, ALTO - 60, BLANCO)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Bucle principal del juego
def game_loop():
    global vidas, puntuacion
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= velocidad_jugador
        if keys[pygame.K_RIGHT] and player_rect.right < ANCHO:
            player_rect.x += velocidad_jugador

        pantalla.blit(bg, (0, 0))
        pantalla.blit(player_img, player_rect)

        for coco in cocos:
            coco.y += 5
            pantalla.blit(coco_img, coco)

            if coco.top > ALTO:
                coco.x = random.randint(0, ANCHO - coco.width)
                coco.y = random.randint(-100, -40)
                puntuacion += 1

            if player_rect.colliderect(coco):
                coco.x = random.randint(0, ANCHO - coco.width)
                coco.y = random.randint(-100, -40)
                vidas -= 1

        mostrar_texto(f"Puntos: {puntuacion}", ANCHO - 150, 10)
        mostrar_vidas()

        if vidas <= 0:
            mostrar_texto("GAME OVER - Presiona R para reiniciar o Q para salir", 100, ALTO // 2)
            pygame.display.flip()
            esperando = True
            while esperando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            reiniciar_juego()
                            esperando = False
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()

    pygame.quit()

# Iniciar el juego
if __name__ == "__main__":
    pantalla_inicio()
    game_loop()







