numbers=[10,20,78,67]
even=[]
odd=[]
for n in numbers:
   if n %2==0:
    even.append(n)
else:
   odd.append(n)
print("Even:",even)
print("Odd:",odd)