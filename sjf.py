print "In SJF, The Arrival Time for all proceses is zero\n"
num=int(input("Enter Number Of Processes: "))
arr=[]
for i in xrange(num):
    arr.append((int(input("Enter Burst Time Of Process "+ repr(i+1) +" : "))))
arr.sort()
total=0
i=0
avg=0
ravg=0
while i!=num:
    total=total+int(arr[i])
    j=i
    while j>0:
        avg=avg+arr[j-1]
        print avg
        j=j-1
    print "\n"
    ravg=ravg+avg
    avg=0
    i=i+1
print "Total Running Time: ",total
print "The Average Waiting Time: ",ravg/(1.00*num)
