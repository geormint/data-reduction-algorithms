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

def getNeighbors(trainSet, value):
    testRow = train[loops]
    distances = [(trainRow, dists(testRow, trainRow)) for trainRow in train if trainRow != testRow]
    distances.sort(key = lambda tup: tup[1]
    if distances[0][0][-1] != testRow[-1]:
	condensedSet.append(testRow)
    return distances, condensedSet

paths = []
condensedSet = []

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
    stop = True
    reductionRate = 0
    base_dir = folder
    directory = os.listdir(base_dir)
    results_file = open(f"{folder}-resultsENN.txt", "w")
    
    for file_count, files in enumerate(directory, start=1):
        path = os.path.join(base_dir, files)
        dataset = pd.read_csv(path, sep='\t', header=None, dtype=str)

        trainSet = dataset.values.tolist()	
		condensedSet.clear() 

		fileCount += 1
		condensedFile = open(f"{folder} + '-tr' + {fileCount}, 'w'")
		
		trainCount = 0
		
		for count in trainSet:
			trainCount += 1

		randChoice = random.choice(trainSet)
		condensedSet.append(randChoice)
		trainSet.remove(randChoice)

		previousData = 0
		condensedCount = 0

		while stop:
			dataCount = 0
			currentData = 0

			for _ in trainSet:
				dataCount += 1

			tic = time.perf_counter()
			for value in range(dataCount):
				print(value)
				distances, condensedSet = getNeighbors(trainSet, value)
			toc = time.perf_counter()

			for element in condensedSet:
				for value in trainSet:
					if element == value:
						trainSet.remove(element)

			for _ in trainSet:
				currentData += 1

			if previousData == currentData:
				stop = False

			previousData = currentData
		
		length = len(condensedSet[0])

		for element in condensedSet:
			for index in range(length):
				condensedFile.write(str(element[index]))
				if index != length - 1:
					condensedFile.write('\t')
				else:
					continue
			condensedCount += 1 
			condensedFile.write("\n")


		condensedFile.close()

		rate = (1 - (condensedCount / trainCount)) * 100.0
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
