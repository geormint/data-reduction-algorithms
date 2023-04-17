import os 
import pandas as pd
from scipy.spatial import distance
import random
import time

def dists(testRow, trainRow):
        f_row = []
        s_row = []
        for num1 in range(len(testRow) - 1):
                if testRow[num1] is not int:
                        conversion = float(testRow[num1])
                        f_row.append(conversion)
        for num2 in range(len(trainRow) - 1):
                if trainRow[num2] is not int:
                        conversion = float(trainRow[num2])
                        s_row.append(conversion)
        if calculation == 1:
                dist = distance.euclidean(f_row, s_row)
        if calculation == 2:
                dist = distance.cityblock(f_row, s_row)
        if calculation == 3:
                dist = distance.minkowski(f_row, s_row, parameter)
        if calculation == 4:
                dist = distance.chebyshev(f_row, s_row)
        return dist

def getNeighbors(trainSet, value):
	distances = []
	testRow = trainSet[value]
	for trainRow in condensedSet:
		dist = dists(testRow, trainRow)
		distances.append((trainRow, dist))
	distances.sort(key = lambda tup: tup[1])
	if distances[0][0][-1] != testRow[-1]:
		#print(distances[0][0])
		condensedSet.append(testRow)
	return distances, condensedSet

paths = []
condensedSet = []

calculation = int(input("Which distance you want to calculate - 1 for Euclidean\n"
                     "\t\t\t\t     - 2 for Manhattan\n"
                     "\t\t\t\t     - 3 for Minkowski\n"
                     "\t\t\t\t     - 4 for Chebyshev\n"
                     "\t\t\t\t     : "))
if calculation == 3:
        parameter = int(input("Choose parameter for Minkowski - 3 or 4: "))

for dirs in os.listdir():
    if dirs == os.path.basename(__file__):
        continue
    paths.append(dirs)

for folder in paths:
	stop = True
	reductionRate = 0
	fileCount = 0
	base_dir = folder
	directory = os.listdir(base_dir)
	resultsFile = open(folder + "-resultsCNN.txt", "w")
	for files in directory:
		path = os.path.join(base_dir, files)
		dataset = pd.read_csv(path, sep='\t', header = None, dtype = str)	
		
		trainSet = dataset.values.tolist()
		condensedSet.clear()

		fileCount += 1
		condensedFile = open(folder + '-tr' + str(fileCount), 'w')
		
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
		resultsFile.write("\n\n\n\n" + "Results of file " + str(fileCount))
		resultsFile.write("\nTime seconds: " + str(toc - tic))
		resultsFile.write("\nTraining set: " + str(trainCount) + "\tCondensed set: " + str(condensedCount))
		resultsFile.write("\nPercentage difference: " + str(rate))

		reductionRate += rate
		stop = True

	r_rate = reductionRate / 5
	resultsFile.write("\n\n\n Reduction rate: " + str(r_rate))
        
	resultsFile.close()