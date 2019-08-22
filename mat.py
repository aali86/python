#Matrix=[[5 for i in range(10)]for x in range(10)]
#Matrix=[]
#for i in range(10):
 #   for x in range(10):
  #      Matrix.append([i][x])

#print(Matrix)


temps = [[0.0 for h in range(24)] for d in range(31)]

#sum=0.0
#print(temps)
#for day in temps:
 #   print(day[11])
#    sum += day[11]
#average = sum/31

#print("average...", average)

max=-100.0

for day in temps:
    for temp in day:
        if temp > max:
            max =temp
print("max temp..",max)
