height, sex = map(int, input().split())

if sex == 1:
    print("{:.1f}" .format((height-80)*0.7))
elif sex == 2:
    print("{:.1f}" .format((height-70)*0.6))