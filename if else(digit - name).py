num = int(input('enter value:'))
if num == 0:
    print('{} is zero'.format(num))
elif num == 1:
    print('{} is one'.format(num))
elif num == 2:
    print('{} is two'.format(num))
elif num == 3:
    print('{} is three'.format(num))
elif num == 4:
    print('{} is four'.format(num))
elif num == 5:
    print('{} is five'.format(num))
elif num == 6:
    print('{} is six'.format(num))
elif num == 7:
    print('{} is seven'.format(num))
elif num == 8:
    print('{} is eight'.format(num))
elif num == 9:
    print('{} is nine'.format(num))
elif num in range(-1,-10):
    print('{} is -ve digit'.format(num))
elif num > 0:
    print('{} is +ve number'.format(num))
else:
    print('{} is -ve number'.format(num))