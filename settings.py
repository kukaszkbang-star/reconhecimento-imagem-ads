# settings.py

# Dimensões da tela
WIDTH = 800
HEIGHT = 600
FPS = 60

# Cores (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Configurações do Player
PLAYER_SPEED = 5
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40

# Configurações do Tiro (Bullet)
BULLET_SPEED = -10
BULLET_WIDTH = 5
BULLET_HEIGHT = 15

# Configurações dos Asteroides (valores iniciais)
ASTEROID_MIN_SPEED = 1
ASTEROID_MAX_SPEED = 3
ASTEROID_WIDTH = 40
ASTEROID_HEIGHT = 40

# Dificuldade progressiva
# A cada SCORE_PER_LEVEL pontos, a dificuldade sobe 1 nível
SCORE_PER_LEVEL = 50
# Limite máximo de nível (evita o jogo ficar injogável)
MAX_LEVEL = 10
# Spawn rate inicial (chance em 100 por frame de criar um asteroide)
SPAWN_RATE_INITIAL = 1
# Taxa máxima de spawn (teto)
SPAWN_RATE_MAX = 6
