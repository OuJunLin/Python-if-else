hr1, min1 = map(int, input().split())
hr2, min2 = map(int, input().split()) 
time1 = abs((hr1*60+min1)-(hr2*60+min2))

if time1 <= 120:
    print("{:d}" .format((time1//30)*30))
elif time1 <= 240:
    print("{:d}" .format(((time1-120)//30)*40+120))
else:
    print("{:d}" .format(((time1-240)//30)*60+280))