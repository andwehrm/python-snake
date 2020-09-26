import pygame
import random
import time


# Game Settings
dis_width = 500
dis_height = 400
block_size = 20
snake_size = 1
snake_speed = 15
food_strength = 5
snake_color = [220,61,75]
food_color = [76,217,100]
background_color = [28,37,46]
start_point = [300,300]
text_color = [220,61,75]

# Internal Values
x_food = 0
y_food = 0
x = start_point[0]
y = start_point[1]
y_change = 0
x_change = 0
snake_list = []
snake_block = []
moved = False

def draw_text(msg,font,color,coords, center):
    mesg = font.render(msg, True, color)
    if center == True:
        text_rec = mesg.get_rect(center=(coords[0]/2,coords[1]/2))
        dis.blit(mesg,text_rec)
    elif center == False:
        dis.blit(mesg,[coords[0],coords[1]])

def spawn_food():
    global x_food
    global y_food
    x_food = random.randrange(0,(dis_width-block_size)/block_size)*block_size
    y_food = random.randrange(0,(dis_height-block_size)/block_size)*block_size

def game_end():
    draw_text("Game Over",font_style,text_color,[dis_width,dis_height],True)
    draw_text("Score: " + str(snake_size),font_style,text_color,[dis_width,dis_height+60],True)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

pygame.init()
font_style = pygame.font.SysFont("ubuntu",25)
font_score = pygame.font.SysFont("ubuntu",18)

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Snake')


clock = pygame.time.Clock()
spawn_food()

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            game_end()
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_DOWN and moved == True:
                if y_change != -block_size:
                    y_change = block_size
                    x_change = 0
                    moved = False
            elif event.key == pygame.K_UP and moved == True:
                if y_change != block_size:
                    y_change = -block_size
                    x_change = 0
                    moved = False
            elif event.key == pygame.K_LEFT and moved == True:
                if x_change != block_size:
                    x_change = -block_size
                    y_change = 0
                    moved = False
            elif event.key == pygame.K_RIGHT and moved == True:
                if x_change != -block_size:
                    x_change = block_size
                    y_change = 0
                    moved = False

    dis.fill(background_color)

# Snake Movement
    x += x_change
    y += y_change
    moved = True

# Out of Bounds detection
    if x > dis_width or x < 0 or y > dis_height or y < 0:
        game_end()

# Collision with own Body detection
    for i in snake_list[1:]:
        if x == i[0] and y == i[1]:
            game_end()

# Snake Calculation
    snake_list.append([x,y])

    if len(snake_list) > snake_size:
        del snake_list[0]

# Drawing the Snake
    for i in snake_list:
        pygame.draw.rect(dis,snake_color,[i[0],i[1],block_size,block_size])

# Collision with food detection
    for i in snake_list:
        if(x_food == i[0] and y_food == i[1]):
            snake_size+=food_strength
            spawn_food()

# Drawing the Food
    pygame.draw.rect(dis,food_color,[x_food,y_food,block_size,block_size]) 

# Score Display
    draw_text("Score: " + str(snake_size),font_score,text_color,[5,0],False)
    pygame.display.update()
    clock.tick(snake_speed)

