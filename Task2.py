#Task 2: Printing Positive numbers

n=int(input("Enter the N value: ")) 
mylist=list() 

for i in range(n):
    value=int(input("Enter value"+str(i)+" :"))
    mylist.append(value)

mylist.sort()

for i in range(n): 
    if mylist[i]>=0: 
        print(mylist[i])
