print('what is your name? ')#单引号内输入字符串
print('what\'s your name? ')#当单引号内部出现单引号的时候，需要运用转义符(\).
print("what's your name? ")#双引号内输入字符串
print('The question is "what is your name "')#单引号内部出现双引号是允许的，并且双引号变为字符串。
print('''
Hello you guys,
    My name is Michael Chen and i'm so happy to join
github.
    So let's get started.
                                            your sincerely
                                            Michael Chen
''')#（'''  '''）或者（""""""）三引号支持多行的书写，如果我们需要书信的格式，可以运用三引号来输出字符串。
#关于python再字符串中的一些特定--中括号的使用，即为一种---索引功能。
name='python'
    # 012345
    # -6-5-4-3-2-1
print(name[0])#->p
print(name[-1])#->n
print(name[-6])#->p
print(name[0:3])#->pyt
print(name[0:-1])#->pytho(不包括【-1】)
print(name[0:10])#->python
print(name[0:6])#->python
print(name[0:5])#->pytho
print(name[0:100])#->python
print(name[-1:-10])#->输出为空=print('')
print(name[:])#->python
another=name[:]#定义一个变量。
print(another)#->python



