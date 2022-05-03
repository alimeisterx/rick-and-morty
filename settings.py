import pygame
WINDOW_NAME = "iShwifty"
GAME_TITLE = WINDOW_NAME
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 750
FPS = 90
DRAW_FPS = True
# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 180
HAND_HITBOX_SIZE = (60, 80)
MORTY_SIZES = (80, 80)
MORTY_SIZE_RANDOMIZE = (1,2) # for each new morty, it will multiply the size with an random value beteewn X and Y
RICKS_SIZES = (100, 100)
RICK_SIZE_RANDOMIZE = (1.2, 1.5)
# drawing
DRAW_HITBOX = False # will draw all the hitbox
# animation
ANIMATION_SPEED = 0.09 # the frame of the deities will change every X sec
# difficulty
GAME_DURATION = 45 # the game will last X sec
MORTY_SPAWN_TIME = 1
MORTY_MOVE_SPEED = {"min": 1, "max": 6}
RICK_PENALITY = 1 # will remove X of the score of the player (if he kills an rick)
# colors
COLORS = {"title": (255, 255, 255), "score": (255, 255, 255), "timer": (255, 255, 255),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (0, 0, 0)}} # second is the color when the mouse is on the button
# sounds / music
MUSIC_VOLUME = 0.5 # value between 0 and 1
SOUNDS_VOLUME = 0.2
# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
