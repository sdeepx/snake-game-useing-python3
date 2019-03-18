import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0, 0)
c1 = (200,200,200)
screen_w = 600
screen_h = 600

#game start from here
#game dis
window = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption("Sanke Game by DeepGame")
pygame.display.update()

# font
font = pygame.font.SysFont(None, 50)  # create a font thats text size = 55
font1 = pygame.font.SysFont(None, 40)

def text_screen(text, color, x, y): #here i def that , i want to print a text on the screen , the text and its color and where i put that..
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y]) # update the screen


def text_screen1(text, color, x, y): #here i def that , i want to print a text on the screen , the text and its color and where i put that..
    screen_text = font1.render(text, True, color)
    window.blit(screen_text, [x, y]) # update the screen




def snk_plot(window, color, snk_list, Ssize):
    for x,y in snk_list:
        pygame.draw.rect(window, color, [x,y, Ssize, Ssize])


#welcome screen
def welcome():

    clock = pygame.time.Clock()
    exit_game = False
    while not exit_game: #from PIL import Image
# jpgfile = Image.open("picture.jpg")
#
# print(jpgfile.bits, jpgfile.size, jpgfile.format)

        # with Image.open("shubha.jpg", "r") as f:
        #     f.read("shubha.jpg")

        window.fill(c1)
        text_screen1("Welcome to snake game. by DeepGame", red, 10,140)
        text_screen1("Press Enter to continue", red, 20,250)
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

    # game variabls
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
            with open("high_s", "w") as f:
                f.write(str(high_s))

            window.fill(black)
            text_screen("Your High Score: " + str(high_s), red, 150, 140)
            text_screen("GAME OVER! Enter to Continue", red, 20,250)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
                if event.type == pygame.QUIT:
                    exit_game = True


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

                if Fsize > 15:
                    score += random.randint(5, 7)
                else:
                    score += random.randint(2,4)

                snk_lenth +=4 # jei food khabe sei boro hobe

            if score > int(high_s):
                high_s = score

            window.fill(white) #change display
            text_screen("Score: " + str(score ) + "  High score :"+ str(high_s), red, 5, 5)


            head = [] #head basically emty now but it will be snk head..
            head.append(snake_x) #that we draw in pygame.draw.rect(window, black,[snake_x, snake_y, Ssize, Ssize]) here, but need to change,,
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenth:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_w or snake_y < 0 or snake_y > screen_h:
                game_over = True

            #pygame rectangle, drawing snake's head,,
            #draw a food
            pygame.draw.rect(window, red, [food_x, food_y, Fsize, Fsize])
            snk_plot(window, black, snk_list, Ssize)  # snake_x or y means the snake where stay from frame
            #snk_list head = snake_x and y

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
