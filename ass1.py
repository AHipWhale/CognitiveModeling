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
        return 75
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

print(exmaple1())

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
        print(all_combinations)
        
        combo_values = []
        for combo in all_combinations:
            combo_values.append(start() + perceptualstep(combo[0]) + cognitivestep(combo[1]) + motorstep(combo[2]))
            
        fig = plt.figure()
        plt.boxplot(combo_values)
        plt.ylabel("time (ms)")
        plt.show()

        return combo_values
        

print(example2("all"))

