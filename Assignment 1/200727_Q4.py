import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline
import pandas as pd


m = int(input("Input m: "))  # input m

prob = []  # list of probabilities


sum = 0
for i in range(0, m-1):
    x = float(input("Input probability p_%(i)d: " % {"i": i}))
    prob.append(x)
    sum = sum + prob[i]

prob.append(1-sum)

n = int(input("Input number of samples to be generated (n): "))

avg = []  # stores average of the samples generated during each iteration

itr = 50000

for i in range(0, itr):
    sum = 0
    samples = []
    for j in range(0, n):
        # generated the sample according the probability distribution
        x = np.random.choice(np.arange(0, m), p=prob)
        sum = sum + x  # sum of sample
        samples.append(x)
    print("The samples on %(i)d th iteration is " % {"i": i})
    print(samples)
    average = sum/n  # average of sample
    average = round(average, 2)  # average rounded upto 2 decimal place
    print("Average on %(i)d th iteration is: %(average)f " %
          {"i": i, "average": average})
    print(" ")
    avg.append(average)


freq = {}  # stores frequency of averages


def FrequencyCount(lst):  # function to count the frequency

    for i in lst:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i] = 1


FrequencyCount(avg)

lists = sorted(freq.items())  # sorted by key, return a list of tuples
x, y = zip(*lists)  # x = average, y = frequency

plt.plot(x, y)
plt.title("Frequency of Averages")
plt.xlabel("Average")
plt.ylabel("Frequency")
plt.show()

x_new = np.asarray(x)
y_new = np.asarray(y)

X_Y_Spline = make_interp_spline(x_new, y_new)

X_ = np.linspace(x_new.min(), x_new.max(), 500)
Y_ = X_Y_Spline(X_)

plt.plot(X_, Y_)
plt.title("Frequency of Averages(smooth)")
plt.xlabel("Average")
plt.ylabel("Frequency")
plt.show()
