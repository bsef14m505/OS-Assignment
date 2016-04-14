arr = []
w = 0
n = int(raw_input('Total no of processes: '))
for i in range(n):
 arr.append([])
 print "Enter Arrival Time of Process" , i+1
 arr[i].append(int(raw_input()))
 w += arr[i][0]
 print "Enter Burst Time of Process" , i+1
 arr[i].append(int(raw_input()))
print 'Waiting time: ',w
print 'Average Waiting time: ',(w/n)
