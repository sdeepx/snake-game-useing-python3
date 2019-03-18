import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0, 0)
c1 = (200,200,200)
c2 = (200, 166, 0)
c3 = (100, 244, 200)
c4 = (180, 255, 120)
screen_w = 600
screen_h = 600

#game display
window = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption("Sanke Game by DeepGame")
pygame.display.update()

# font
font = pygame.font.SysFont(None, 50)
font1 = pygame.font.SysFont(None, 40)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])

def text_screen1(text, color, x, y):
    screen_text = font1.render(text, True, color)
    window.blit(screen_text, [x, y])

def snk_plot(window, color, snk_list, Ssize):
    for x,y in snk_list:
        pygame.draw.rect(window, color, [x,y, Ssize, Ssize])

#welcome screen
def welcome():

    clock = pygame.time.Clock()
    exit_game = False
    while not exit_game:
        window.fill(c1)
        text_screen("Welcome to Snake Game", red, 100,200)
        text_screen1("Powered by DeepGame", red, 250,240)
        text_screen("Press Enter to Continue", red, 90,350)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()

        pygame.display.update()

        clock.tick(30)


def game_loop():
    # color
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0, 0)
    c2 = (0,0,222)
    c3 = (100,244,200)
    c4 = (1,5,2)
    c5 = (30,40,50)

    snake_x = 50
    snake_y = 100
    Ssize = 15
    Fsize = random.randint(10,15)
    exit_game = False
    game_over = False
    fps = 30
    volocity_x = 0
    volocity_y = 0
    score = 0

    snk_list = []
    snk_lenth = 1

    food_x = random.randint(50, 500)
    food_y = random.randint(50, 500)

    clock = pygame.time.Clock()  # to update our game accoding to time

    with open("high_s", "r") as f:
        high_s = f.read()


    #game loop
    while not exit_game:

        if game_over:
            clock.tick(.80)
            with open("high_s", "w") as f:
                f.write(str(high_s))
            window.fill(c4)

            text_screen("High Score: " + str(high_s), red, 150, 140)
            text_screen("Your Score: " + str(score), red, 100, 100)
            text_screen1("GAME OVER! Press Enter to Continue", red, 20, 250)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    quit()

        else:
            for event in pygame.event.get(): #evant
                #movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        volocity_x = 5
                        volocity_y = 0

                    if event.key == pygame.K_LEFT:
                        volocity_x = -5
                        volocity_y = 0

                    if event.key == pygame.K_UP:
                        volocity_y = -5
                        volocity_x = 0

                    if event.key == pygame.K_DOWN:
                        volocity_y = 5
                        volocity_x = 0

                if event.type == pygame.QUIT:
                    exit_game = True

            snake_y += volocity_y
            snake_x += volocity_x

            #changing food position and score value
            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:

                #to change food positions again
                food_x = random.randint(50, 400)
                food_y = random.randint(50, 400)
                Fsize = random.randint(13, 17)

                score += random.randint(2,7)
                if score > 150:
                    score += random.randint(5,10)
                if score > 250:
                    score += random.randint(8,10)
                    snk_lenth += 3

                snk_lenth +=4

            if score > int(high_s):
                high_s = score

            window.fill(c3) #change display
            text_screen("Score: " + str(score ) + "                  High score :"+ str(high_s), red, 5, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenth:
                del snk_list[0]

            if head in snk_list[:-1]:
                text_screen1("OOPS! Snake is Dead", red, 200, 200)
                game_over = True

            if snake_x < 0 or snake_x > screen_w or snake_y < 0 or snake_y > screen_h:
                text_screen1("OOPS! Snake is Dead", red, 200,200)
                game_over = True

            #pygame rectangle, drawing snake's head,,
            #draw a food
            pygame.draw.rect(window, c2, [food_x, food_y, Fsize, Fsize])
            snk_plot(window, black, snk_list, Ssize)

        pygame.display.update() #update display

        clock.tick(fps) # here def 30 frame / 1 sec
        if score > 50:
            fps = 35
        if score > 100:
            fps = 40
        if score > 150:
            fps = 45
        if score > 200:
            fps = 50
        if score > 300:
            fps = 60

    pygame.quit()
    quit()

welcome()
game_loop()
