import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 800, 600
FPS = 60

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicjalizacja okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atari Pong")

# Zegar gry
clock = pygame.time.Clock()

# Gracz
player_height = 100
player_width = 10
player_speed = 8
player1_pos = [0, HEIGHT // 2 - player_height // 2]
player2_pos = [WIDTH - player_width, HEIGHT // 2 - player_height // 2]
player2_speed = 8

# Piłka
ball_size = 20
ball_speed = 6
ball_pos = [WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2]
ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]

# Punkty
score_player1 = 0
score_player2 = 0
font = pygame.font.Font(None, 36)

# Dodaj nową zmienną
game_paused = False

# Ekran wyboru trybu gry
game_mode_selection = True
duo_mode = False

while game_mode_selection:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Wybór gry przeciwko komputerowi
                game_mode_selection = False
            elif event.key == pygame.K_2:  # Wybór gry dwuosobowej
                game_mode_selection = False
                duo_mode = True

    # Rysowanie tła
    screen.fill(BLACK)

    # Rysowanie tekstu na ekranie wyboru trybu gry
    mode_selection_text = font.render("Select Game Mode", True, WHITE)
    solo_text = font.render("1 - Solo (Against Computer)", True, WHITE)
    duo_text = font.render("2 - Duo (Two Players)", True, WHITE)

    screen.blit(mode_selection_text, (WIDTH // 2 - mode_selection_text.get_width() // 2, HEIGHT // 4))
    screen.blit(solo_text, (WIDTH // 2 - solo_text.get_width() // 2, HEIGHT // 2))
    screen.blit(duo_text, (WIDTH // 2 - duo_text.get_width() // 2, HEIGHT // 2 + 50))

    # Aktualizacja ekranu
    pygame.display.flip()

    clock.tick(FPS)

# Główna pętla gry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = not game_paused

    if not game_paused:
        keys = pygame.key.get_pressed()
        # Ruch gracza 1
        if keys[pygame.K_w] and player1_pos[1] > 0:
            player1_pos[1] -= player_speed
        if keys[pygame.K_s] and player1_pos[1] < HEIGHT - player_height:
            player1_pos[1] += player_speed

        # Ruch gracza 2 w grze dwuosobowej
        if duo_mode:
            if keys[pygame.K_UP] and player2_pos[1] > 0:
                player2_pos[1] -= player_speed
            if keys[pygame.K_DOWN] and player2_pos[1] < HEIGHT - player_height:
                player2_pos[1] += player_speed
        # Ruch komputera w grze przeciwko komputerowi
        elif not duo_mode:
            if player2_pos[1] + player_height // 2 < ball_pos[1]:
                player2_pos[1] += player2_speed
            elif player2_pos[1] + player_height // 2 > ball_pos[1]:
                player2_pos[1] -= player2_speed

        # Ruch piłki
        ball_pos[0] += ball_speed * ball_direction[0]
        ball_pos[1] += ball_speed * ball_direction[1]

        # Kolizje z górną i dolną krawędzią ekranu
        if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - ball_size:
            ball_direction[1] *= -1

        # Kolizje z paletkami
        if (
            player1_pos[0] + player_width > ball_pos[0] > player1_pos[0]
            and player1_pos[1] + player_height > ball_pos[1] > player1_pos[1]
        ) or (
            player2_pos[0] < ball_pos[0] + ball_size < player2_pos[0] + player_width
            and player2_pos[1] + player_height > ball_pos[1] > player2_pos[1]
        ):
            ball_direction[0] *= -1

        # Zdobywanie punktów
        if ball_pos[0] < 0:
            score_player2 += 1
            game_paused = True
            ball_pos = [WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2]
        elif ball_pos[0] > WIDTH - ball_size:
            score_player1 += 1
            game_paused = True
            ball_pos = [WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2]

    # Sprawdź warunek zakończenia gry
    if score_player1 == 11 or score_player2 == 11:
        winner_text = font.render(f"Player {1 if score_player1 == 11 else 2} WINS!", True, WHITE)
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)  # Pauza na 3 sekundy po zakończeniu gry
        pygame.quit()
        sys.exit()

    # Rysowanie tła
    screen.fill(BLACK)

    # Rysowanie paletki gracza 1
    pygame.draw.rect(screen, WHITE, (player1_pos[0], player1_pos[1], player_width, player_height))

    # Rysowanie paletki gracza 2
    pygame.draw.rect(screen, WHITE, (player2_pos[0], player2_pos[1], player_width, player_height))

    # Rysowanie piłki
    pygame.draw.ellipse(screen, WHITE, (ball_pos[0], ball_pos[1], ball_size, ball_size))

    # Wyświetlanie wyniku
    score_text = font.render(f"{score_player1} - {score_player2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Wyświetlanie informacji o zatrzymaniu gry
    if game_paused:
        pause_text = font.render("PAUSED - Press SPACE to resume", True, WHITE)
        screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))

    # Aktualizacja okna
    pygame.display.flip()

    # Ustawienie FPS
    clock.tick(FPS)
