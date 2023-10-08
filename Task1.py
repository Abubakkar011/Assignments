#Task 1: Fibonacci Sequence
n=int(input("Enter the N value: "))
a=0
b=0
c=1

for i in range(n):
    a=b
    b=c
    print(c)
    c=a+b
