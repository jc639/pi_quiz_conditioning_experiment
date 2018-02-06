import pygame
from true_false import q_a
import random
from pygame.locals import *
from sys import exit
from math import ceil
import RPi.GPIO as GPIO
import time

# define question and answer
question = [q[0] for q in q_a]
answer = [a[1] for a in q_a]

# Set the gpio pins according to broadcom numbers
GPIO.setmode(GPIO.BCM)

# left is on 4, right on 17
left_but = 4
right_but = 17

# Set them up with pull up resistor, pulls floating input high
# will go low when switch is pressed and connects it to GND
GPIO.setup(left_but, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(right_but, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# set white background, and 1/3 of screen size
plain_background = (255,255,255)
screen_width = round(1920*0.3)
screen_height = round(1080*0.3)

# initialise pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(plain_background)

# function to split questions over several lines if they are long
def line_split(line, char_per_line):
    n_lines = ceil(len(line) / char_per_line)
    if n_lines == 1:    
        return([line])
    else:
        n_words = len(line.split())
        n_words_p_line = ceil(n_words / n_lines)
        lines = []
        for i in range(0, n_lines, 1):
            if i == (n_lines - 1): 
                lines.append(" ".join(line.split()[i*n_words_p_line:]))
            else :
                lines.append(" ".join(line.split()[i*n_words_p_line:(i+1)*n_words_p_line]))

        return(lines)

        
# update the question being displayed    
def question_update(index):
    global question
    ques = question[index]
    q = line_split(ques, 40)

    line_y = 20
    for lines in q:
        q_font = pygame.font.SysFont('monospace', 18, bold=True)
        text = lines
        size, ignore = q_font.size(text)
        line = q_font.render(text, 1, (153, 0, 0))
        screen.blit(line, ((screen_width/2) - (size/2), line_y))
        line_y += q_font.get_linesize()           
        

# put True/ False on certain sides
def answer_update(index):
    global answer
    curr_ans = answer[index]

    if index < 75:
        left_ans = 'True'
        right_ans = 'False'
    elif 75 <= index < 125:
        left_ans = 'False'
        right_ans = 'True'
    else:
        if random.randint(0,1) == 1:
            left_ans = 'True'
            right_ans = 'False'
        else:
            left_ans = 'False'
            right_ans = 'True'
            

    # set answer font
    ans_font = pygame.font.SysFont('monospace', 20, bold=True)
    # place left answer left
    left_text = ans_font.render(left_ans, 1, (79,181,207))
    screen.blit(left_text, (round(0.2*screen_width), round(0.5*screen_height)))
    # place right answer on the right
    right_text = ans_font.render(right_ans, 1, (79,181,207))
    screen.blit(right_text, (round(0.7*screen_width), round(0.5*screen_height)))

    pygame.display.update()
    
    # while loop continuous until button pressed by user
    ans = None
    while ans is None:
        if GPIO.input(left_but) == 1:
            ans = left_ans[0]
            time.sleep(0.1)
        elif GPIO.input(right_but) == 1:
            ans = right_ans[0]
            time.sleep(0.1)
        
    # check selected answer against correct and display
    corr_font = pygame.font.SysFont('monospace', 30)
    if ans == curr_ans:
        pygame.time.delay(100)
        screen.fill(plain_background)
        text = 'CORRECT!'
        corr_message = corr_font.render(text, 1, (58,207,88))
        screen.blit(corr_message, (round(0.4*screen_width), round(0.45*screen_height)))
        pygame.display.update()
        time.sleep(1)
    else:
        pygame.time.delay(100)
        screen.fill(plain_background)
        text = 'INCORRECT!'
        corr_message = corr_font.render(text, 1, (207,6,6))
        screen.blit(corr_message, (round(0.3*screen_width), round(0.45*screen_height)))
        pygame.display.update()
        time.sleep(1)

    del ans

# for displaying messages
def display_message(text):
    message = line_split(text, 40)
    line_y = 100
    for lines in message:
        message_font = pygame.font.SysFont('monospace', 16, bold=True)
        text = lines
        size, ignore = message_font.size(text)
        line = message_font.render(text, 1, (153, 0, 0))
        screen.blit(line, ((screen_width/2) - (size/2), line_y))
        line_y += message_font.get_linesize()
    pygame.display.update()
    pygame.time.delay(10000)
    screen.fill(plain_background)
    pygame.display.update()
    

    
# main loop                    
try:
    idx = 0
    while idx < len(question):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                del question, answers, correct_answer
                GPIO.cleanup()
                exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    del question, answers, correct_answer
                    GPIO.cleanup()
                    exit()

        if idx == 75:
            display_message('True and False will now switch sides')
        if idx == 125:
            display_message('True and False will now be on random sides')

        
        question_update(idx)
        answer_update(idx)
        pygame.display.update()
        
        screen.fill(plain_background)
        pygame.display.update()
        idx += 1

    screen.fill(plain_background)
    pygame.display.update()
    del question, answer
    time.sleep(30)
    GPIO.cleanup()
    pygame.quit()
    exit()

except KeyboardInterrupt:
    GPIO.cleanup()
    pygame.quit()
    exit()

