import pygame
pygame.init()

# -------- Global Variables -----------

# --- Colours ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BGCOLOUR = (153, 255, 255)

# --- Sprites ---

# --- Misc ---
moveRight = False
moveLeft = False
moveUp = False
moveDown = False

playerX = 0
playerY = 0
playerMovSpeed = 5

# -------- Initialize Game -----------

# Open main game window
size = (1280, 720)
mainScreen = pygame.display.set_mode(size)
pygame.display.set_caption("Cool game")

running = True
 
# Clock is used to control how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while running:
    
    # --- Main event loop ---
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              running = False # Flag that we are done so we exit the game loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: moveRight = True
            if event.key == pygame.K_a: moveLeft = True
            if event.key == pygame.K_w: moveUp = True
            if event.key == pygame.K_s: moveDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d: moveRight = False
            if event.key == pygame.K_a: moveLeft = False
            if event.key == pygame.K_w: moveUp = False
            if event.key == pygame.K_s: moveDown = False
 
    # --- Game logic ---
    if moveRight: playerX += playerMovSpeed
    if moveLeft:  playerX -= playerMovSpeed
    if moveUp:    playerY -= playerMovSpeed
    if moveDown:  playerY += playerMovSpeed

    # --- Drawing Logic ---
    # Set BG colour to white
    mainScreen.fill(BGCOLOUR)

    pygame.draw.rect(mainScreen, RED, pygame.Rect(playerX, playerY, 60, 60))

    # Update screen
    pygame.display.flip()
     
    # Set Framerate to 60fps
    clock.tick(60)


 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()