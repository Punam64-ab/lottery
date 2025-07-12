#to generate a random list of numbers
import random
number=[]
for i in range(15):
    num=random.randint(1,15)
    number.append(num)

#to split the list into three parts
set1=number[0:5]
set2=number[5:10]
set3=number[10:15]

#to calculate sum
sum1=sum(set1)
sum2=sum(set2)
sum3=sum(set3)

#to print the sets and their sums
print("Set 1:", set1, "Sum:", sum1)
print("Set 2:", set2, "Sum:", sum2)
print("Set 3:", set3, "Sum:", sum3)

#to print the original list of numbers
print("Original list:", number)

#to calculate maximum sum
if(sum1>sum2) and (sum1>sum3):
    print(sum1, "Won the lottery!!")
elif(sum2>sum1) and (sum2>sum3):
    print(sum2, "Won the lottery!!")
else:
    print(sum3, "Won the lottery!!")
print("Thank you for playing the lottery!")
print("Punam Adhikari, 081BEL064")