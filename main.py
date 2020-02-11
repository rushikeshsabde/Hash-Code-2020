def solve(MAX, inputList):

    solutionIndexList = [] 
    solutionValueList = [] 
    currentIndexList = [] 
    currentValueList = []

    fullSize = len(inputList)

    maxScore = 0 

    startIndex = fullSize 
    sum = 0
    while((len(currentIndexList) > 0 and currentIndexList[0] != 0) or len(currentIndexList) == 0):

        startIndex = startIndex - 1 

        for i in range(startIndex, -1, -1):

            currentValue = inputList[i]

            tempSum = sum + currentValue 

            if (tempSum == MAX): 
                sum = tempSum
                currentIndexList.append(i)
                currentValueList.append(currentValue) 
                break 

            elif (tempSum > MAX): 
                continue 

            elif (tempSum < MAX):
                sum = tempSum
                currentIndexList.append(i) 
                currentValueList.append(currentValue) 
                continue  

        if (maxScore < sum):  
            maxScore = sum  

            solutionIndexList = []
            solutionValueList = []

            for y in currentIndexList:
                solutionIndexList.append(y) 
            for y in currentValueList:
                solutionValueList.append(y) 

        if (maxScore == MAX): 
            break

        if(len(currentValueList) != 0):
            lastVal = currentValueList.pop() 
            sum = sum - lastVal 

        if(len(currentIndexList) != 0):
            lastIndex = currentIndexList.pop() 
            startIndex = lastIndex 

        if(len(currentIndexList) == 0 and (startIndex == 0)): 
            break 

    print("SCORE = " + str(maxScore))    

    return solutionIndexList  


def process(fileName):

    inputFile = open(inputFilesDirectory + fileName + ".in", "rt")

    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()
    MAX, NUM = list(map(int, firstLine.split()))
    inputList = list(map(int, secondLine.split()))

    outputList = solve(MAX, inputList)  
    outputString = ""
    for l in outputList:
        outputString = outputString + str(l) + " "
    print(outputString)

    outputFile = open(outputFilesDirectory + fileName + ".out", "w")
    outputFile.write(str(len(outputList)) + "\n")
    outputFile.write(outputString)
    outputFile.close()


inputFilesDirectory = "Input/"  
outputFilesDirectory = "Output/" 

fileNames = ["a_example", "b_small", "c_medium",
             "d_quite_big", "e_also_big"]  

for fileName in fileNames: 
    process(fileName)