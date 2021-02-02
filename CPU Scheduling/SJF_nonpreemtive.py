
class Process:
    def __init__(self, arrivalTime, brustTime) -> None:
        self.arrivalTime = arrivalTime
        self.brustTime = brustTime
        self.remainingTime = brustTime
        self.waitingTime = 0
        self.turnAroundTime = 0
        self.completeTime = -1

def findavgTime(processes): 
    #TODO: write function to calculate avgWaitingTime and avgTurnAroundTime of SJF Algorithm (Non-preemptive)
    n = len(processes)
    lstProcess = []
    # Tạo các process 
    for process in processes:
        lstProcess.append(Process(process[0], process[1]))

    # set các thông số cần thiết
    countProcessComplete = 0
    runTime = 0
    #Chạy đến khi nào tất cả các process đều đã hoàn thành
    while(countProcessComplete < n):
        index = 0
        shortestJob = 99999
        #Tìm process chưa được thực hiện và có burst time nhỏ nhất 
        #Ở trường hợp này burst time cũng là remaining time, vì giải thuật không nhường
        for i in range(n):
            if lstProcess[i].arrivalTime <= runTime and lstProcess[i].completeTime == -1:
                if lstProcess[i].remainingTime < shortestJob:
                    #tìm được process thõa mãn
                    shortestJob = lstProcess[i].remainingTime
                    index = i
        #Cập nhật các thông số cho process thõa mãn 
        lstProcess[index].waitingTime = runTime - lstProcess[index].arrivalTime
        runTime += lstProcess[index].remainingTime
        lstProcess[index].completeTime = runTime
        lstProcess[index].turnAroundTime = lstProcess[index].waitingTime + lstProcess[index].brustTime
        
        countProcessComplete +=1
    
    avgWaitingTime = sum([process.waitingTime for process in lstProcess])/n
    avgTurnAroundTime = sum([process.turnAroundTime for process in lstProcess])/n

    #! DO NOT CHANGE
    # print("Average waiting time = "+ "{:.2f}".format(avgWaitingTime)) 
    # print("Average turn around time = "+ "{:.2f}".format(avgTurnAroundTime)) 
    return "Average waiting time = "+ "{:.2f}".format(avgWaitingTime) + "\n" + "Average turn around time = "+ "{:.2f}".format(avgTurnAroundTime) + "\n"

# findavgTime([(0,2),(2,6),(3,5),(3,2),(5,1),(6,1),(6,2),(7,2),(7,3),(6,2),(7,5),(4,3),(5,6),(10,1)])