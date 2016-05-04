num=int(input("Enter Number Of Processes: "))
arr=[]
for i in xrange(num):
    arr.append([0,0])
    arr[i][0]=(int(input("Enter Arrival Time Of Process "+ repr(i+1) +" : ")))
    arr[i][1]=(int(input("Enter Burst Time Of Process "+ repr(i+1) +" : ")))
arr.sort()
total=0
idle=0
i=0
if arr[0][0]>0:
    total=total+arr[0][0]
    idle=idle + arr[0][0]
while i!=num:
    if arr[i][0]>total:
        idle=idle+arr[i][0]-total
        total=arr[i][0]
        total=total+arr[i][1]
    else:
        total=total+arr[i][1]
    i=i+1

print "Total Time Consumed(Total Running Time): ",total
print "Total Idle Time: ",idle
