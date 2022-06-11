import numpy as np
import matplotlib.pyplot as plt

def sum(data): # basic function for summing elements of an array
    total = 0
    for i in range(0 , len(data)):
        total = total + data[i]
    return total
arrx = [] # an array to append calculated y1 values
bins = 100
def fx(x,mu,sigma): # implementation of probability density function of Normal Distribution
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-np.power((x-mu)/sigma,2)/2)

for j in range(20000):
    arry = []
    for i in range (50):
        a = np.random.uniform(0 , 1) # to sample a parameter
        b = np.random.uniform(0 , 1) # to sample a parameter
        data = np.random.uniform(a , b-a , 1) # the uniform distribution parameters should be sampled from a standart uniform distribution
        arry.append(data[0]) # arry is for holding values from 50 different uniform distributions
        data[0] = 0

    y = sum(arry)
    arrx.append(y) #append sums to new array which is going to hold 20000 value



mean = np.mean(arrx) # calculate mean
print("Experimental Mean :" , mean)
std = np.std(arrx) #calculate standart deviation
print("Experimental Variance :" , std**2)
print("Standart Deviation :" , std)
x = np.linspace(0 , 25 , 1000) # domain
plt.hist(arrx , bins , density=True ) # histogram
plt.plot(x,fx(x,mean,std)) # plot Normal Distribution Function
plt.show() #show graphs
