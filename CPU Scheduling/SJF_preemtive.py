
class Process:
    def __init__(self, arrivalTime, brustTime) -> None:
        self.arrivalTime = arrivalTime
        self.brustTime = brustTime
        self.remainingTime = brustTime
        self.waitingTime = 0
        self.turnAroundTime = 0
        self.completeTime = -1

def findavgTime(processes): 
    #TODO: write function to calculate avgWaitingTime and avgTurnAroundTime of SJF Algorithm (Preemptive)
    n = len(processes)
    lstProcess = []
    # Tạo các process 
    for process in processes:
        lstProcess.append(Process(process[0], process[1]))

    # set các thông số cần thiết
    countProcessComplete = 0
    runTime = 0
    #Chạy đến khi nào tất cả các process đều đã hoàn thành
    #Lặp qua từng thời điểm
    while(countProcessComplete < n):
        index = -1
        shortestJob = 99999
        #Tìm process chưa được thực hiện và có remaining time nhỏ nhất 
        for i in range(n):
            if lstProcess[i].arrivalTime <= runTime and lstProcess[i].completeTime == -1:
                if lstProcess[i].remainingTime < shortestJob:
                    #tìm được process thõa mãn
                    shortestJob = lstProcess[i].remainingTime
                    index = i

        runTime += 1
        #nếu không tìm được process thõa mãn thì skip 
        if index == -1:
            continue
        #Cập nhật các thông số cho process thõa mãn 
        lstProcess[index].remainingTime -= 1
        if lstProcess[index].remainingTime == 0: #process hoàn thành
            lstProcess[index].completeTime = runTime
            lstProcess[index].turnAroundTime = runTime - lstProcess[index].arrivalTime
            lstProcess[index].waitingTime = lstProcess[index].turnAroundTime - lstProcess[index].brustTime
            countProcessComplete +=1
    
    avgWaitingTime = sum([process.waitingTime for process in lstProcess])/n
    avgTurnAroundTime = sum([process.turnAroundTime for process in lstProcess])/n

    #! DO NOT CHANGE
    # print("Average waiting time = "+ "{:.2f}".format(avgWaitingTime)) 
    # print("Average turn around time = "+ "{:.2f}".format(avgTurnAroundTime)) 
    return "Average waiting time = "+ "{:.2f}".format(avgWaitingTime) + "\n" + "Average turn around time = "+ "{:.2f}".format(avgTurnAroundTime) + "\n"

# findavgTime([(1,6),(1,8),(2,7),(3,3)])