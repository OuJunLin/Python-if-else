n, a1, a2, a3 = map(int, input().split())
n2 = 0
coin = [50, 5, 1]
count = [0, 0, 0]

if n > a1*15+a2*20+a3*30:  
    n2 = n-(a1*15+a2*20+a3*30)
    for i in range(len(coin)):
        count[i] = n2 // coin[i]
        n2 = n2 % coin[i]
        if n2 == 0:
            break
else:
    print("0")

for i in range(2, -1, -1):
    print(count[i])