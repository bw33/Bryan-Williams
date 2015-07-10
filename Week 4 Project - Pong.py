# importing any relevant modules
import simplegui
import random   

# defining global variables
BALL_POSITION = [75, 75]
BALL_RADIUS = 8
BALL_VEL = [3, 5]
WIDTH = 600
HEIGHT = 450
PADDLE1_POS = [10, 225]
PADDLE2_POS = [590, 225]
PADDLE_WIDTH = 20
counter1 = 0
counter2 = 0
VEL = [0, 0]
VEL2 = [0, 0]

# defining event handlers  
def spawn_ball(direction):   # spawns ball going right or left
    global BALL_POSITION, BALL_VEL
    BALL_POSITION = [250, 250]
    if direction == "RIGHT":
        BALL_VEL[0] = random.randrange(2, 4)
        BALL_VEL[1] = -(random.randrange(2, 6))
    if direction == "LEFT":
        BALL_VEL[0] = -(random.randrange(2, 4))
        BALL_VEL[1] = random.randrange(2, 6)

def reset():
    global counter1, counter2
    counter1 = 0
    counter2 = 0
    new_game()

def new_game():
    direction = random.randrange(0,2)
    if direction == 0:
        spawn_ball("LEFT")
    elif direction ==1:
        spawn_ball("RIGHT")
    
def keydown(key):   # altering velocity vector based on key press
    global PADDLE1_POS, PADDLE2_POS, VEL, VEL2
    ACC = 5
    if key == simplegui.KEY_MAP["up"]:
        VEL2[1] = -ACC
    elif key == simplegui.KEY_MAP["down"]:
        VEL2[1] = ACC
    elif key == simplegui.KEY_MAP["w"]:
        VEL[1] = -ACC
    elif key == simplegui.KEY_MAP["s"]:
        VEL[1] = ACC
            
def keyup(key):  # velocity vector to [0, 0] when keys not being pressed
    global PADDLE1_POS, PADDLE2_POS, ACC, VEL, VEL2
    ACC = 0
    if key == simplegui.KEY_MAP["up"]:
        VEL2[1] = ACC
    elif key == simplegui.KEY_MAP["down"]:
        VEL2[1] = ACC
    elif key == simplegui.KEY_MAP["w"]:
        VEL[1] = ACC
    elif key == simplegui.KEY_MAP["s"]:
        VEL[1] = ACC   
    
def draw(canvas):
    PADDLE1_POS[1] += VEL[1]
    PADDLE2_POS[1] += VEL2[1]
    
    # code that stops paddles from passing the "ceilings" and 
    # "floors" of the table
    if PADDLE1_POS[1] <= 40:
       VEL[1] = 0 
    elif PADDLE1_POS[1] >= 410:
       VEL[1] = 0
    elif PADDLE2_POS[1] <= 40:
       VEL2[1] = 0
    elif PADDLE2_POS[1] >= 410:
       VEL2[1] = 0
   
    # coordinates of the two polygons - i.e. the two paddles
    POLY1 = [PADDLE1_POS[0], (PADDLE1_POS[1] - 40)]
    POLY2 = [PADDLE1_POS[0], PADDLE1_POS[1]]
    POLY3 = [PADDLE1_POS[0], (PADDLE1_POS[1] + 40)]
    POLY4 = [PADDLE2_POS[0], (PADDLE2_POS[1] - 40)]
    POLY5 = [PADDLE2_POS[0], PADDLE2_POS[1]]
    POLY6 = [PADDLE2_POS[0], (PADDLE2_POS[1] + 40)]
    
    BALL_POSITION[0] += BALL_VEL[0]
    BALL_POSITION[1] += BALL_VEL[1]
           
    # collision code, i.e. when the ball hits the paddles 
    if (BALL_POSITION[0] - BALL_RADIUS <= PADDLE1_POS[0] + 15 and
        BALL_POSITION[0] - BALL_RADIUS >= PADDLE1_POS[0] + 5 and 
        BALL_POSITION[1] <= PADDLE1_POS[1] + 40 and
        BALL_POSITION[1] >= PADDLE1_POS[1] - 40):
        BALL_VEL[0] = -BALL_VEL[0] - (BALL_VEL[0] * .10)
        BALL_VEL[1] = BALL_VEL[1] + (BALL_VEL[1] * .04)
    elif(BALL_POSITION[0] + BALL_RADIUS >= PADDLE2_POS[0] - 15 and 
         BALL_POSITION[0] - BALL_RADIUS <= PADDLE2_POS[0] - 5 and 
         BALL_POSITION[1] <= PADDLE2_POS[1] + 40 and
         BALL_POSITION[1] >= PADDLE2_POS[1] - 40):
         BALL_VEL[0] = -BALL_VEL[0] - (BALL_VEL[0] * .10)
         BALL_VEL[1] = BALL_VEL[1] + (BALL_VEL[1] * .04)
    elif BALL_POSITION[0] > WIDTH - BALL_RADIUS - PADDLE_WIDTH:
         global counter1
         counter1 += 1         
         spawn_ball("LEFT") 
    elif BALL_POSITION[0] < BALL_RADIUS + PADDLE_WIDTH:
         global counter2
         counter2 += 1
         spawn_ball("RIGHT")
    elif BALL_POSITION[1] > HEIGHT - BALL_RADIUS:
        BALL_VEL[1] = -BALL_VEL[1]
    elif BALL_POSITION[1] < BALL_RADIUS:
        BALL_VEL[1] = -BALL_VEL[1]
    
    canvas.draw_circle(BALL_POSITION, BALL_RADIUS, 5, "White", "White")
    canvas.draw_polygon((POLY1, POLY2, POLY3), PADDLE_WIDTH / 2, "White", "Gray")
    canvas.draw_polygon((POLY4, POLY5, POLY6), PADDLE_WIDTH / 2, "White", "Gray") 
    canvas.draw_polygon(([16, 0],[16, 225],[16, 450]), 2, "Gray", "Gray")
    canvas.draw_polygon(([584, 0],[584, 225],[584, 450]), 1.5, "Gray", "Gray")
    canvas.draw_polygon(([300, 0], [300, 225], [300, 450]), 1, "Gray", "Gray")
    canvas.draw_text(str(counter1), [150, 50], 30, "White")
    canvas.draw_text(str(counter2), [450, 50], 30, "White")

# create frame
frame = simplegui.create_frame("Pong Project", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.add_button("New Game!", reset, 100)

# start frame
frame.start()
