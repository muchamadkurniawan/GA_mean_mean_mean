import random
import numpy as np
import numpy.random as rnd
import math

from matplotlib import pyplot as plt

class gen:
    __nfeature = None
    __ncluster = None
    __bound = None
    position = []
    fitness = 0
    
    def __init__(self, nfeature,ncluster, bound=None):
        self.__nfeature = nfeature
        self.__ncluster=ncluster
        self.__bound = bound
        self.__initPosition()

    def __initPositionNoBound(self):
        gen = []
        for i in range(self.__ndim):
            gen.append(random.random())
        return gen

    def __initPositionBound(self):
        gen = []
        for j in range(self.__ncluster):
            for i in range (self.__nfeature):
                min = self.__bound[i][0]
                max = self.__bound[i][1]
                # print(min,max)
                dna = np.random.uniform(low=min, high=max, size=(1))
                # print(dna.tolist())
                dna = dna.tolist()
                gen.append(dna[0])
        gen = np.array(gen)
        return gen
        # print("GEN", gen)
        # print("woiii ini ", gen.shape)
        # print(ind.shape)
        # mini = self.__bound[0]
        # maxi = self.__bound[1]
        # for i in range(self.__ndim):
        #     ind = random.randint(mini, maxi-1)
        #     gen.append(ind)
        # return gen

    def __initPosition(self):
        self.position = self.__initPositionBound()

    def viewPosition(self):
        print(self.position)

class GA:
    nPop = None
    pop = None
    nDim = 0
    bound = None
    function = None
    bestInd = None
    bestFitness = 0
    loop = 0
    nElit = 0
    newpop = []
    fitness = []
    nCluster = 0
    nfeature = 0
    X = []
    y = []

    def __init__(self, nPop, ncluster, dim, max_itarasi,Cr,Mr, X, y, Function=None):
        self.loop = max_itarasi
        self.nPop = nPop
        self.nCluster = ncluster
        self.nfeature = dim
        self.nDim = ncluster*dim
        self.function = Function
        self.X = X
        self.y = y
        self.mainAlgorithm(Cr, Mr)

    def initPosition(self):
        swarm = []
        # print("BOOND", self.bound)
        bon = []
        for i in range (len(self.X[0])):
            bin = []
            bin.append(min(self.X[i]))
            bin.append(max(self.X[i]))
            bon.append(bin)
        bond = np.array(bon)
        self.bound = bond
        for i in range(self.nPop):
            swarm.append(gen(self.nfeature,self.nCluster, bound=self.bound))
        self.pop = swarm

    def viewPosition(self):
        for i in range(self.nPop):
            print("no :", i, ": ",self.pop[i].position)
    
    def calFitness(self):
        for i in range(self.nPop):
            # print("shape individu: ",len(self.pop[i].position))
            # print("CLUSTER ", i , self.nCluster, self.nfeature)
            # print("len position ", len(self.pop[i].position))
            arr_2d = np.reshape(self.pop[i].position,(
                self.nCluster, self.nfeature))
            fit = (self.function.fitness2(arr_2d, self.X))
            self.pop[i].fitness = fit
    
    def viewFitness(self):
        for i in range(self.nPop):
            print("fitness : ", self.pop[i].fitness)
            
    def getGbest(self):
        i = self.__findGbestMin()
        self.bestInd = self.pop[i].position
        self.bestFitness = self.pop[i].fitness
    
    def __findGbestMax(self):
        mini = self.pop[0].fitness
        index = 0
        for i in range(self.nPop):
            # print("GGG ", self.pop[i].fitness)
            if self.pop[i].fitness > mini:
                index = i
                mini = self.pop[index].fitness
        return index

    def __findGbestMin(self):
        mini = self.pop[0].fitness
        index = 0
        for i in range(self.nPop):
            # print("GGG ", self.pop[i].fitness)
            if self.pop[i].fitness < mini:
                index = i
                mini = self.pop[index].fitness
        return index

    def __selec_turnamen(self):
        selec = np.random.randint(self.nPop)
        for xi in np.random.randint(0,self.nPop,3):
            if self.pop[xi].fitness < self.pop[selec].fitness:
                selec = xi
        return self.pop[selec].position

    def pickParent(self):
        selected = [self.__selec_turnamen() for _ in range(self.nPop)]
        return selected

    def crossover(self, p1, p2, Cr):
        offspring = []
        offspring1 , offspring2 = p1.copy(), p2.copy()
        if rnd.rand() < Cr:
            c1 = rnd.rand()
            c2 = 1 - c1
            offspringA = list(np.array(offspring1)*c1)
            offspringB = list(np.array(offspring2)*c2)
            offspringC = list(np.array(offspring1)*c2)
            offspringD = list(np.array(offspring2)*c1)
            asu1 = self.tambahtambahan(offspring1, offspringB)
            # print("offspring1 :",offspring1)
            # print("asu1 :",asu1)
            self.add_newPop(asu1)
            self.add_newPop(self.tambahtambahan(offspring2, offspringA))
            # asu = offspringA+offspringB
            # print("offspringA ",len(offspringA))
            # print("ASU", len(asu))
            self.add_newPop(offspringC)
        else:
            self.add_newPop(offspring1)
            self.add_newPop(offspring2)

    def tambahtambahan(self,x1,x2):
        n = len(x1)
        new = []
        for i in range(n):
            new.append((x1[i]+x2[i])*1.1)
        return new


    def kawin_polygamy(self):
        pass

    def mutation(self,Mr):
        mut = math.floor(self.nPop * Mr)
        # print("mut :",mut)
        for i in range(mut):
            child = []
            # print("nDim :", self.nDim)
            for j in range(self.nDim):
                child.append(rnd.rand()*10)
            self.add_newPop(child)

    def elitisme(self):
        n = self.nPop
        self.newpop = []
        if n % 2 == 0:
            # print("genap ")
            self.add_newPop(self.bestInd)
            self.add_newPop(self.bestInd)
            self.nElit = 2
        else:
            # print("ganjil ")
            self.add_newPop(self.bestInd)
            self.nElit = 1

    def add_newPop(self, pop):
        # print ( (pop))
        self.newpop.append(pop)

    def replacePop(self):
        # print("len nPop :",self.nPop)
        for i in range(self.nPop):
            # print("NEW POP :", i, " ", len(self.newpop[i]))
            self.pop[i].position = self.newpop[i]

        self.newpop = []

    def mainAlgorithm(self, cr,mr):
        self.initPosition()
        # self.viewPosition()
        error = []
        for j in range(self.loop):
            # self.viewFitness()
            # print("best best ",self.bestFitness)
            self.calFitness()   #calculate Fitness
            # self.viewFitness()
            self.getGbest()     #find Gbest
            # print("======")
            self.elitisme()     #elitisme
            # print(self.newpop)
            # print("======")
            # print(self.newpop)
            # crossover
            for i in range(
                    self.nElit,self.nPop-math.floor(mr*self.nPop),2):
                selected = self.pickParent()
                # print("print selected ", len(selected))
                self.crossover(selected[i],selected[i+1],cr)
            self.mutation(mr)   #mutation
            # print(len(self.newpop[1]))
            self.replacePop()   #replace oldPop with newPop
            error.append(self.bestFitness)
            self.fitness.append(self.bestFitness)
            # print(self.fitness)
        plt.plot(error)
        plt.show()
        # print("best individu =",self.bestInd)
        #   fix selesai