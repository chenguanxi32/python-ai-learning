print('100-200=',100-200)

print('''line1
line2
line3''')
print(r'''hello,\n
world''')

print('I\'m \"ok\".')
print(r'I\'m \"ok\".')

BMI=input('please enter your BMI:')
if int(BMI)>24:
    print('pangzi')
else:
    print('zhengchang')

print(ord('a'))
print(chr(65))
print('abc'.encode('ascii'))
print('abc'.encode('utf-8'))
print(b'abc'.decode('ascii'))

print('小明的成绩提升了:%.1f%%'%((85-72)/72*100))
