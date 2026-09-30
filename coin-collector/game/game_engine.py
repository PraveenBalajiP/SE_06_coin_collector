"""
GameEngine: owns the player and all coins.

Starter version: one coin type, no obstacles, no timer yet. Coin
collection also has a known bug (see how `update` uses check_collection
below) that Task 1 asks you to fix - collected coins are never removed,
so standing on one keeps awarding points every frame.
"""

import random
import pygame

from game.player import Player
from game.coin import Coin
from game.collection import check_collection
from game.renderer import WIDTH, HEIGHT

NUM_COINS = 6

COIN_TYPES = [
    {"value": 1, "color": (184, 115, 51)},   # Bronze
    {"value": 3, "color": (192, 192, 192)},  # Silver
    {"value": 5, "color": (255, 215, 0)},    # Gold
]

OBSTACLES = [
    pygame.Rect(100, 100, 120, 30),
    pygame.Rect(300, 220, 30, 120),
    pygame.Rect(500, 100, 120, 30),
]


class GameEngine:
    def __init__(self):
        self.player = Player(x=WIDTH / 2, y=HEIGHT / 2)
        self.coins = [self._random_coin() for _ in range(NUM_COINS)]
        self.obstacles = OBSTACLES.copy()
        self.score = 0
        self.lives = 3

    def _random_coin(self):
        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)

        coin_type = random.choice(COIN_TYPES)

        return Coin(
            x=x,
            y=y,
            radius=12,
            value=coin_type["value"],
            color=coin_type["color"]
        )

    def handle_input(self, keys_pressed):
        dx = dy = 0
        if keys_pressed[pygame.K_UP]:
            dy -= self.player.speed
        if keys_pressed[pygame.K_DOWN]:
            dy += self.player.speed
        if keys_pressed[pygame.K_LEFT]:
            dx -= self.player.speed
        if keys_pressed[pygame.K_RIGHT]:
            dx += self.player.speed
        self.player.move(dx, dy, WIDTH, HEIGHT)

    def update(self):
        collected = check_collection(self.player, self.coins)
        for coin in collected:
            self.score += coin.value
            self.coins.remove(coin)
        player_rect = self.player.get_rect()
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle):
                self.lives -= 1
                self.player.x = WIDTH / 2
                self.player.y = HEIGHT / 2
                break

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_scene(surface,self.player,self.coins,self.obstacles)
        renderer.draw_text(surface, font, f"Score: {self.score}", (10, 10))
        renderer.draw_text(surface, font, f"Lives: {self.lives}", (10, 40))