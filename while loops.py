#使用while循环来多次使用代码块，这样有助于构建交互式程序和游戏。
#形式如下：
#while condition:
    #...#
    #当条件为真的时候，所输入的这句话，在这个块中会重复执行。
i=1
while i<=5:
    print(i)
    i+=1##如果不增加这个条件，我们会无限输出i=1这个值,因为这个条件将永远是真，一个总是小于5的数。
    #所以在每一个迭代循环中，我们把i增加1，所以在某一点上，i将达到6，然后条件为false.
    #我们跳出了循环。
    #上面两行缩进说明他们是while循环的一部分。
print('Done')#当跳出循环之后输出done


#Guessing game:
#三次猜测数字的机会，如果最终没有猜对，输出：你没有猜对。
# 如果有恰好有一次猜对了输出：你猜对了。
Guess_Number=input('Guess Number: ')
Guess=int(Guess_Number)
Right_Number=9
while Guess!=Right_Number:
    Guess=int(input('Please guess again: '))
else:
    print('you win !')
##上面这个程序，没有设定三次的猜测次数限制，现在让我们来更改这个程序。
Guess_count=0
Guess_number=int(input('猜猜我心里的数字是多少： '))
number=9
while Guess_count<3:
    Guess_count+=1
    if Guess_number==number:
        print('你赢了！')
        break#想要终止while循环，使用break终止。
    else:
        Guess_number = int(input('再猜一猜: '))
else:
    print('猜错喽，再玩一把？ ')#这里的代码会在while循环语句中被执行。
    #理解：如果玩家猜对了数字，你打破这个循环，你跳出他的代码，所以我们在else块中写入的代码不会被执行，
    #但是玩家如果用户不能猜测出这个数字，你就永远不会跳出来。
    #所以这个循环将被执行到完成，知道condition变成false,到这个时候else块中的代码将被执行。












