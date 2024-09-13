num = float(input('enter value: '))
if num == 0:
    print('{} is zero'.format(num))
if num == 1:
    print('{} is one'.format(num))
if num == 2:
    print('{} is two'.format(num))
if num == 3:
    print('{} is three'.format(num))
if num == 4:
    print('{} is 4'.format(num))
if num == 5:
    print('{} is five'.format(num))
if num == 6:
    print('{} is six'.format(num))
if num == 7:
    print('{} is seven'.format(num))
if num == 8:
    print('{} is eight'.format(num))
if num == 9:
    print('{} is nine'.format(num))
if num in (-1,-2,-3,-4,-5,-6,-7,-8,-9):
    print('{} is negitive digit'.format(num))
if (num<0) and (num not in (-1,-2,-3,-4,-5,-6,-7,-8,-9,-0)):
    print('{} is -ve number'.format(num))

if num > 9:
    print('{} is +ve number'.format(num))
print('program executed')
