#Task 1: Calculating The Area Of A Circle
import numpy as np
radius=int(input("Enter the radius: "))
area=np.pi*(radius**2)
print("The Area of the circle is ",area)


#Task 2: Detecting The File Extension 
file=input("Enter your filename with extension: ")
file=file.split(".")[1]
print("The extension of the file is: "+file)
