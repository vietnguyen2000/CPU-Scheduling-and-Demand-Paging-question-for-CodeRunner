from os import write
from random import Random, randint
from FCFS import findavgTime as fcfs
from LRTF import findavgTime as lrtf
from RoundRobin import findavgTime as roundRobin
from SJF_preemtive import findavgTime as sjf_preemtive
from SJF_nonpreemtive import findavgTime as sjf_nonpreemtive

import csv
import random

fileName = "FCFS_Testcase"
iter = 50
testcodes = []

numOfProcessBetween = (100,1000)
timeRandomBetween = 10
brustRandomBetween = 20
for i in range(iter):
    testcode = []
    for j in range(random.randint(numOfProcessBetween[0],numOfProcessBetween[1])):
        if j == 0:
            testcode.append((random.randint(0,timeRandomBetween),random.randint(1,brustRandomBetween)))
            
        else:
            testcode.append((testcode[j-1][0] + random.randint(0,timeRandomBetween), random.randint(1,brustRandomBetween)))
    testcodes.append(testcode)
expected_fcfs = list(map(fcfs,testcodes))
print('done fcfs')
expected_lrtf = list(map(lrtf,testcodes))
print('done lrtf')
expected_roundRobin = list(map(lambda x: roundRobin(x,random.randint(2,6)),testcodes))
print('done roundRobin')
expected_sjf_preemtive = list(map(sjf_preemtive,testcodes))
print('done sjf_preemtive')
expected_sjf_nonpreemtive = list(map(sjf_nonpreemtive,testcodes))
print('done sjf_nonpreemtive')

for x in [('FCFS_Testcase',expected_fcfs),('LRTF_Testcase',expected_lrtf),('RoundRobin_Testcase',expected_roundRobin),('SJF_nonpreemtive_Testcase',expected_sjf_nonpreemtive), ('SJF_preemtive_Testcase',expected_sjf_preemtive)]:
    with open(x[0]+'.csv', 'w', newline='') as csvfile:
        fieldname = ['testcode','expected']
        writer = csv.DictWriter(csvfile, fieldnames= fieldname)
        writer.writeheader()
        for i in range(iter):
            writer.writerow({'testcode': "findavgTime("+str(testcodes[i])+")", 'expected':x[1][i]})

