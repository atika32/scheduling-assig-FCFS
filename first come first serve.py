totalwaitingtime=0
totalturnarroundtime=0
n= int(input("Enter number of processes :"))
waitingtime=[0]*n
turnarroundtime=[0]*n
bursttime=[0]*n
i=0
j=0
p=[0]*n
while i<n:
      p[i]=i
      i+=1
for i in range(n):
    bursttime[i]=int(input("Enter burst time :"))
waitingtime[0]=0;
for i in range(n-1):
     j=1
     j+=i
     waitingtime[j]=waitingtime[i] + bursttime[i];
print('Process No    Burst Time    Waiting Time    Turn Around Time')
for i in range(n):
    turnarroundtime[i]=waitingtime[i]+bursttime[i];   
for i in range(n):
     print("p[",i,"]","\t\t",(bursttime[i]),"\t\t",(waitingtime[i]),"\t\t",(turnarroundtime[i]))
for i in range(n):
    totalwaitingtime=totalwaitingtime+waitingtime[i];
    totalturnarroundtime=totalturnarroundtime+turnarroundtime[i];
print("Average Waiting Time" ,totalwaitingtime/n)
print("Average Turn Arround Time", totalturnarroundtime/n)