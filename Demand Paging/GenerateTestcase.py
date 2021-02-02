from os import write
from random import randint
from Clock import findNumOfPageReplacement as clock
from FIFO import findNumOfPageReplacement as fifo
from LRU import findNumOfPageReplacement as lru
from Optimal import findNumOfPageReplacement as optimal

import csv
import random
iter = 100
testcodes = []
testframes = []
numOfPageReplacementBetween = (100,1000)
numOfFrameBetween = 10
numOfDifferentPage = 20
for i in range(iter):
    testcode = []
    for j in range(random.randint(numOfPageReplacementBetween[0],numOfPageReplacementBetween[1])):
        testcode.append(random.randint(1,numOfDifferentPage))
    testcodes.append(testcode)
    testframes.append(randint(1,numOfFrameBetween))
expected_clock = list(map(lambda x: clock(x[0],x[1]),zip(testcodes,testframes)))
expected_fifo = list(map(lambda x: fifo(x[0],x[1]),zip(testcodes,testframes)))
expected_lru = list(map(lambda x: lru(x[0],x[1]),zip(testcodes,testframes)))
expected_optimal = list(map(lambda x: optimal(x[0],x[1]),zip(testcodes,testframes)))



for x in [('clock_Testcase',expected_clock),('fifo_Testcase',expected_fifo),('lru_Testcase',expected_lru),('optimal_Testcase',expected_optimal)]:
    with open(x[0]+'.csv', 'w', newline='') as csvfile:
        fieldname = ['testcode','expected']
        writer = csv.DictWriter(csvfile, fieldnames= fieldname)
        writer.writeheader()
        for i in range(iter):
            writer.writerow({'testcode': "findNumOfPageReplacement("+str(testcodes[i])+", " + str(testframes[i]) + ")", 'expected': str(x[1][i]) + "\n"})