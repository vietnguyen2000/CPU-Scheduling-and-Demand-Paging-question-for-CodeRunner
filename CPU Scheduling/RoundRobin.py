class Process:
    def __init__(self, arrivalTime, brustTime) -> None:
        self.arrivalTime = arrivalTime
        self.brustTime = brustTime
        self.remainingTime = brustTime
        self.waitingTime = 0
        self.turnAroundTime = 0
        self.completeTime = -1

def findavgTime(processes, quantumTime): 
    #TODO: write function to calculate avgWaitingTime and avgTurnAroundTime of RoundRobin Algorithm
    n = len(processes)
    lstProcess = []
    # Tạo các process 
    for process in processes:
        lstProcess.append(Process(process[0], process[1]))

    # set các thông số cần thiết
    countProcessComplete = 0
    runTime = 0
    index = 0
    quantumCount = 0
    #Chạy đến khi nào tất cả các process đều đã hoàn thành
    #Lặp qua từng thời điểm
    while(countProcessComplete < n):
        if quantumCount == 0:
            #Tìm process chưa được thực hiện
            for i in range(index, index + n):
                if lstProcess[i%n].arrivalTime <= runTime and lstProcess[i%n].completeTime == -1:
                    #tìm được process thõa mãn
                    index = i%n
            quantumCount = quantumTime
        runTime += 1

        quantumCount -= 1
        #Cập nhật các thông số cho process thõa mãn 
        lstProcess[index].remainingTime -= 1
        if lstProcess[index].remainingTime == 0: #process hoàn thành
            lstProcess[index].completeTime = runTime
            lstProcess[index].turnAroundTime = runTime - lstProcess[index].arrivalTime
            lstProcess[index].waitingTime = lstProcess[index].turnAroundTime - lstProcess[index].brustTime
            countProcessComplete +=1
            # print(index+1, lstProcess[index].completeTime, lstProcess[index].waitingTime, lstProcess[index].turnAroundTime)
    avgWaitingTime = sum([process.waitingTime for process in lstProcess])/n
    avgTurnAroundTime = sum([process.turnAroundTime for process in lstProcess])/n

    #! DO NOT CHANGE
    # print("Average waiting time = "+ "{:.2f}".format(avgWaitingTime)) 
    # print("Average turn around time = "+ "{:.2f}".format(avgTurnAroundTime)) 
    return "Average waiting time = "+ "{:.2f}".format(avgWaitingTime) + "\n" + "Average turn around time = "+ "{:.2f}".format(avgTurnAroundTime) + "\n"

# findavgTime([(0,3),(0,4),(0,3)],1)
# findavgTime([(0,10),(0,5),(0,8)],2)