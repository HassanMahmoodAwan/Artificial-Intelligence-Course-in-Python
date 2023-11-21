import random
import math



class GA:
    def __init__ (self, individualSize, populationSize):
        self.population=dict()
        self.individualSize = individualSize
        self.populationSize = populationSize
        self.totalFitness=0





    
    i=0
    while i < populationSize:
        listofBits = [0] * individualSize
        listOfLocations = list (range (0, individualSize))
        numberOfOnes = random.randint (0, individualSize-1)
        onesLocations = random. sample (listOfLocations, numberOfOnes)
        for j in onesLocations:
            listofBits [j] =1
            self.population[i]=[listOfBits, numberOfOnes]
            self.totalFitness = self.totalFitness + numberOfOnes
            i=i+1


    def updatePopulationFitness (self):
        self.totalFitness = 0
        
        for individual in self.population:
            individualFitness = sum(self.population[individual][0])
            self.population[individual][1] = individualFitness
            self.totalFitness = self.totalFitness + individualFitness



if __name__ == '__main__':
    pass
    



    