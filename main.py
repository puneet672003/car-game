import random
import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 180, 0)
light_green = (0,255,0)
red = (180,0,0)
light_red = (255,0,0)
blue = (0, 0, 180)
light_yellow = (0,0,255)
yellow = (180,180,0)
light_yellow = (255,255,0)
road_colour = (131, 127, 135)

display_height = 600
display_width = 800
score_display_width = display_width
score_display_height = 40

display = pygame.display
gameDisplay = display.set_mode((display_width, display_height + score_display_height))
display.set_caption("Lets go yeaaaaaaaa !!!!!")
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
carImg = pygame.transform.scale(carImg, (60, 100))
score_bg = pygame.image.load('white_bg.png')
score_bg = pygame.transform.scale(score_bg, (score_display_width, score_display_height))
enemy_car_img = pygame.image.load('enemy_car.png')
enemy_car_img = pygame.transform.scale(enemy_car_img, (50, 80))
nitroImg = pygame.image.load('nitro.png')
nitroImg = pygame.transform.scale(nitroImg, (80, 80))

def car (x, y):
    gameDisplay.blit(carImg, (x, y))
def road(road_x, road_y):
    gameDisplay.blit(roadImg, (road_x, road_y))
def score_bg_print(x, y):
    gameDisplay.blit(score_bg, (x,y))
def enemy_car(x, y):
    gameDisplay.blit(enemy_car_img, (x, y))
def nitro(x, y):
    gameDisplay.blit(nitroImg, (x,y))

def button(msg, color, x_change, y_change, size, rect_color, mouse_pos):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, color)
    text_rect = screen_text.get_rect()
    rect_w = text_rect.width + 20
    rect_h = text_rect.height + 20
    pygame.draw.rect(gameDisplay, rect_color, [display_width/2 - screen_text.get_width()/2 + x_change - 10, display_height/2 - screen_text.get_height()/2 + y_change - 10, rect_w, rect_h])
    gameDisplay.blit(screen_text, [display_width/2 - screen_text.get_width()/2 + x_change, display_height/2 - screen_text.get_height()/2 + y_change])
    x1 = display_width/2 - screen_text.get_width()/2 + x_change - 10
    x2 = x1 + rect_w
    y1 = display_height/2 - screen_text.get_height()/2 + y_change - 10
    y2 = y1 + rect_h

    if rect_color == yellow:
        light_rect_color = light_yellow
    elif rect_color == red:
        light_rect_color = light_red
    elif rect_color == blue:
        light_rect_color = light_blue
    elif rect_color == green:
        light_rect_color = light_green

    if (mouse_pos[0] > x1 and mouse_pos[0] < x2) and (mouse_pos[1] > y1 and mouse_pos[1] < y2):
        pygame.draw.rect(gameDisplay, light_rect_color, [display_width/2 - screen_text.get_width()/2 + x_change - 10, display_height/2 - screen_text.get_height()/2 + y_change - 10, rect_w, rect_h])
        gameDisplay.blit(screen_text, [display_width/2 - screen_text.get_width()/2 + x_change, display_height/2 - screen_text.get_height()/2 + y_change])
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        return clicked

def message(msg, color, y_change = 0, size = 25, x_change = 0):
    font = pygame.font.SysFont("Comic Sans MS", size)
    screen_text = font.render(msg,True, color)
    gameDisplay.blit(screen_text, [(display_width/2 - screen_text.get_width()/2) + x_change, display_height/2 - screen_text.get_height()/2 + y_change])

def main_menu():
    main_menu = True
    while main_menu:
        gameDisplay.fill(white)
        message("WELCOME!!", red, -80, 80)
        message("to", black, -10, 25)
        message("HiGhWaY rIdEr", black, 50, 80)
        mouse_pos = pygame.mouse.get_pos()
        clicked = button("PLAY", red, 0, 200, 40, green,mouse_pos)
        if clicked:
            game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu = False
                pygame.quit()
                quit()
        pygame.display.update()

def pause():
    pause = True
    gameDisplay.fill(white)
    message("PAUSED", red, -100, 80)
    message("press p to continue", black , 0, 40)
    display.update()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False

def game_loop():
    x = (display_width * (1/4) - 5 + (display_width * (1/4) - 5) * 2) / 2 - carImg.get_width()/2
    y = display_height * 0.9
    change_x = (display_width * (1/4) - 5)* 2 - (display_width * (1/4) - 5)
    x_change = 0
    y_change = 0
    frame_rate = 60

