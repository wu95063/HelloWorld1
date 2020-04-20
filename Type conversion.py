#type是显示数据类型的函数。
print(type(12))#->输出为<class 'int'>(integer),表示12这个数字是一个整数型。
print(type(12.5))#->输出为<class 'float'(float),表示12.5这个数字是一个浮点型。
print(type('王大锤'))#->输出为<class 'str'（string）,表示'王大锤'这个名字是一个字符串。
a=3
b=4
print(a<b)#->输出为True,因为a<b这个条件为真，所以输出为True.
#再说就是type conversion,即为类型转换。
print(type(a<b))#->输出为<class 'bool'（boll布尔类型）,表示a<b是一个布尔类型的数据。
number1=12
print(float(number1))#->输出为12.0，整数型变成了浮点型，这就是float函数的作用，即将整数型的数据类型转换成浮点型
number2=12.2
print(int(number2))#->输出为12，同理一个浮点型的数字变成了整数。
print('王大锤'+str(2))#->输出为王大锤2，这是一个字符串，通过str函数将2转换成为整数型，然后对两个字符串进行了拼接。




