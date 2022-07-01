import numpy as np
import matplotlib.pyplot as plt
import random


def random_N():
    N = random.randint(10000, 1000000)
    return N


def kchoices(N, k):
    k_tickets = []
    for i in range(0, k):
        a = random.randint(1, N+1)
        k_tickets.append(a)
    return k_tickets


def mean_median(N, k_range, itr):
    avg_mean = []
    avg_median = []
    for k in range(1, k_range + 1):
        mean = []
        median = []
        for i in range(0, itr):
            k_tickets = kchoices(N, k)
            a = np.mean(k_tickets)
            mean.append(a)
            b = np.median(k_tickets)
            median.append(b)
        avg_mean.append(np.mean(mean))
        avg_median.append(np.mean(median))
    return avg_mean, avg_median


def N_expectation(m):
    expected_N = [i * 2 - 1 for i in m]
    return expected_N


def plotting(expected_N, k_range, N):
    plt.plot(range(1, k_range+1), expected_N)
    plt.plot(range(1, k_range+1), [N]*len(range(1, k_range+1)))
    plt.legend(["expected_N", "actual_N"])
    plt.show()


def prediction(i):
    print("\nPrediction %(i)d\n" % {"i": i})
    N = random_N()
    mean, median = mean_median(N, 1000, 100)
    expected_N_mean = N_expectation(mean)
    print("\nFor k going from 1 to 1000, corresponding expected N values (calculated using mean, on 100 iterations) are as follows:\n")
    print(expected_N_mean)
    expected_N_median = N_expectation(median)
    print("\nFor k going from 1 to 1000, corresponding expected N values (calculated using median, on 100 iterations) are as follows:\n")
    print(expected_N_median)
    print("\nThe actual value of N is %(N)d\n" % {"N": N})
    plotting(expected_N_mean, 1000, N)
    plotting(expected_N_median, 1000, N)


print("Prediction for 3 different Ns.\n")

for i in range(1, 4):
    prediction(i)
