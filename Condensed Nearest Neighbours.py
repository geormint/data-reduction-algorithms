import os 
import pandas as pd
from scipy.spatial import distance
import random
import time

def dists(testRow, trainRow):
    f_row = [float(val) if not isinstance(val, int) else val for val in testRow[:-1]]
    s_row = [float(val) if not isinstance(val, int) else val for val in trainRow[:-1]]
    
    distance_functions = {
        1: distance.euclidean,
        2: distance.cityblock,
        3: lambda f_row, s_row: distance.minkowski(f_row, s_row, parameter),
        4: distance.chebyshev
    }

    if calculation in distance_functions:
        dist = distance_functions[calculation](f_row, s_row)
    else:
        print("No valid option")
        
    return dist

def get_neighbors(testRow):
    distances = [(trainRow, dists(testRow, trainRow)) for trainRow in condensed_set]
    distances.sort(key=lambda tup: tup[1])
    
    if distances and distances[0][0][-1] != testRow[-1]:
        condensed_set.append(testRow)
    return distances, condensed_set

paths = []
condensed_set = []

calculations = {
    1: "Euclidean",
    2: "Manhattan",
    3: "Minkowski",
    4: "Chebyshev"
}

calculation = int(input(f"Which distance you want to calculate - {', '.join([f'{key} for {value}' for key, value in calculations.items()])}: "))

parameter = None
if calculation == 3:
    parameter = int(input("Choose parameter for Minkowski - 3 or 4: "))

paths = [dirs for dirs in os.listdir() if dirs != os.path.basename(__file__)]

for folder in paths:
    reductionRate = 0
    base_dir = folder
    directory = os.listdir(base_dir)
    
    for file_count, files in enumerate(directory, start=1):
        path = os.path.join(base_dir, files)
        dataset = pd.read_csv(path, sep='\t', header=None, dtype=str)
        train_set = dataset.values.tolist()
        condensed_set.clear()

        randChoice = random.choice(train_set)
        condensed_set.append(randChoice)
        train_set.remove(randChoice)

        while True:
            previous_data = len(train_set)

            tic = time.perf_counter()
            for value in train_set:
                distances, condensed_set = get_neighbors(value)
            toc = time.perf_counter()
            
            train_set = [value for value in train_set if value not in condensed_set]

            current_data = len(train_set)
        
            if previous_data == current_data:
                break

        with open(f"{folder}-tr{file_count}.txt", "w") as condensed_file:
            for element in condensed_set:
                condensed_file.write('\t'.join(map(str, element)) + '\n')
        
        rate = (1 - (len(condensed_set) / len(train_set))) * 100.0

        with open(f"{folder}-resultsCNN.txt", "a") as results_file:
            results_file.write(
                f"\n\n\n\nResults of file {file_count}"
                f"\nTime seconds: {toc - tic}"
                f"\nTraining set: {len(train_set)}\tCondensed set: {len(condensed_set)}"
                f"\nPercentage difference: {rate}"
            )

        reductionRate += rate

    r_rate = reductionRate / 5
    with open(f"{folder}-resultsCNN.txt", "a") as results_file:
        results_file.write(f"\n\n\nReduction rate: {r_rate}")