#first line strips
    strip_x = 20
    strip_y = 30
    strip1_x = display_width * (1/4) - 5
    strip2_x = strip1_x * 2
    strip3_x = strip1_x * 3
    strip4_x = strip1_x * 4
#second line strips
    strip_y2 = 260
# third line strips
    strip_y3 = 490

#strips change and hurdle change
    hurdle_change = 4
    strip_change = 6

#defining hurdles in the way OF CAR
    hurdle_width = enemy_car_img.get_width()
    hurdle_height = enemy_car_img.get_height()
    hurdle2_x = (strip1_x + strip2_x) / 2 - hurdle_width/2
    hurdle1_y = random.randint(-(display_height*2), -display_height)
    hurdle3_x = (strip2_x + strip3_x) / 2 - hurdle_width/2
    hurdle2_y = random.randint(-(display_height*2), -display_height)
    hurdle4_x = (strip3_x + strip4_x) / 2 - hurdle_width/2
    hurdle3_y = random.randint(-(display_height*2), -display_height)
    hurdle1_x = (strip_x + strip1_x) / 2 - hurdle_width/2
    hurdle4_y = random.randint(-(display_height*2), -display_height)
    hurdle1_x2 = hurdle1_x + hurdle_width
    hurdle2_x2 = hurdle2_x + hurdle_width
    hurdle3_x2 = hurdle3_x + hurdle_width
    hurdle4_x2 = hurdle4_x + hurdle_width

#nitro details
    give_nitro = False
    add_nitro = False
    nitro_width = nitroImg.get_width()
    nitro_x = random.choice([(strip1_x + strip2_x) / 2 - nitro_width/2, (strip2_x + strip3_x) / 2 - nitro_width/2, (strip3_x + strip4_x) / 2 - nitro_width/2, (strip4_x + strip_x) / 2 - nitro_width/2])
    nitro_y = random.randint(-display_height, -100)
    nitro_change = 4

#main logic
    right_up = True
    left_up = True
    run = True
    score = 0
    frame_count = 0

    while run:

        frame_count += 1
        seconds = frame_count/frame_rate
#IF PLAYER HAVE NITRO
        #if add_nitro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_LEFT:
                    x_change = -change_x
                    y_change = 0
                    right_up = False
                    left_up = True
                    up_up = False
                    down_up = False
                    x += x_change
                if event.key == pygame.K_RIGHT:
                    x_change = +change_x
                    y_change = 0
                    right_up = True
                    left_up = False
                    up_up = False
                    down_up = False
                    x += x_change
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -8
                    right_up = False
                    left_up = False
                    up_up = True
                    down_up = False
                    x += x_change
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 8
                    right_up = False
                    left_up = False
                    up_up = False
                    down_up = True
                    x += x_change
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and left_up == True:
                    x_change = 0
                if event.key == pygame.K_RIGHT and right_up == True:
                    x_change = 0
                if event.key == pygame.K_UP and up_up == True:
                    y_change = 0
                if event.key == pygame.K_DOWN and down_up == True:
                    y_change = 0

    #looping strip and hurdle management
        if strip_y > display_height:
            strip_y = -100
        if strip_y2 > display_height:
            strip_y2 = -100
        if strip_y3 > display_height:
            strip_y3 = -100

        if hurdle1_y > display_height:
            hurdle1_y = random.randint(-(display_height + 120*4), -120*4)
            score += 1
        if hurdle2_y > display_height:
            hurdle2_y = random.randint(-(display_height + 120*4), -120*4)
            score += 1
        if hurdle3_y > display_height:
            hurdle3_y = random.randint(-(display_height + 120*4), -120*4)
            score += 1
        if hurdle4_y > display_height:
            hurdle4_y = random.randint(-(display_height + 120 *4), -120*4)
            score += 1
        y += y_change
    #if there is nitro
        if add_nitro:
            strip_change = 16
            hurdle_change = 16
    ##    else :
        #    strip_change = 6
        #    hurdle_change = 4
        x2 = carImg.get_width() + x
        y2 = carImg.get_height() + y

        if score > 0 and score*10 % 50 == 0:
            strip_change += 0.01
            hurdle_change += 0.01

    #first line strip
        strip_y += strip_change
    #second line strips
        strip_y2 += strip_change
    #third line
        strip_y3 += strip_change
    #nitro change
        nitro_y += nitro_change

    #hurdle change
        hurdle1_y += hurdle_change
        hurdle2_y += hurdle_change
        hurdle3_y += hurdle_change
        hurdle4_y += hurdle_change
        hurdle1_y2 = hurdle1_y + hurdle_height
        hurdle2_y2 = hurdle2_y + hurdle_height
        hurdle3_y2 = hurdle3_y + hurdle_height
        hurdle4_y2 = hurdle4_y + hurdle_height

