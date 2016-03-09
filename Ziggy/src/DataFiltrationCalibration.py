import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from multiprocessing import Process
from ziggy import RandomDataGenerator


from collections import deque
from bisect import insort, bisect_left
from itertools import islice

class DataFiltrationCalibration:
    '''
        Constructor
        takes in mean, standard deviation, and number of samples 
    '''
    def __init__(self,sampleSize):
        self.samples=sampleSize
    '''
        Running mean function takes in N as the number of data points to aggregate over
    '''    
    def runningMean(self,x, N):
        return np.convolve(x, np.ones((N,))/N)[(N-1):]
    
    def plotMean(self,N) :
        ECLmean = self.runningMean( N)
        plt.plot(self.mean, 'y')
        plt.plot(ECLmean, 'r')
        
    def runningMedian(self,data, N) :
        #x = data, N = window size
        data = iter(data)
        n = N // 2
        x = [item for item in islice(data,N)]    
        d = deque(x)
        median = lambda : x[n] if bool(N&1) else (x[n-1]+x[n])*0.5
        x.sort()    
        medians = [median()]   
        for item in data:
            old = d.popleft()          # pop oldest from left
            d.append(item)             # push newest in from right
            del x[bisect_left(x, old)] # locate insertion point and then remove old 
            insort(x, item)            # insert newest such that new sort is not required        
            medians.append(median())  
        return medians
    
    def plotMedian(self,x, N) :
        median = self.runningMedian(x, N)
        plt.plot(x, 'b')
        plt.plot(median, 'g')
       
    def plotData(self,x, N) :
        plt.figure()
        plt.style.use('ggplot')
        plt.figure(figsize=(12, 10), dpi=80)
        plt.xlim(0, 2000)
        plt.ylim(-2, 2) 
        median = self.runningMedian(x, N) 
        plt.plot(x, 'b')
        plt.plot(median, 'g')
        self.plotMean(median, N) 
        
if __name__ == '__main__':
    
    #create random data
    #testData = []
    testData=RandomDataGenerator(0.0,1.0,2000)
    testData.plotNormalDistribution(testData)
    #run two processes at once 
    test =DataFiltrationCalibration(2000)
    target=test.plotData(testData,15)
   
"""
 ADD: once read in another data set, continuously update  
 Reading in multiple inputs 
 lookup table 
 random number generators for RMS noise 
 2 pass filtration: once for extreme outliers (using running median), one for data filtration
 scatterplot of frequency vs time -> determine outliers that way 
 plan for one file!!!! 

"""