#!/usr/bin/env python

#class of individuals for carrying markers
class Mates:
    def __init__(self,atr1: str, atr2: str) :
        self.atr1 = atr1
        self.atr2 = atr2
        self.count=0
    def __repr__(self):
        return self.atr1 + self.atr2
    def __str__(self):
        return "Mates"
    def countUp(self):
        self.count+=1

generations = []
generations.append([])

#reading the files of the atribute markers
with open('genes.txt') as f:
    contents = f.readlines()
    for line in contents :
        atrs = line.split()
        generations[0].append(Mates(atrs[0], atrs[1]))
        print(atrs)
    print(generations[0])



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

for i in range(5):
    generations.append(generateGeneration(generations[-1]))
print(generations)

#def
