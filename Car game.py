Input_some=input('> ')
while Input_some!='quit':
    if Input_some==('help'):
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
    else:
        print('i do not understand...')
        Input_some = input('>')
else:
    print('to exit')







#这是一个需要被循环的输出项，所以放在while里面。
 #Input_some=input('> ')
