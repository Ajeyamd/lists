# t=0
# days=int(input("Enter the number of days "))  
# for days in range(1,days+1):
#     temp=int(input(f"Enter {days}'s temperature "))
#     t=t+temp
# avg=t/days
# print(f"Average = {avg}")

# if temp > avg:
#     print(f"{days}'s temperature is above average")

total=0

#create an empty list
temp=[]
def temperature(numdays):
    for days in range(1,int(numdays+1)):
        n=int(input(f"Enter {days}'s temperature "))
        temp.append(n)                                      #append the values into empty list
    avg=sum(temp)/numdays                                   #Find the average
    print(f"average= {avg}")
    above=0
    for i in temp:
        if i > avg:
            above+=1
    print(f" {above} day(s) above average")
temperature(int(input("Enter no of days ")))



    




      
    