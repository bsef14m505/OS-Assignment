arr = []
bt=[]
total=0
n = int(raw_input('Enter the total no of processes: '))
for i in range(n):
 arr.append([])
 print "Enter Arrival Time of Process" , i+1
 arr[i].append(int(raw_input()))
 print "Enter Burst Time of Process" , i+1
 bt.append(int(raw_input()))
j=1
for i in xrange(n):
 p=i
 for j in xrange(n):
  if bt[j]<bt[p]:
   p=j
  t=bt[i]
  bt[i]=bt[p]
  bt[p]=t
  t=arr[i]
  arr[i]=arr[p]
  arr[p]=t
j=0
for i in xrange(n):
 wt=0
 for j in xrange(i):
  wt+=bt[i]
 total+=wt
print 'Waiting time: ',total
print 'Average waiting time: ',(total/n)
