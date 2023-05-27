"""
TITLE: Jumpy!
DESCRIPTION: A platform game
"""
# --- libraries --- #
import pygame, tsk

# --- setup --- #

# pygame
pygame.init()
w = pygame.display.set_mode([500, 500])

# variables
ypos = 0
xpos = 250 

yvel = 0
xvel = 0

jump = False
mainfloor = 450
floor = mainfloor

# functions 
def cube(x, y, count):
    """
    BUGLIST
    -when you stand next to the left of a block, and press right arrow and up
    -=-repeatable with right side and corresponding keys
    -=-has to do with tricking the xvel 
    """
    # global variables 
    global xpos 
    global ypos 
    global xvel
    global yvel
    global floor
    global mainfloor 
    
    # render platform
    cube = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(w, (127, 127, 127), cube)
    
    # check in platform 
    if xpos > x-50 and xpos < x+50 and ypos > y-50: 
        if ypos-50 < y-50: # ypos-50 is the size of the square, moving it out of the platform
            yvel = 0
            floor = y-50
            ypos = floor
        else:
            if xvel > 0:
                xvel = 0
                xpos = x-50
            elif xvel < 0:
                xvel = 0
                xpos = x+50
    elif xpos < x-50 or xpos > x+50:
        if count == 1:
            floor = mainfloor
# running loop
run = True

# --- main loop --- #
while run:
    # --- key presses --- #
    # event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    # key check 
    jump = False
    if ypos == floor:
        if tsk.get_key_pressed(pygame.K_UP):
            jump = True
        else:
            jump = False
    
    xpressed = False
    if tsk.get_key_pressed(pygame.K_RIGHT):
        xvel += 1
        xpressed = True
    if tsk.get_key_pressed(pygame.K_LEFT):
        xvel -= 1 
        xpressed = True
    
    # --- math --- # 
    # velocity
    yvel += 1
    
    # y movement
    ypos += yvel
    if ypos > floor:
        ypos = floor
    if jump:
        yvel = -15
            
    # x movement
    if not xpressed:
        if xvel != 0:
            if xvel > 0:
                xvel -= 1
            else:
                xvel += 1
    
    if xvel > 7:
        xvel = 7
    if xvel < -7:
        xvel = -7
    
    xpos += xvel 
    
    # --- final checks --- #
        
    # bound check 
    if xpos > 450:
        xpos = 450
    elif xpos < 0:
        xpos = 0
    # --- render --- #
    # reset
    w.fill((0, 0, 0))
    
    # platforms
    cube(200, 450, 1)
    cube(250, 450, 2)
    
    # square init
    player = pygame.Rect(xpos, ypos, 50, 50)
    
    # square render 
    pygame.draw.rect(w, (255, 255, 255), player) 
    
    # end script 
    pygame.display.flip()
    pygame.time.wait(10)
