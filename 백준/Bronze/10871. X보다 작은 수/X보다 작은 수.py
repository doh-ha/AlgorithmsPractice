n,x=map(int,input().split())

arr=list(map(int,input().split()))
less_arr=[]




for num in arr:
    
    if num<x: 
        less_arr.append(num)

index=0
for element in less_arr:
    if index==len(less_arr)-1:
        print(element)
    else:
        print(element, end=' ')   
    index+=1
    