import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize game and create screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group of bullets and aliens.
    bullets = Group()
    aliens = Group()
    
    # Creat a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
        
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
run_game()
