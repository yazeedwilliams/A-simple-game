# This is a pygame program that is a simple game. The objective of the game is to avoid the enemies and hit at least one jewel to win
# I used this video https://youtu.be/FfWpgLFMI7w, by  https://www.freecodecamp.org to help me understand the functions of pygame better
# I also used https://www.flaticon.com to get images and downloaded them with the size of 64 pixels

# Importing the pygame library to use pygame funtions
# Importing the random library to generate random numbers
import pygame
import random

# Initialising the pygame module
pygame.init()

# creating a window and setting the size and name of the window
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jewel Collision")

# Loading the player image
player = pygame.image.load("superhero.png")   # <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>


# Loading the enemies images
enemy1 = pygame.image.load("ghost.png")    # <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

enemy2 = pygame.image.load("ghost2.png")   # <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

enemy3 = pygame.image.load("ghost3.png")   # <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>


# Loading the prizes images
prize1 = pygame.image.load("crown.png")

prize2 = pygame.image.load("jewel.png")


# width and height of images
# Used the .get_height function to get the player width and height so that it can be used later
player_height = player.get_height()
player_width = player.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

# Used the .get_height function to get the enemy width and height so that it can be used later
enemy1Height = enemy1.get_height()
enemy1Width = enemy1.get_width()

enemy2Height = enemy2.get_height()
enemy2Width = enemy2.get_width()

enemy3Height = enemy3.get_height()
enemy3Width = enemy3.get_width()

# Used the .get_height function to get the prize width and height so that it can be used later prize width and height
prize1_height = prize1.get_height()
prize1_width = prize1.get_width()

prize2_height = prize2.get_height()
prize2_width = prize2.get_width()


# Player starting position
playerXPosition = 100
playerYPosition = 300

# Enemy starting positions
# Each enemy x coordinate starting postion is different so that they do not come onto the screen at the same time
enemy1XPosition =  1040
enemy1YPosition =  random.randint(0, screen_height - enemy1Height)

enemy2XPosition =  1500
enemy2YPosition =  random.randint(0, screen_height - enemy2Height)

enemy3XPosition =  1750
enemy3YPosition =  random.randint(0, screen_height - enemy3Height)

# Prize start position
# Each prize x coordinate starting postion is different so that they do not come onto the screen at the same time
prize1XPosition = 1200
prize1YPosition = random.randint(0, screen_height - prize1_height)

prize2XPosition = 1400
prize2YPosition = random.randint(0, screen_height - prize2_height)



# Declaring the movement keys as False because they are not being pressed yet
keyUp= False
keyDown = False
keyRight = False
keyLeft = False

# Game loop
# This is where all the events in the game is coded
while 1:

    # screen.fill changes the colour of the surface using the RGB formula
    screen.fill((153, 255, 255))

    # screen.blit renders the images ontop of the surface at the specified coordinates
    screen.blit(player, (playerXPosition, playerYPosition))

    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))

    screen.blit(prize1, (prize1XPosition, prize1YPosition))
    screen.blit(prize2, (prize2XPosition, prize2YPosition))

    # This updates the screen
    pygame.display.flip()

    # This is a loop that is used to check if the exited the game by pressing the exit button of the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    
        # If statement to check a key on the keyboard is pressed
        # pygame.KEYDOWN lets you test this 
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True

        # If statement to check a key on the keyboard is released
        # pygame.KEYUP lets you test this
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height: # This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1

    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position
    playerBox.top = playerYPosition            
    playerBox.left = playerXPosition
    
    # Bounding boxes for the enemies:

    enemy1Box = pygame.Rect(enemy1.get_rect())

    # The following updates the enemyBox position to the enemy's position
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding boxes for the prizes

    prize1Box = pygame.Rect(prize1.get_rect())

    # The following updates the prizeBox position to the prize's position
    prize1Box.top = prize1YPosition
    prize1Box.left = prize1XPosition

    prize2Box = pygame.Rect(prize2.get_rect())

    # The following updates the prizeBox position to the prize's position
    prize2Box.top = prize2YPosition
    prize2Box.left = prize2XPosition

    
    # Test collision of the player and enemy boxes:
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    # Test collision of the player and prize boxes

    if playerBox.colliderect(prize1Box) or playerBox.colliderect(prize2Box):
        print("You win!")
        pygame.quit()
        exit(0)

    elif prize1XPosition and prize2XPosition < -64: # -64 because the image size is 64 pixels    
        print("You lose!")
        pygame.quit()
        exit(0)

    # enemy movement
    enemy1XPosition -= 0.5
    enemy2XPosition -= 0.45
    enemy3XPosition -= 0.4

    # prize movement
    prize1XPosition -= 0.25
    prize2XPosition -= 0.35

    # ================The game loop logic ends here. =============

        
    
    


