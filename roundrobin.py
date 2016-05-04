qt=int(input("Enter Quantum Time for Round Robin: "))
num=int(input("Enter Number Of Processes: "))
remainp=num
turnaround=0
waiting=0
time=0
flag=0
arr=[]
rt=[]
print arr
for i in range(num):
    arr.append([0,0,0])
    arr[i][0]=(int(input("Enter Arrival Time Of Process "+ repr(i+1)+" : ")))
    arr[i][1]=(int(input("Enter Burst Time Of Process "+repr(i+1)+" : ")))
    arr[i][2]=arr[i][1]
print arr
print rt
arr.sort()
print arr
print len(arr)
for i in range(len(arr)):
    for j in range(2):
        print arr[i][j]
print "\nProcess\t|Turnaround Time|Waiting Time\n"
i=0
while remainp!=0:
    if arr[i][2]<=qt and arr[i][2]>0:
        time=time+arr[i][2]
        arr[i][2]=0
        flag=1
    elif arr[i][2]>0:
        arr[i][2]=arr[i][2]-qt
        time=time+qt
    if arr[i][2]==0 and flag==1:
        remainp=remainp-1
        print "P"+repr(i+1)+"\t|\t",time-arr[i][0]," \t|\t",time-arr[i][0]-arr[i][1],"\n"
        waiting=waiting+time-arr[i][0]-arr[i][1]
        turnaround=turnaround+time-arr[i][0]
        flag=0
    if(i==num-1):
        i=0
    elif arr[i+1][0]<time:
        i=i+1
    else:
        i=0
print "Average Waiting Time ", float(waiting/(1.00*num))
print "Average Turnaround Time", float(turnaround/(1.00*num))
