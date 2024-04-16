def merge(num1,len1,num2,len2):
    i=len1-1
    j=len2-1
    k=len1+len2-1
    for n in range(len2):
        num1.append(0)

    while i>=0 and j>=0:
        if num1[i]>num2[j]:
            num1[k]=num1[i]
            i-=1
        else:
            num1[k]=num2[j]
            j-=1
        k-=1
    while j>=0:
        num1[k]=num1[j]
        j-=1
        i-=1


input1 = input("enter space after each number:")
num1 = list(map(int, input1.split()))
len1 = len(num1)
input2 = input("enter space after each number:")
num2 = list(map(int, input2.split()))
len2 = len(num2)
merge(num1,len1,num2,len2)

a=list()

for m in range(len1+len2):
    if(m==0 or num1[m]!=num1[m-1]):
        a.append(num1[m])

print(a)