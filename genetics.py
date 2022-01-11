#!/usr/bin/env python

#class of individuals for carrying markers
class Mates:
    def __init__(self,atr1: str, atr2: str) :
        self.atr1 = atr1
        self.atr2 = atr2
    def __repr__(self):
        return self.atr1 + self.atr2
    def __str__(self):
        return "Mates"

#the list holding the originals
gen0 = []

#reading the files of the atribute markers
with open('genes.txt') as f:
    contents = f.readlines()
    for line in contents :
        atrs = line.split()
        gen0.append(Mates(atrs[0], atrs[1]))
        print(atrs)
    print(gen0)

#the five generations generated
gen1 = []
gen2 = []
gen3 = []
gen4 = []
gen5 = []

def generateGeneration(lastGen: []) -> []:
    nextGen = []
    for i in range(len(lastGen)-1):
        parent1 = lastGen[i]
        parent2 = lastGen[i+1]

        nextGen.append(Mates(parent1.atr1, parent2.atr1))
        nextGen.append(Mates(parent1.atr2, parent2.atr1))
        nextGen.append(Mates(parent1.atr1, parent2.atr2))
        nextGen.append(Mates(parent1.atr2, parent2.atr2))
    parent1 = lastGen[-1]
    parent2 = lastGen[0]
    nextGen.append(Mates(parent1.atr1, parent2.atr2))
    nextGen.append(Mates(parent1.atr1, parent2.atr1))
    nextGen.append(Mates(parent1.atr2, parent2.atr2))
    nextGen.append(Mates(parent1.atr2, parent2.atr1))

    return nextGen
gen1=generateGeneration(gen0)
print (gen1)
gen2=generateGeneration(gen1)
print(gen2)
gen3=generateGeneration(gen2)
print(gen3)
gen4=generateGeneration(gen3)
print(gen4)
gen5=generateGeneration(gen4)
print(gen5)
