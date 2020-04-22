Input_some=input('> ')
while Input_some!='quit':#while循环开始
    if Input_some==('help'):#if statement
        print('''
start-start the car
top-stop the car
quit-exit the system
''')
        Input_some = input('>')
    elif Input_some==('start'):
        print('start the car')
        Input_some = input('>')
    elif Input_some==('stop'):
        print('stop the car')
        Input_some = input('>')
    else:#ifd的else
        print('i do not understand...')
        Input_some = input('>')
else:#while 循环结束
    print('to exit')







#这是一个需要被循环的输出项，所以放在while里面。
 #Input_some=input('> ')
