import pandas as pd
import time
import os
from scipy.spatial import distance
import Menu

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

def getNeighbors(train, loops, numNeighbors):
	distances = []
	majorClass = []
	testRow = train[loops]
	for trainRow in train:
		if trainRow == testRow:
			continue
		dist = dists(testRow, trainRow)
		distances.append((trainRow, dist))
	distances.sort(key = lambda tup: tup[1])
	for i in range(numNeighbors):
		majorClass.append(distances[i][0][-1])
		#print(distances[[i][0]])
	maxClass = max(majorClass, key = majorClass.count)
	if maxClass != testRow[-1]:
		editedSet.remove(testRow)
	return editedSet

paths = []

k = int(input("Value K:"))
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
	reductionRate = 0
	fileCount = 0
	base_dir = folder
	directory = os.listdir(base_dir)
	resultsFile = open(folder + "-resultsENN.txt", "w")
	for files in directory:
		path = os.path.join(base_dir, files)
		dataset = pd.read_csv(path, sep='\t', header = None, dtype = str)

		trainSet = dataset.values.tolist()
		editedSet = dataset.values.tolist()

		fileCount += 1
		editedFile =  open(folder + '-tr' + str(fileCount), 'w')

		trainCount = 0
		editedCount = 0

		for line in trainSet:
			trainCount += 1

		tic = time.perf_counter()
		for line in range(trainCount):
			print(line)
			editedSet = getNeighbors(trainSet, line, k)
		toc = time.perf_counter()

		length = len(editedSet[0])
		
		for element in editedSet:
			for index in range(length):
				editedFile.write(str(element[index]))
				if index != length - 1:
					editedFile.write('\t')
				else:
					continue
			editedCount += 1
			editedFile.write("\n")

		editedFile.close()

		rate = (1 - (editedCount / trainCount)) * 100.0

		resultsFile.write("\n\n\n\n" + "Results of file " + str(fileCount))
		resultsFile.write("\nTime seconds: " + str(toc - tic))
		resultsFile.write("\nTraining set: " + str(trainCount) + "\tEdited set: " + str(editedCount))
		resultsFile.write("\nPercentage difference: " + str(rate))

		reductionRate += rate

	r_rate = reductionRate / 5
	resultsFile.write("\n\n\nReduction rate: " + str(r_rate))
        
	resultsFile.close()
