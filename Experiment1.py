import numpy as np
import matplotlib.pyplot as plt




def fx(x,mu,sigma): # implementation of probability density function of Normal Distribution
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-np.power((x-mu)/sigma,2)/2)

arrx = [] # an array to append calculated y1 values
bins = 100

a = 0 # interval [a , b]
b = 1 # interval [a , b]
mu = (a+b)/2 # theoretical mean or expected value of Standart Uniform Distribution
sigmasquare = ((b-a)**2) / 12 # theoretical variance of Standart Uniform Distribution



for n in range(20000):
    data = np.random.uniform(0,1,2) # generating 2 points between 0 and 1.
    x = data[0] + data[1] #y1 = x1 + x2
    print(x)
    arrx.append(x) # append y1 to an array

print("Theoretical Mean :" , 2*mu)
print("Theoretical Variance :", 2*sigmasquare)
mean=np.mean(arrx) # calculating mean of the array
print("Experimental Mean :" ,mean)
std=np.std(arrx) # calculating standart deviation of the array
print("Experimental Variance :" , std**2)
print("Standart Deviation" ,std)

x=np.linspace(-1, 3 , 1000) #x axis
plt.hist(arrx, bins , density=True) # plot histogram
plt.plot(x,fx(x,mean,std)) # plot Normal Distribution Function
plt.show() # show Graphs
