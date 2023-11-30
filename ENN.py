import pandas as pd
import time
import os
from scipy.spatial import distance

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

def getNeighbors(train, loops, numNeighbors):
    testRow = train[loops]
    distances = [(trainRow, dists(testRow, trainRow)) for trainRow in train if trainRow != testRow]
    distances.sort(key = lambda tup: tup[1])
    majorClass = [distances[i][0][-1] for i in range(numNeighbors)]
    maxClass = max(majorClass, key = majorClass.count)
    if maxClass != testRow[-1]:
        editedSet.remove(testRow)
    return editedSet

paths = []

k = int(input("Value of K:"))

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
else:
    exit()

paths = [dirs for dirs in os.listdir() if dirs != os.path.basename(__file__)]
    
for folder in paths:
    reductionRate = 0
    base_dir = folder
    directory = os.listdir(base_dir)
    results_file = open(f"{folder}-resultsENN.txt", "w")
    
    for file_count, files in enumerate(directory, start=1):
        path = os.path.join(base_dir, files)
        dataset = pd.read_csv(path, sep='\t', header=None, dtype=str)

        trainSet = dataset.values.tolist()
        editedSet = dataset.values.tolist()

        edited_file = open(f"{folder}-tr{file_count}.txt", "w")

        trainCount = 0
        editedCount = 0

        tic = time.perf_counter()
        for line, _ in enumerate(trainSet):
            editedSet = getNeighbors(trainSet, line, k)
        toc = time.perf_counter()

        for element in editedSet:
            edited_file.write('\t'.join(map(str, element)) + '\n')
            editedCount += 1

        edited_file.close()

        rate = (1 - (editedCount / line)) * 100.0

        results_file.write(
            f"\n\n\n\nResults of file {file_count}"
            f"\nTime seconds: {toc - tic}"
            f"\nTraining set: {trainCount}\tEdited set: {editedCount}"
            f"\nPercentage difference: {rate}"
        )

        reductionRate += rate

    r_rate = reductionRate / 5
    results_file.write(f"\n\n\nReduction rate: {r_rate}")
    results_file.close()
