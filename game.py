import pygame
import sys
import random
from settings import *
from sprites import Player, Asteroid

def main():
    pygame.init()
    pygame.font.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Atari Space Shooter")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    score = 0
    level = 1
    running = True
    game_over = False

    while running:
        clock.tick(FPS)

        # 1. Processamento de Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    player.shoot(all_sprites, bullets)
                if event.key == pygame.K_r and game_over:
                    # Reiniciar o jogo
                    all_sprites.empty()
                    asteroids.empty()
                    bullets.empty()
                    player = Player()
                    all_sprites.add(player)
                    score = 0
                    level = 1
                    game_over = False

        if not game_over:
            # 2. Atualização
            all_sprites.update()

            # Calcular nível de dificuldade com base na pontuação
            level = min(1 + score // SCORE_PER_LEVEL, MAX_LEVEL)

            # Taxa de spawn sobe progressivamente com o nível
            spawn_rate = min(SPAWN_RATE_INITIAL + (level - 1), SPAWN_RATE_MAX)

            # Spawn de asteroides
            if random.randrange(100) < spawn_rate:
                asteroid = Asteroid(level=level)
                all_sprites.add(asteroid)
                asteroids.add(asteroid)

            # Verificar colisão entre tiro e asteroide
            hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
            for hit in hits:
                score += 10

            # Verificar colisão entre player e asteroide
            hits = pygame.sprite.spritecollide(player, asteroids, False)
            if hits:
                game_over = True

            # Verificar se algum asteroide passou do fundo da tela
            for asteroid in asteroids:
                if asteroid.rect.top > HEIGHT:
                    game_over = True

        # 3. Renderização
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Desenhar pontuação e nível
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        level_text = font.render(f"Level: {level}", True, YELLOW)
        screen.blit(level_text, (10, 40))

        if game_over:
            game_over_text = font.render("GAME OVER", True, RED)
            text_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(game_over_text, text_rect)
            restart_text = font.render("Pressione R para reiniciar", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
            screen.blit(restart_text, restart_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
