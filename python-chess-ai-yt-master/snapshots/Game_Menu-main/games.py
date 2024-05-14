''' This contains the games that will be options for the game_menu 
'''
import pygame
pygame.init()


def changeScreenYellow():
    WIDTH = 400
    HEIGHT = 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT), 1, 32)
    pygame.display.set_caption('Change Colour')
    print('In changeScreenYellow')

    clock = pygame.time.Clock() 
    running = True 
    
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                print('Back to Menu')
                running = False 
        
        WIN.fill((255,255,0))
        pygame.display.update()


def changeScreenCyan():
    WIDTH = 600
    HEIGHT = 400
    WIN = pygame.display.set_mode((WIDTH, HEIGHT), 1, 32)
    pygame.display.set_caption('Change Colour')
    print('In changeScreenCyan')

    fam = pygame.image.load('assets/images/img5.jpg')
    fam = pygame.transform.scale(fam, (600,200))

    clock = pygame.time.Clock() 
    running = True 
    
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                print('Back to Menu')
                running = False 
        
        WIN.fill((0,255,255))
        WIN.blit(fam, (0,0))
        pygame.display.update()

