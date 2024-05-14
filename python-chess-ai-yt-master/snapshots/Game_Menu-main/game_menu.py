import pygame
from sys import exit 
from random import *
from math import floor
from logging import *
from games import * 
from twoPersonShooter import main as Shooter

basicConfig(
    level=INFO,
    format='%(asctime)s - %(message)s'
)
disable(level=WARNING)

# Constants
screen_ratio = 16/9
WIDTH = 380
HEIGHT = int(WIDTH * screen_ratio)

# Initialise
pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT), 1, 32)
# pygame.display.set_caption('My Game')
BLACK = (0,0,0)
BLUE1 = (0,150,200)
BLUE2 = (0, 100, 255)
num_of_games = 6

class Menu():
    game_names = [
        'Game #1', 'Game #2', 
        'Game #3', 'Game #4', 
        'Game #5', 'Game #6', 
        'Game #7', 'Game #8',
        'Game #9', 'Game #10']
    title_area_height = 0
    icon_width = 0
    icon_height = 0
    cols = 3 # Change to add more games to menu

    def __init__(self, win, fxns_list, game_icons):
        self.surface = win 
        if len(game_icons) < len(fxns_list):
            raise Exception('Number of functions doesn\'t match number of icons')
        if len(game_icons) > len(fxns_list):
            num_fxns_absent = len(game_icons) - len(fxns_list)
            fxns_list.extend([self.dudFxn]*num_fxns_absent)
        self.fxns_list = fxns_list # hold list of functions
        self.game_icons = game_icons
        self.game_icons_index = self.gameIconsIndex()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            keys = pygame.key.get_pressed() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for icon, fxn in zip(self.game_icons, self.fxns_list):
                        if icon.isClicked(mouse_pos):
                            fxn()
            if keys[pygame.K_q]:
                running = False
                    
            pygame.display.set_mode((WIDTH, HEIGHT), 1, 32) # pygame.RESIZABLE, 32)
            self.display()
            pygame.display.update()
        pygame.quit()
        exit(0)

    def display(self):
        # Title section
        font_title = pygame.font.SysFont('times', 41)
        self.surface.fill(BLUE1)
        menu_title = font_title.render('MAIN MENU', False, BLACK)
        spacing_y = 10
        self.title_area_height = 50 + menu_title.get_height() + 2*spacing_y
        title_section_rect = pygame.Rect(0, 0, WIDTH, self.title_area_height)
        pygame.draw.rect(self.surface, BLUE2, title_section_rect)
        self.surface.blit(menu_title, 
            (WIDTH/2-menu_title.get_width()/2, int(self.title_area_height/3)))

        # Place images
        game_icons_pos = self.gameIconsPosition()
        for icon, pos in zip(self.game_icons, game_icons_pos):
            icon.pos = pos 
            self.surface.blit(icon.image, icon.pos)

        # Title images
        font_name = pygame.font.SysFont('baskervilleoldface', int(self.icon_width/10)) #15)
        for i in range(len(self.game_icons)):
            game_name = font_name.render(self.game_names[i], False, BLACK)
            name_x = game_icons_pos[i][0] + self.icon_width/7
            name_y = game_icons_pos[i][1] + self.icon_height + 3
            self.surface.blit(game_name, (name_x, name_y))
            
    def gameIconsIndex(self):
        row = 0
        game_icons_index = []

        for i in range(0,len(self.game_icons)):
            if i%self.cols==0 and i>0:
                row += 1
            game_icons_index.append((i%self.cols, row))
        return game_icons_index

    def gameIconsPosition(self):
        spacing_y = 30
        spacing_x = int(WIDTH/70) # 10
        gaps = floor(len(self.game_icons)/2)
        game_area_height = HEIGHT - self.title_area_height
        self.icon_height = int((game_area_height-spacing_y*3) / (gaps+1))
        self.icon_width = int((WIDTH-spacing_x*3)/self.cols)

        # Resize images
        for icon in self.game_icons:
            icon.image = resizeImage(icon.image, self.icon_width, self.icon_height)

        game_icons_pos = []
        for i,j in self.game_icons_index:
            x = (i+1)*spacing_x + i*self.icon_width
            y = self.title_area_height + (j+1)*spacing_y + j*self.icon_height
            game_icons_pos.append((x,y))
        return game_icons_pos

    def dudFxn(self):
        info('in dud')


class GameIcon():
    def __init__(self, img, pos=(0,0)):
        '''img: image surface
            pos: (x0, y0) position of the image
        '''
        self.image = img
        self.pos = pos 

    def isClicked(self, mouse_pos):
        '''Check whether this game icon was clicked or not'''
        mouse_x, mouse_y = mouse_pos 
        if (self.pos[0] <= mouse_x <= self.pos[0]+self.image.get_width()) and \
        (self.pos[1] <= mouse_y <= self.pos[1]+self.image.get_height()):
            return True
        return False 


def resizeImage(image, width, height):
    resized_image = pygame.transform.scale(image, (width, height))
    return resized_image

icon_list = []
for i in range(num_of_games):
    file = f'assets/images/img{i+1}.jpg'
    img = pygame.image.load(file)
    g = GameIcon(img)
    icon_list.append(g)
game_list = [changeScreenYellow, changeScreenCyan, Shooter]

main_menu = Menu(WIN, game_list, icon_list)
main_menu.run()