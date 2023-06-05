myList=list()
while(True):
   inp=input('Enter a number ')
   if inp == 'done' : break
   value=float(inp)
   myList.append(value)
avg=sum(myList)/len(myList)
    
print("average=",avg)
print(myList)