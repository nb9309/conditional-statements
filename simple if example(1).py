s = input('enter value: ')
if s == s[::-1]:
    print('{} is palendrome'.format(s))
if s != s[::-1]:
    print('{} is not a palendrome'.format(s))
print('code executed')