def findNumOfPageReplacement(pageReference, numOfFrames):
    frames = [-1]*numOfFrames
    currentIndex = 0
    numOfPageReplacement = 0
    for page in pageReference:
        if page not in frames:
            frames[currentIndex%numOfFrames] = page
            numOfPageReplacement +=1
            currentIndex +=1

    # print(numOfPageReplacement)
    return numOfPageReplacement

findNumOfPageReplacement([7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1],3)