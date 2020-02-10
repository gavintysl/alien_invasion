import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
import game_functions as gf
from button import Button

def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #Make the play button
    play_button = Button(ai_settings, screen, "Play game")
    
    #Create an instance to store game statistics and create a scoreboard
    # Create an instance to store game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    #Make a ship,a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Set the background color.
    #bg_color = (230, 230, 230)
    
    #Start the main loop for the game
    while True:
        #Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
#        #Get rid of bullets that have disappeared.
#        for bullet in bullets.copy():
#            if bullet.rect.bottom <= 0:
#                bullets.remove(bullet)
#        print(len(bullets))
        
        
        #Redraw the screen during each pass through the loop
#        screen.fill(bg_color)
#        
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                sys.exit()
#        screen.fill(ai_settings.bg_color)
#        ship.blitme()
#            #Make the most recently drawn screen visible.
#        pygame.display.flip()           
            
run_game()
    #Initialize game and create screen object
    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

