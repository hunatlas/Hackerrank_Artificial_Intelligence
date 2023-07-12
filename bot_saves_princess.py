#!/usr/bin/python

import math

def displayPathtoPrincess(n,grid):
    
    iteratorIndex = 0
        
    for row in grid:
        for character in row:
            if character == "m":
                botIndex = iteratorIndex
            elif character == "p":
                princessIndex = iteratorIndex
            iteratorIndex += 1
    
    while(botIndex != princessIndex):
        if(math.floor(botIndex / m) < math.floor(princessIndex / m)):
            print("DOWN")
            botIndex += m
        elif(math.floor(botIndex / m) > math.floor(princessIndex / m)):
            print("UP")
            botIndex -= m
        elif(math.floor(botIndex / m) == math.floor(princessIndex / m)):
            if(botIndex < princessIndex):
                print("RIGHT")
                botIndex += 1
            elif(botIndex > princessIndex):
                print("LEFT")
                botIndex -= 1

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
