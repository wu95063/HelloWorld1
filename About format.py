#关于format函数的理解：format即是格式化的意思.
#而格式化字符串，在动态处理某些东西的情况下尤其有用。例如：
name='王大锤'
character=2
print(f'{name}{character}')#不管是什么东东，只要放到这个大括号里
                           #所有的变量类型都会被格式化成为字符串类型。
                           #大括号里的变量，是一种动态的对象，所以格式化字符串对于动态处理很有用。
                           #->王大锤2
#Another example:
Job=input('what\'s your career? ')
Year=input('from which year? ')
working_time=2020-int(Year)
Working_Experiences=(f'So you have {working_time} years working experiences as a {Job} ')
print(Working_Experiences)
print('Congratulations and Welcome to our company')
