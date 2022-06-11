import numpy as np
import matplotlib.pyplot as plt


def sum(data): # basic function for summing elements of an array
    total = 0
    for i in range(0 , len(data)):
        total = total + data[i]
    return total


def fx(x,mu,sigma): # implementation of probability density function of Normal Distribution
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-np.power((x-mu)/sigma,2)/2)

arrx = [] # an array to append calculated y1 values
bins = 100

a = 0 # interval [a , b]
b = 1 # interval [a , b]
mu = (a+b)/2 # theoretical mean or expected value of Standart Uniform Distribution
sigmasquare = ((b-a)**2) / 12 # theoretical variance of Standart Uniform Distribution

print("Theoretical Expected Value (mean)" , 50*mu) # *50 because 50 values are sampled
print("Theoretical Variance" ,50*sigmasquare) # *50 because 50 values are sampled



for n in range(20000):
    data = np.random.uniform(0,1,50) # generating 2 points between 0 and 1.
    x = sum(data) # function call
    arrx.append(x) # append y1 to an array

mean=np.mean(arrx) # calculating mean of the samples
print("Experimental Mean :" ,mean)
std=np.std(arrx) # calculating standart deviation of the samples
print("Experimental Variance :",std**2)
print("Standart Deviation :" ,std)

x=np.linspace(15 , 35 , 1000) # x axis (domain)
plt.hist(arrx, bins , density=1) # plot histogram
plt.plot(x,fx(x,mean,std)) # plot Normal Distribution Function
plt.show() # show Graphs