import pygame

pygame.init() # it means , pygame will init all modules that is in pygame..

pygame.display.set_mode((800, 200)) # window - pygame ki korbe set korbe display, then set mode - 111,222 ..!
pygame.display.set_caption("Shubha Game") #set_caption caption to set caption

exit_game = False
game_over = False
#when they will be true the game will be end..

#fix window
#creating a gaming loop

while not exit_game:
    #create a event that will handel out event or order on game
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN: # KEYDOWN means press any key, now what key pressed that i wll decide
            if event.key == pygame.K_a: # here event type is someone press a key, that here is command
                print("You entered a key..")


        if event.type == pygame.QUIT: #here game quit command ,
            exit_game = True

#pygame quit
pygame.quit()
#python quit
quit()