#if hurdles are toooo close:
        if (abs(hurdle1_y2 - hurdle2_y) < 120 or abs(hurdle1_y - hurdle2_y2) < 120) and (abs(hurdle2_y2 - hurdle3_y) < 120 or abs(hurdle2_y - hurdle3_y2) < 120) and (abs(hurdle3_y2 - hurdle4_y) < 120 or abs(hurdle3_y - hurdle4_y2) < 120):
            print("changing hurdles position as there is no place to cross")
            choice = random.choice([1,2,3])
            if choice == 1:
                if hurdle1_y2 > hurdle2_y:
                    hurdle1_y -= 120
                else :
                    hurdle1_y += 120
            elif choice == 2:
                if hurdle2_y2 > hurdle3_y:
                    hurdle2_y -= 120
                else :
                    hurdle2_y += 120
            elif choice == 3:
                if hurdle3_y2 > hurdle4_y:
                    hurdle3_y -= 120
                else :
                    hurdle3_y += 120

            hurdle1_y2 = hurdle1_y + hurdle_height
            hurdle2_y2 = hurdle2_y + hurdle_height
            hurdle3_y2 = hurdle3_y + hurdle_height
            hurdle4_y2 = hurdle4_y + hurdle_height

#if the user crashes the boundary
        if x >= strip3_x + (strip4_x - strip3_x)/2 - carImg.get_width()/2:
            x = strip3_x + (strip4_x - strip3_x)/2  - carImg.get_width()/2
        if x <= (strip1_x - strip_x)/2 - carImg.get_width()/2:
            x = (strip1_x - strip_x)/2 - carImg.get_width()/2
        if y <= 0:
            y = 0
        if y >= display_height - 100:
            y = display_height - 100

