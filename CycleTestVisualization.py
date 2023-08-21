# Task 4 -> Note down the marks you have scored in all the cycle tests in your previous year of college and visualize data in a bar plot
import pandas as pd
%matplotlib inline

sno=[1,2,3,4,5,6,7,8,9,10,11,12]
test_list=["Test 1",'Test 2','Test 3','Test 4','Test 5','Test 6','Test 7','Test 8','Test 9','Test 10','Test 11','Test 12']
mark_list=[10,14,20,25,31,15,36,40,45,67,87,95]
df=pd.DataFrame({"Tests":test_list,'Marks':mark_list},index=sno)
bar=df.plot(kind='bar',color='purple')
bar.set_xlabel('Test Months')
bar.set_ylabel('Marks')
bar.set_title('Previous Year Marks')
