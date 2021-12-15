from read_file import FileOperator
from greedy_alg import greed, ladny_print
import numpy as np

def mark(data):
    tab = []
    raw = data.get().tolist()
    for x,y in enumerate(raw):
        tab.append(int(raw[x][2]) / int(raw[x][1]))
    for x,y in enumerate(tab):
        raw[x].append(y)
    return raw

dane = FileOperator("GreedyKnapsack")

dane.default()
zocenami = mark(dane)

ladny_print(zocenami)

answer = greed(11, zocenami)

print("Wybrane opcje:")
ladny_print(answer[1])
print(f"Zużyto całą pulę ")\
        if answer[0] == 0 \
            else  print(f"Pozostało {answer[0]} kg")


