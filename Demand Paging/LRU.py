def findNumOfPageReplacement(pageReference, numOfFrames):
    frames = [-1]*numOfFrames
    numOfPageReplacement = 0
    for i in range(len(pageReference)):
        if pageReference[i] not in frames:
            index = 0
            maxLength = -99999
            for j in range(numOfFrames):
                if frames[j] not in pageReference[:i]:
                    index = j
                    break
                if pageReference[:i][::-1].index(frames[j]) > maxLength:
                    maxLength = pageReference[:i][::-1].index(frames[j])
                    index = j
            frames[index] = pageReference[i]
            numOfPageReplacement += 1
    # print(numOfPageReplacement)
    return numOfPageReplacement

findNumOfPageReplacement([7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1],3)