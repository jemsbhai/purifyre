import pygame
import time
import random
import serial


ser = serial.Serial('/dev/ttyACM0', 115200)

# ser = serial.Serial('COM24', 115200)


print ("connected to: " + ser.portstr)

serialmsg = b''
 
pygame.init()
 
display_width = 750
display_height = 400
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
car_width = 73
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Purifyre')
clock = pygame.time.Clock()

def quitgame():
    pygame.quit()
    ser.flush()
    ser.write(b'o')
    ser.close()
    quit()

def send_messageU():
    ser.flush()
    ser.write(b'U')
    ser.write(b'\n')
    

def send_messageu():
    ser.flush()
    ser.write(b'u')
    ser.write(b'\n')

def send_messageH():
    ser.flush()
    ser.write(b'H')

def send_messageh():
    ser.flush()
    ser.write(b'h')


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def main_loop():

    mainloop = True

    while mainloop:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Purify", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        

        button("UV on",0,275,100,50,green,bright_green,send_messageU)
        button("UV off",150,275,100,50,green,bright_green,send_messageu)
        button("Heater on",300,275,100,50,green,bright_green,send_messageH)
        button("Heater off",450,275,100,50,green,bright_green,send_messageh)
        button("Quit",600,275,100,50,red,bright_red,quitgame)
        

        
        pygame.display.update()
        clock.tick(15)




main_loop()
pygame.quit()
ser.close()
quit()
        
