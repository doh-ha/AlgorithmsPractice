n,k=map(int,input().split())
coin_type=[]
cnt=0

for i in range(n):
    coin_type.append(int(input()))

coin_type.sort(reverse=True)

for coin in coin_type:
    if k>=coin:
        cnt+=k//coin
        k%=coin

print(cnt)