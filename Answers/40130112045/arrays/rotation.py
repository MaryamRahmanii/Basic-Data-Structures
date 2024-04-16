
def shift(array,k):
    return array[-k:]+array[:-k]

input1=input("enter space after each number:")
numbers=list(map(int,input1.split()))
num=input("k:")
k=int(num)
size=len(numbers)
shifted=shift(numbers,k)
print(shifted)
