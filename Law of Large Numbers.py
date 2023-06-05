# The Law of Large Numbers (LLN) is a fundamental principle in statistics that explains how the average of numerous independent and identically distributed random variables behaves. It states that as the size of the sample increases, the average value of the observed variables, known as the sample mean, will approach the mean of the entire population.

# Hence, we will validate the Law of Large Numbers through the application of Monte Carlo Simulation.

# Experiment:
## We will assess the probability of an unbiased coin. The expected probability of obtaining either a Head or a Tail from the coin flip should be 0.5.


#Monte Carlo Simulation function

def lnn(n):
    import random as rnd
    output= list()
    for iter in range(n):
        r = rnd.random()
        if r <= 0.5:
            ##Tail
            output.append(1)
        else: ##Head
            output.append(0)
    prob = sum(output)/ len(output)
    return round(prob,2)


for iter in [10, 100, 250, 500, 1000, 10000]:
    prob = lnn(iter)
    print(f'When number of experiment is {iter}, sample mean is {prob}\n')


# From this we can see that as the number of experiment increases, the average value of the sample approaches the population mean.