# if palyer crashes the huedle
        if (x > hurdle1_x and x < hurdle1_x2 and y > hurdle1_y and y < hurdle1_y2) or (x2 > hurdle1_x and x2 < hurdle1_x2 and y2 > hurdle1_y and y2 < hurdle1_y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (x > hurdle1_x and x < hurdle1_x2 and y2 > hurdle1_y and y2 < hurdle1_y2) or (x2 > hurdle1_x and x2 < hurdle1_x2 and y > hurdle1_y and y < hurdle1_y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (x > hurdle2_x and x < hurdle2_x2 and y > hurdle2_y and y < hurdle2_y2) or (x2 > hurdle2_x and x2 < hurdle2_x2 and y2 > hurdle2_y and y2 < hurdle2_y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (x > hurdle2_x and x < hurdle2_x2 and y2 > hurdle2_y and y2 < hurdle2_y2) or (x2 > hurdle2_x and x2 < hurdle2_x2 and y > hurdle2_y and y < hurdle2_y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (x > hurdle3_x and x < hurdle3_x2 and y > hurdle3_y and y < hurdle3_y2) or (x2 > hurdle3_x and x2 < hurdle3_x2 and y2 > hurdle3_y and y2 < hurdle3_y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (x > hurdle3_x and x < hurdle3_x2 and y2 > hurdle3_y and y2 < hurdle3_y2) or (x2 > hurdle3_x and x2 < hurdle3_x2 and y > hurdle3_y and y < hurdle3_y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (x > hurdle4_x and x < hurdle4_x2 and y > hurdle4_y and y < hurdle4_y2) or (x2 > hurdle4_x and x2 < hurdle4_x2 and y2 > hurdle4_y and y2 < hurdle4_y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (x > hurdle4_x and x < hurdle4_x2 and y2 > hurdle4_y and y2 < hurdle4_y2) or (x2 > hurdle4_x and x2 < hurdle4_x2 and y > hurdle4_y and y < hurdle4_y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
#IF HURDLE CROSSES car
        if (hurdle1_x < x2 and hurdle1_x > x and hurdle1_y > y and hurdle1_y < y2) or (hurdle1_x2 < x2 and hurdle1_x2 > x and hurdle1_y2 > y and hurdle1_y2 < y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (hurdle2_x < x2 and hurdle2_x > x and hurdle2_y > y and hurdle2_y < y2) or (hurdle2_x2 < x2 and hurdle2_x2 > x and hurdle2_y2 > y and hurdle2_y2 < y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (hurdle3_x < x2 and hurdle3_x > x and hurdle3_y > y and hurdle3_y < y2) or (hurdle3_x2 < x2 and hurdle3_x2 > x and hurdle3_y2 > y and hurdle3_y2 < y2):
            if not add_nitro:
                run = False
                game_over = True
            else:
                None
        elif (hurdle4_x < x2 and hurdle4_x > x and hurdle4_y > y and hurdle4_y < y2) or (hurdle4_x2 < x2 and hurdle4_x2 > x and hurdle4_y2 > y and hurdle4_y2 < y2):
            if not add_nitro:
                run = False
                game_over =  True
            else:
                None

#adding NItro PACK
        if score == 1:
            give_nitro = True
            add_nitro = False
            add_nitro_time = seconds
            nitro_x = random.choice([(strip1_x + strip2_x) / 2 - nitro_width/2, (strip2_x + strip3_x) / 2 - nitro_width/2, (strip3_x + strip4_x) / 2 - nitro_width/2, (strip1_x + strip_x) / 2 - nitro_width/2])
            nitro_y = random.randint(-display_height, -100)
            nitro_x2 = nitroImg.get_width() + nitro_x
            nitro_y2 = nitroImg.get_height() + nitro_y
            #if user gets nitro
            if x > nitro_x and x < nitro_x2 and y > nitro_y and y < nitro_y2:
                add_nitro = True
            elif x > nitro_x and x < nitro_x2 and y2 > nitro_y and y2 < nitro_y2:
                add_nitro = True

# prints stuff to the display are
    #prints road and car :- first line
        gameDisplay.fill(road_colour)
        pygame.draw.rect(gameDisplay, white, [strip1_x, strip_y, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip2_x, strip_y, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip3_x, strip_y, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip4_x, strip_y, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip_x, strip_y, 10, 100])
    #second line
        pygame.draw.rect(gameDisplay, white, [strip1_x, strip_y2, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip2_x, strip_y2, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip3_x, strip_y2, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip4_x, strip_y2, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip_x, strip_y2, 10, 100])
    #third line
        pygame.draw.rect(gameDisplay, white, [strip1_x, strip_y3, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip2_x, strip_y3, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip3_x, strip_y3, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip4_x, strip_y3, 10, 100])
        pygame.draw.rect(gameDisplay, white, [strip_x, strip_y3, 10, 100])
    #displaying hurdle in the way , car and nitro pack
        enemy_car(hurdle1_x, hurdle1_y)
        enemy_car(hurdle2_x, hurdle2_y)
        enemy_car(hurdle3_x, hurdle3_y)
        enemy_car(hurdle4_x, hurdle4_y)

        if give_nitro:
            nitro(nitro_x, nitro_y)

        car(x, y)
    #prints boundaris
        pygame.draw.rect(gameDisplay, black, [0, 0, display_width, 3])
        pygame.draw.rect(gameDisplay, black, [0, 0, 6, display_height])
        pygame.draw.rect(gameDisplay, black, [0, display_height, display_width, -3])
        pygame.draw.rect(gameDisplay, black, [display_width, display_height, -3, -display_height])
        score_bg_print(0, display_height)
        message(f"score : {score * 10}", black, display_height/2 + score_display_height/2, 25, -(display_width/2 - 60))
        if add_nitro:
            time_passed = seconds - add_nitro_time
            if time_passed <= 10:
                message(f"Nitro time remaining : {10 - (round(time_passed))}", red, display_height/2 + (score_display_height / 2), 20, 200)
            else:
                add_nitro = False
        pygame.display.update()
        clock.tick(frame_rate)

    while game_over :
        gameDisplay.fill(black)
        message("GAME OVER", red, -100, 80)
        message(f"Your score : {score * 10}", green, 0, 40)
        mouse_pos = pygame.mouse.get_pos()
        play_clicked = button("play again", red, -150, 100, 40, green, mouse_pos)
        exit_clicked = button("Exit", blue, 150, 100, 40, red, mouse_pos)
        display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                run = False
                pygame.quit()

        if play_clicked:
            game_over = False
            game_loop()
        elif exit_clicked:
            game_over = False
            run = False
            pygame.quit()

main_menu()
pygame.quit()
quit()
