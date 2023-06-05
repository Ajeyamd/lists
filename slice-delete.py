import create  
obj=create.abc()

#Slicing
print(obj.spam[1:4])
obj.spam[0:2]=[-1,-2]
print(obj.spam)

#Deleting
del obj.spam[1:4]
print(obj.spam)

#remove
spam2=['ajeya',1,2,3,4]
spam2.remove('ajeya')
print(spam2)