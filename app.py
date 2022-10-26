# from ast import main
# from distutils.log import debug
# from flask import Flask, json

from flask import Flask, jsonify
import random

app = Flask(__name__)

class GA:
    def __init__(self):
        self.population = []
        i = 1
        while i <= 40:
            self.population.append(i)
            i= i+1

        print(i)

        # while i < populationSize:
        #     listOfBits = [0] * individualSize
        #     listOfLocations = list(range(0, individualSize))
        #     numberOfOnes =  random.randint(0, individualSize - 1)
        #     onesLocations = random.sample(listOfLocations, numberOfOnes)
        #     for j in onesLocations:
        #         listOfBits[j] = 1
        #         self.population[i] = [listOfBits, numberOfOnes]
        #         self.totalFitness = self.totalFitness + numberOfOnes
        #         i = i+1

    # def updatePopulationFitness(self):
    #         self.totalFitness = 0
    #         for individual in self.population:
    #             individualFitness = sum(self.population[individual])
    #             self.population[individual] = individualFitness
    #             self.totalFitness = self.totalFitness + individualFitness


    

    def generateChildren(self,h_n):
                rand = []

                i = 0
                k=1
                while i<=39:
                    rand.append(k)
                    i = i+1
                    k=k+1

                random.shuffle(rand)
                randomNumber = random.randint(1, 5)
                guesser = random.randint(1, 5)

                j = 0
                while j<= 24:
                    if(randomNumber == guesser) :
                        h_n[j] = rand[j]

                    guesser = random.randint(1, 5)
                    randomNumber = random.randint(1, 5)
                    j=j+1

                return h_n

    def selectParents(self):
            rouletteWheel = []
            j = 0
            while j<= 59:
                rouletteWheel.append(self.population[j])
                print(j)
                j = j+1

            random.shuffle(rouletteWheel)
            h_n = []
            k = 0
            while k<=24:
                h_n.append(rouletteWheel[k])
                k=k+1
            return h_n

            # generateChildren(h_n)


# individualSize, populationSize = 8,10



@app.route("/", methods=['GET'])
def app():
    instance = GA()
    arr = instance.selectParents()
    print(arr)
    finalArr = instance.generateChildren(arr)

    return jsonify(finalArr)


if __name__ == "__main__":
    app.run(port=1000)
