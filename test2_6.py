a = int(input('введите четырехзначное число: ')) 
number = list(str(a))
if number[0] > number[1] > number[2] > number[3]:
    print('da')
else:
    print('net')

