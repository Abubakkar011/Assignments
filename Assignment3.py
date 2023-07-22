# Task: To count repeatedly occurred characters in a string
def most_frequent(string):
    string=list(string)
    i=int(0)
    j=int(0)
    mydict=dict()
    for i in range(len(string)):
        count=0
        for j in range(len(string)):
            if string[j]==string[i]:
                count+=1
                
        mydict[string[i]]=count
        if mydict[string[i]]==1:
            mydict.pop(string[i])
            

    print(mydict)

string=input("Enter the string: ")
most_frequent(string)
