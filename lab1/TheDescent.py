#Źródło problemu: https://www.codingame.com/ide/puzzle/the-descent
#Twórca rozwiązania: Aleksandra Formela; s17402

import sys
import math

while True:
    maxId = -1
    maxValue = -1
    for i in range(8):
        mountain_h = int(input())  
        if mountain_h > maxValue:
            maxId = i
            maxValue = mountain_h

    print(maxId)