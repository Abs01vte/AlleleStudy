#!/usr/bin/env python

class Mates:
    def __init__(self, atr1, atr2) :
        self.atr1 = atr1
        self.atr2 = atr2
    def __repr__(self):
        return self.atr1 + self.atr2
    def __str__(self):
        return "Mates"

matelist = []

with open('genes.txt') as f:
    contents = f.readlines()
    for line in contents :
        atrs = line.split()
        matelist.append(Mates(atrs[0], atrs[1]))
        print(atrs)
    print(matelist)
