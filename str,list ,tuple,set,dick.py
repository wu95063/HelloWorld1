#str(字符串)，list(列表)，tuple(元组) 专业名词叫：序列类型。
a='hello world'[1]
print(a)
print(3 in (1,2,3))
print(ord('w'))
#set(集合)：集合无序且不重复。
set2={1,2,3}
print(set2)
set1={1,2,2,2,3,5}
print(set1)
set2={1,2,3}
#print(set)会报错TypeError: 'set' object is not subscriptable。
q={1,2,3,4,5}
t={3,4}
print(q-t)##求两个集合的差集。
print(q&t)##求交集。
print(q|t)##求并集。
#空集：c=set()
s=set()
print(type(s))
len(set())##无即为空。
#dick（字典）也属于集合类型：类似于set，无序的且不能重复（对于key来讲），由key和value组成。
#字典基本的定义方式：{key1:value1,key2:value2,key3:value3,...}
dick1={1:1,2:2,3:3}#最常用的操作就是通过key(关键字) 得到/访问 value。
print(type(dick1))
dick2={1:'王丹',2:'丽丽',3:'李伟'}[1]
print(dick2) #输出'王丹'。
##dick中的key要求是不可变的，所以可以用int/str/tuple等来当key，但是list就不可以，因为列表是可变的类型。
#空的字典。{}
type({})
print(type({}))##dick