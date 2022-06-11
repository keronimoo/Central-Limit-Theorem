import numpy as np
import matplotlib.pyplot as plt

def sum(data): # basic function for summing elements of an array
    total = 0
    for i in range(0 , len(data)):
        total = total + data[i]
    return total
arrx = [] #an array to append calculated y1 values
bins = 100

def fx(x,mu,sigma): # implementation of probability density function of Normal Distribution
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-np.power((x-mu)/sigma,2)/2)



for j in range(20000):
    data = np.random.uniform(0 , 300 , 50) # Since interval of the uniform distrubitons not given i choose [0 , 300 ] as interval
    for i in range(49):
        if data[i] < 99:
            # if a value is smaller than 99 the next value is sampled from uniform distribution between 0 and 200
            data[i+1] = np.random.uniform(0 , 200 , 1) # change next value ---> interval [0 , 200]
        else:
            data[i+1] = np.random.uniform(98 , 102 , 1) # change next value ---> interval [98 , 102]
    y = sum(data) # y1 = x1 + x2 + x3 + ....... x50
    arrx.append(y) #append sums to new array which is going to hold 20000 value

mean = np.mean(arrx) # calculate mean
print("Experimental Mean :" ,mean)
std = np.std(arrx) #calculate standart deviation
print("Experimental Variance :" , std**2)
print("Standart Deviation :" ,std)
x = np.linspace(4000 , 6500 , 1000) #domain
plt.hist(arrx , bins , density=True ) #histogram
plt.plot(x,fx(x,mean,std)) # plot Normal Distribution Function
plt.show() #show graphs