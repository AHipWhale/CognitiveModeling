import time
import itertools
import numpy as np
import matplotlib.pyplot as plt

def start(type="middle"):
    if type == "fast":
        return 0
    elif type == "middle":
        return 0
    else:
        return 0
     
def perceptualstep(type="middle"):
    if type == "fast":
        return 50
    elif type == "middle":
        return 100
    else:
        return 200

def cognitivestep(type="middle"):
    if type == "fast":
        return 25
    elif type == "middle":
        return 70
    else:
        return 170

def motorstep(type="middle"):
    if type == "fast":
        return 30
    elif type == "middle":
        return 70
    else:
        return 100


def exmaple1():
    t = 0
    t += start()
    t += perceptualstep()
    t += cognitivestep()
    t += motorstep()
    return t


def example2(completeness="extremes"):
    if completeness == "extremes":
        fast = start("fast") + perceptualstep("fast") + cognitivestep("fast") + motorstep("fast")
        middle = start("middle") + perceptualstep("middle") + cognitivestep("middle") + motorstep("middle")
        slow = start("slow") + perceptualstep("slow") + cognitivestep("slow") + motorstep("slow")
        return fast, middle, slow
    else:
        functions = [perceptualstep, cognitivestep, motorstep]
        types = ["fast", "middle", "slow"]
        
        all_combinations = list(itertools.product(types, repeat=len(functions)))
        
        combo_values = []
        for combo in all_combinations:
            combo_values.append(start() + perceptualstep(combo[0]) + cognitivestep(combo[1]) + motorstep(combo[2]))
            
        fig = plt.figure()
        plt.boxplot(combo_values)
        plt.ylabel("time (ms)")
        plt.show()

        return combo_values
        

def example3():
    functions = [perceptualstep, cognitivestep, motorstep]
    types = ["fast", "middle", "slow"]
    
    all_combinations = list(itertools.product(types, repeat=len(functions)))

    combo_values = []
    for combo in all_combinations:
        combo_values.append(start() + 2 * perceptualstep(combo[0]) + 2 * cognitivestep(combo[1]) + motorstep(combo[2]))

    return combo_values

def example4():
    functions = [perceptualstep, cognitivestep, motorstep]
    types = ["fast", "middle", "slow"]
    
    all_combinations = list(itertools.product(types, repeat=len(functions)))
    
    combo_values = []
    for delay in [40, 80, 110, 150, 210, 240]:
        for combo in all_combinations:
            snd_perceptualstep_start = max(perceptualstep(combo[0]), delay)
            combo_values.append(start() +  snd_perceptualstep_start + perceptualstep(combo[0]) + 2 * cognitivestep(combo[1]) + motorstep(combo[2]))
    return combo_values

def example5():
    functions = [perceptualstep, cognitivestep, motorstep]
    types = ["fast", "middle", "slow"]
    
    all_combinations = list(itertools.product(types, repeat=len(functions)))

    combo_values = []
    error_probs = []
    for combo in all_combinations:
        error_prob = 0.01
        for i, tp in enumerate(combo):
            if tp == "slow":
                error = 0.5
            elif tp == "middle":
                error = 2
            else:
                error = 3
            if i == 0 or i == 1:
                error_prob *= error * error
            else:
                error_prob *= error

        error_probs.append(min(error_prob, 1))
        combo_values.append(start() + 2 * perceptualstep(combo[0]) + 2 * cognitivestep(combo[1]) + motorstep(combo[2]))

    plt.scatter(combo_values, error_probs)
    plt.xlabel("trial time (ms)")
    plt.ylabel("probability error (fraction)")
    plt.show()

    return combo_values, error_probs


# print(exmaple1())
# print(example2("all"))
# print(example3())
# print(max(example4()))
print(example5())
