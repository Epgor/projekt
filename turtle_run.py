import turtle
import numpy as np
import random
import draw_lines

LIVE = 40 #żywotność

wartosci = [20, 3000]
wagi = [1, 20]
#tworzę odpowiadające sobie macierze wag i cen
values = [[random.randint(wartosci[0], wartosci[1]) for x in range(20)] for y in range(20)]
weights = [[random.randint(wagi[0], wagi[1]) for x in range(20)] for y in range(20)]
#to do, eksport generatora do oddzielnego pliku
values_ = np.asarray(values)
weights_ = np.asarray(weights)

knapsack = 0
for x in weights_: #wartość plecak ustalana by dobrze badać zachowanie algorytmu
    knapsack += sum(x)
knapsack = knapsack/100 #duży plecak, jako 1/100 sumy wag


print(knapsack)

#screen = turtle.getscreen()
turtley = turtle.Turtle()
turtle.screensize(canvwidth=1000, canvheight=1000)
turtley.shape('turtle')
#turtley.up()
turtley.lt(90)
turtley.up()
turtley.goto(0, -320) #początek labiryntu, jako dół
turtley.down()
pos = [9, 0]
n_pos = [9, 0]
"""
    turtley.fd(100)

    turtley.lt(90)

    turtley.bk(100)

    turtley.goto(-100,-100)

    screen.bgcolor("orange")
    input("xd")"""
def overweight(tabu):
    temp = 0
    for x in tabu:
        temp += weights_[x[0]][x[1]]
    if temp >= knapsack:
        return True
    return False

def borders(x, y):
    if x < 0 or x >=20:
        return False
    if y < 0 or y >= 20:
        return False
    return True

def best_neigh(pos, tabu): #no look back
    x,y = pos[0], pos[1]
    temp_x, temp_y = x, y+1
    if borders(temp_x, temp_y):
        if borders(temp_x-1, temp_y):
            if values_[x-1][y] >= values_[temp_x][temp_y]:
                if [x-1, y] not in tabu:
                    temp_x, temp_y = x-1, y
                    move_turtle([temp_x, temp_y])
                    tabu.append([temp_x, temp_y])
                    return tabu
        if borders(temp_x+1, temp_y):
            if values_[x+1][y] >= values_[temp_x][temp_y]:
                if [x+1, y] not in tabu:
                    temp_x, temp_y = x+1, y
                    move_turtle([temp_x, temp_y])
                    tabu.append([temp_x, temp_y])
                    return tabu
        if [temp_x, temp_y] not in tabu:
            move_turtle([temp_x, temp_y])
            tabu.append([temp_x, temp_y])
            return tabu
    else:
        temp_x, temp_y = x, y-1
        move_turtle([temp_x, temp_y])
        return tabu

def move_turtle(new_position):
    turtley.goto((new_position[0]-9)*40,(new_position[1]-9)*40)

def demo():
    #values = [[0 for x in range(20)] for y in range(20)]
    #weigths = [[0 for x in range(20)] for y in range(20)]
    position = [10,10]
    new_position = [10,10]
    tabu = []

    for x in range (10):
        new_position = [position[0]+random.randint(-1,1),position[1]+random.randint(-1,1)]
        tabu.append(new_position[:])
        move_turtle(new_position)
        position = new_position[:]



    print(tabu)
    print(position)
    print(new_position)
    input("Press any key...")


#position = [9,9] #pozycja startowa jako środek 




"""for x,_ in enumerate(values):
    for y,__ in enumerate(values[0]):
        values[x][y] = 2"""
""""""
"""for x in values:
    print(x)

for x in weigths:
    print(x)

print(values_[0][0])
"""

tabu = []
tabu.append(pos[:])

for x in range(LIVE):
    tabu = best_neigh(pos, tabu)
    pos = tabu[len(tabu)-1]
    while overweight(tabu):
        tabu.pop(0)

#pos = n_pos[:]

print("Pozycja końcowa")
print(pos)
print("Tablica:")
print(tabu)
for i, x in enumerate(tabu):
    print('Item {: d}:'.format(i+1))
    val = values_[x[0]][x[1]]
    print("Value: {: d}".format(val))
    wei = weights_[x[0]][x[1]]
    print("Weight: {: d}".format(wei))


input("Press any key...")