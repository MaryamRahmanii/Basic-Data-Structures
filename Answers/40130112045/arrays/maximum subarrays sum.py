def max_subarray(arr):
    max_so_far =arr[0]
    max_ending_here =arr[0]
    a=list()
    a.append(arr[0])

    for i in range(0,len(arr)):
        if arr[i]>max_ending_here+arr[i]:
            max_ending_here=arr[i]
        else:
            max_ending_here+=arr[i]

        if max_so_far <max_ending_here:
            max_so_far=max_ending_here



    return max_so_far



input1=input("enter space after each number:")
numbers=list(map(int,input1.split()))

max_sum=max_subarray(numbers)

print("Max sum:",max_sum)