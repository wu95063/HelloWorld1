#写代码的时候经常会调用函数，如：
name='PytHon'
print(len(name))#->输出的是字符串python的长度：6
type1=len(name)#定义了一个type的函数。
print(type(type1))#像print;len;type这些函数都是python的内建函数，是具有通用性的。
#len函数不仅可以计算字符串的长度还可以计算列表中项目的数量，但是不能计算整数型的长度，因为整数型没有长度。
list=[1,2,3,5,7,9,]#定义了一个列表变量。
print(len(list))#输出为列表项目的数量：6
#区别于这些内建函数（builtins），方法(methods)对应于不同的数据类型，如：
name.upper()#（name（一个被定义为字符串的变量））将所有的字符串变成大写，这里的upper即为一个method
name.lower()#将所有的字符串变成小写，这里的lower即为一个method
print(name.lower())#输出全部变成小写。（可以理解为：输出'使用了方法的name变量'）
print(name.upper())#输出全部变成大写。
name.find('P')#-->0
name.find('O')#--->-1
name.repalce('P','T')#-->
#iin 操作符
print('PytHon' in name )#-->True.








