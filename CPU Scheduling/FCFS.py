def findavgTime(processes): 
    #TODO: write function to calculate avgWaitingTime and avgTurnAroundTime of FCFS Algorithm
    n = len(processes)
    wt = [0] * n 
    tat = [0] * n  
    completeTime = [0]*n

    # Function to find turn around time
    for i in range(n):
        completeTime[i] = max(completeTime[i-1],processes[i][0]) + processes[i][1] if i>0 else processes[i][0] + processes[i][1]
        
        tat[i] = completeTime[i] - processes[i][0] # turn around time = completeTime - arrival time

        # finding waiting time
        wt[i] = tat[i] - processes[i][1]
  
    
    
    avgWaitingTime = sum(wt) / n
    avgTurnAroundTime = sum(tat) / n

    #! DO NOT CHANGE
    # print("Average waiting time = "+ "{:.2f}".format(avgWaitingTime)) 
    # print("Average turn around time = "+ "{:.2f}".format(avgTurnAroundTime)) 
    return "Average waiting time = "+ "{:.2f}".format(avgWaitingTime) + "\n" + "Average turn around time = "+ "{:.2f}".format(avgTurnAroundTime) + "\n"

# findavgTime([(0,2),(0,2)])

