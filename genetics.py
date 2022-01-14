#!/usr/bin/env python

import sys
import copy

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# This takes in a set of allele pairs that are put into a file and breaks them down into individuals called Mates
# each Mate is paired with one of the other ones of a similar generation to make the next generations
# each pair makes 4 new objects, one for each combination on a punnett square
# then the whole collection is compared to see how many are the same combination of alleles
# in order to determine where genetic code would mutate.

#class of individuals for carrying markers
class Mates:
    def __init__(self,atr1: str, atr2: str) :
        if atr2.isupper():
             self.atr2 = atr1
             self.atr1 = atr2
        else:
            self.atr1 = atr1
            self.atr2 = atr2
        self.count=0

    def __repr__(self):
        return self.atr1 + self.atr2 + ": " + str(self.count)
    def __str__(self):
        return self.atr1 + self.atr2 + ": " + str(self.count)
    def countUp(self):
        self.count+=1
    def __eq__(self, other):
        return self.atr1+self.atr2 == other.atr1+other.atr2
    def printOut(self):
        if self.count>1:
            print(self)
    def  __lt__(self, other):
        if self.atr1.islower():
            if self.atr1 < other.atr1.lower():
                return True
            return False
        if other.atr1.islower():
            if other.atr1 < self.atr1.lower():
                return False
            return True
        if self.atr1 < other.atr1 and self.atr2 < other.atr2:
            return True
        if self.atr1 < other.atr1:
            return True

        return False


#holder of the generations
generations = []
generations.append([])
uniqueMates = []


def incrementMate(mate: Mates):
    for each in uniqueMates:
        if each == mate:
            each.countUp()
            return
    mate.countUp()
    uniqueMates.append(mate)

# counts the number of similarities to previous generations

def compareGens(genIndex: int):
    genI = copy.deepcopy(generations[genIndex])
    genPrev = copy.deepcopy(generations[genIndex-1])
    for m in reversed(genI):
        for m2 in reversed(genPrev):
            if m == m2:
                incrementMate(m)
                genPrev.remove(m2)
        genI.remove(m)



# produces new generations based on the allele pairs of two parents from the previous generation
def generateGeneration(lastGen: []) -> []:
    nextGen = []
    for i in range(len(lastGen)-1):
        parent1 = lastGen[i]
        parent2 = lastGen[i+1]

        nextGen.append(Mates(parent1.atr1, parent2.atr1))
        nextGen.append(Mates(parent1.atr1, parent2.atr2))
        nextGen.append(Mates(parent1.atr2, parent2.atr1))
        nextGen.append(Mates(parent1.atr2, parent2.atr2))

    parent1 = lastGen[-1]
    parent2 = lastGen[0]
    nextGen.append(Mates(parent1.atr1, parent2.atr1))
    nextGen.append(Mates(parent1.atr1, parent2.atr2))
    nextGen.append(Mates(parent1.atr2, parent2.atr1))
    nextGen.append(Mates(parent1.atr2, parent2.atr2))


    return nextGen

def organize():
    uniqueMates.sort()


numGenerations = 5
genesFile = "genes.txt"

for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    argc = len(sys.argv) - 1
    match arg:
        case "--num-gens":
            if i == argc:
                raise ValueError("No number given for --num-gens")
            numGenerations = int(sys.argv[i + 1])
        case "--file":
            if i == argc:
                raise ValueError("No file path given for --file")
            genesFile = sys.argv[i + 1]


#reading the files of the atribute markers
with open(genesFile) as f:
    numLinesFile = 0
    contents = f.readlines()
    for line in contents :
        atrs = line.split()
        numLinesFile+=1
        generations[0].append(Mates(atrs[0], atrs[1]))


for i in range(numGenerations):
    generations.append(generateGeneration(generations[-1]))


for i in range(1,len(generations)):
    compareGens(i)

organize()

for mate in uniqueMates:
    mate.printOut()

# compares the number of repeats represented by uniqueMates to the total number of all mates in the list generations
repeats = 0
total = 0
for mate in uniqueMates:
    repeats += mate.count
for generation in generations:
    total += len(generation) -1
print("Out of " + str(total) + "there are " + str(repeats) + "repeats.")
print("The percentage of repeats is: " + "{:.2f}".format(float(repeats)/float(total)*100) + "%")
print("The average possible is: {}".format((numLinesFile*2)*(numGenerations)))
