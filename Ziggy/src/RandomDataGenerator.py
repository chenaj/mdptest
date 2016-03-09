'''

'''
import numpy as np
import matplotlib.pyplot as plt
import random


class RandomDataGenerator:
    '''
        Constructor
        takes in mean, standard deviation, and number of samples 
    '''
    def __init__(self,m,sd,samp):
        self.mean=m
        self.std=sd
        self.samples=samp

    def randomNormalDistribution(self):
        return np.random.normal(self.mean, self.std, self.samples)
    
    def plotNormalDistribution(self,data):
        s=data.randomNormalDistribution()
        count, bins, ignored = plt.hist(s, 30, normed=True)
        plt.plot(bins, 1/(data.std * np.sqrt(2 * np.pi)) *np.exp( - (bins - data.mean)**2 / (2 * data.std**2) ),linewidth=2, color='r')
        plt.show()
        
#data=RandomDataGenerator(0.0,1.0,2000)
#data.plotNormalDistribution(data)