def findNumOfPageReplacement(pageReference, numOfFrames):
    frames = [-1]*numOfFrames
    secondChange = [False]*numOfFrames
    currentIndex = 0
    numOfPageReplacement = 0
    for i in range(len(pageReference)):
        if pageReference[i] in frames:
            secondChange[frames.index(pageReference[i])] = True
        elif pageReference[i] not in frames:
            for j in range(currentIndex, currentIndex+numOfFrames*2):
                if secondChange[j%numOfFrames] == True:
                    secondChange[j%numOfFrames] = False
                    continue
                else:
                    frames[j%numOfFrames] = pageReference[i]
                    currentIndex = j%numOfFrames + 1
                    break
            numOfPageReplacement += 1
    # print(numOfPageReplacement)
    return numOfPageReplacement

# findNumOfPageReplacement([2,5,10,1,2,2,6,9,1,2,10,2,6,1,2,1,6,9,5,1],4)
findNumOfPageReplacement([2,5,10,1,2,2,6,9,1,2,10,2,6,1,2,1,6,9,5,1],3)
