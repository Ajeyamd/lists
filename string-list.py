#Convert into a list using LIST()
string = "spam spam spam"
mylist=list(string)
print(mylist)

#Split string using delimiter
string2 = "spam-spam-spam"
delimiter = '-'
mylist2=string2.split(delimiter)
print(mylist2)


#Joining strings into a list using JOIN()
mylist3 = ['s','p','a','m']
delimiter = ''
string3 = delimiter.join(mylist3)
print(string3)