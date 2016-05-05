arr=[]
ready=[]
total=0
idle=0
turn=[]
num=input("Enter number of processes: ")
qt=input("Enter Quantum time for Round Robin: ")
for i in range(num):
    turn.append(0)
    arr.append([0,0])
    arr[i][0]=input("Enter Arrival time of process "+repr(i+1)+" : ")
    arr[i][1]=input("Enter Burst time of process "+repr(i+1)+" : ")
arr.sort()
for i in range(num):
    if arr[i][0]>total:
        idle=idle+arr[i][0]-total
        total=arr[i][0]
    if arr[i][0]<=total:
        j=i+1
        ready.append(arr[i])
        while len(ready)!=0:
            if ready[0][1]<=qt:
                total=total+ready[0][1]
                del ready[0]
            else:
                total=total+qt
                ready[0][1]=ready[0][1]-qt
                brr=ready[0]
                print ready
                del ready[0]
                print ready
                while j<num and arr[j][0]<=total:
                    print j
                    ready.append(arr[j])
                    j=j+1
                ready.append(brr)
                
print "Total Running Time: ", total
print "Total Idle Time: ", idle

            
