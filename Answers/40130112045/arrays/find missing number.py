input=input("enter space after each number:")
numbers=list(map(int,input.split()))
sum=0
size=len(numbers)
for i in numbers:
    sum=sum+i

total=(size*(size+1))/2

missing_num=total-sum

print(missing_num)

