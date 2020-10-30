#Źródło problemu: https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
#Twórca rozwiązania: Aleksandra Formela; s17402

import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

position_x, position_y = initial_tx, initial_ty

while 1:
    remaining_turns = int(input())
    
    direction = ""
    
    if position_y > light_y:
        direction += "N"
        position_y -= 1
    elif position_y < light_y:
        direction += "S"
        position_y += 1

    if position_x > light_x:
        direction += "W"
        position_x -= 1
    elif position_x < light_x:
        direction += "E"
        position_x += 1
        
    print(direction)

