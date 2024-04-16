input1=input("enter space after each number:")
numbers=list(map(int,input1.split()))
size=len(numbers)
a=list()

for i in range(size):
    if(i==0 or numbers[i]!=numbers[i-1]):
        a.append(numbers[i])

print(len(a))