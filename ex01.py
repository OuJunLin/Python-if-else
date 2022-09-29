x_str = input()
x_1 = str( (int(x_str[2])+7)%10 )
x_2 = str( (int(x_str[3])+7)%10 )
x_3 = str( (int(x_str[0])+7)%10 )
x_4 = str( (int(x_str[1])+7)%10 )

print(x_1 + x_2 + x_3 + x_4)