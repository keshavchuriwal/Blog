import itertools
from collections import defaultdict
f=open("partition.txt","r")

support=[2,1,2,1]
avg=float(sum(support))/4
lines = f.readlines()
lines2d=[['' for x in range(0)] for x in range(4)]

distinct = defaultdict(dict)    
overall_distinct=[]

i=1
for line in lines:
    line=line.strip()
    if('-' in line):
        i=i+1
        continue
    else:
        lines2d[i-1].append(line)
    for item in line.split(','):
        if(item not in distinct[i].keys()):
            distinct[i][item]=1
        else:
            distinct[i][item]=distinct[i][item]+1
        if(item not in overall_distinct):
            overall_distinct.append(item)


list1 = [['' for x in range(0)] for x in range(4)] 
frequent=[['' for x in range(0)] for x in range(4)] 

print ("------C 1-----")
for i in range(1,5,1):
    for key in sorted(distinct[i]):
            print ("('%s') %d" % (key, distinct[i][key]))
    print ("-----\n")
        
print ('\n******L 1*****')
for i in range(1,5,1):
    for key in sorted(distinct[i]):
        if(distinct[i][key]>=support[i-1]):
            print ("('%s') %d" % (key, distinct[i][key]))
            if(key not in list1):
                list1[i-1].append(key)
                frequent[i-1].append(key)
    print ("-----")

print ("\n\n")



newlist=[['' for x in range(0)] for x in range(4)] 

for i in range(1,5,1):
    print ('\n\nFOR PARTITION NO. : ',i,'\n\n')
    length=len(list1[i-1])
    L=2
    while(L<=length):
        print ('------C',L,'-----')
        for subset in itertools.combinations(list1[i-1], L):
                for line in lines2d[i-1]:
                    line=line.strip().split(',')
                    if(subset not in distinct[i]):
                        distinct[i][subset]=0
                    if(set(subset).issubset(set(line))):
                        distinct[i][subset]=distinct[i][subset]+1
    
                print (subset, distinct[i][subset])
        print ('******L',L,'*****')
        for subset in itertools.combinations(list1[i-1], L):
                if(distinct[i][subset]>=support[i-1]):
                    print (subset, distinct[i][subset])
                    frequent.append(subset)
                    for j in subset:
                        if j not in newlist[i-1]:
                            newlist[i-1].append(j)
        list1[i-1]=newlist[i-1]
        newlist[i-1]=[]
        length=len(list1[i-1])
        print ("\n\n")
        L=L+1
        
new_elements=[]
for l in range(len(overall_distinct)):
    for subset in itertools.combinations(overall_distinct, l):
        total=0        
        count=0
        for i in range(1,5):
            for j in distinct[i].keys():
                if(sorted(subset)==sorted(j) and distinct[i][j]>=support[i-1]):
                    total=total+distinct[i][j]
                    count=count+1
                    break
        #print sorted(subset)
        if(count==0):
            continue
        else:
            print (("('%s') %.2f") % (subset, float(total)/float(count)))
            if(float(total)/float(count)>=avg):
                new_elements.append(subset)

print ('\n\n')   

for k in new_elements:
    total=0
    for i in range(1,5):
        for j in distinct[i].keys():
            if(sorted(k)==sorted(j)):
                total=total+distinct[i][j]
                break
    print (("('%s') %.2f") % (sorted(k), float(total)/float(4)))