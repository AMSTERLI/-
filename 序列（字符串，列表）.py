'''
索引
切片
序列相加
序列相乘
'''
verse=['自古逢秋悲寂寥，我言秋日胜春招']
verse_=['竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生']
print(verse+verse_)#序列加法
print(verse*2)#序列乘法
#使用称号实现初始化指定列表长度
_verse=['python']*4
print(_verse)
#检查元素是否为序列成员
#语法：value（要检查的元素） in sequence（指定的序列）
_verse_=['李炳乐','张楠彬','张克','丘家豪']
print('张楠彬'in _verse_)
print('张克'not in _verse_)
#计算序列的长度，最大值和最小值
num=[2,4,7,98,56,3,8,72]
print(len(num))#长度
print(max(num))#最大值
print(min(num))#最小值
'''
python内置函数
list()序列转换为列表 str（）序列转换为字符串 sum（）计算元素和
sorted（）对元素进行排序 reversed反序序列中的元素
enumerate（）将序列组合为一个索引序列，多在for循环中使用
'''
'''
字符串是Python当中最常用数据类型
1.认识字符串
2.下标
3.切片
'''
#下标的作用：使用编号精确找到数据--又称索或索引值
str1='abcdef'
print(str1[1])#从零开始编排
#切片的作用：截取操作对象中的一部分
'''
语法：str[开始位置下标:结束位置下标：步长]
不写开始值，代表开始值为0。不写步长，代表步长为1。
不写结束值，代表选取到最后。
如果值为负数，则表示倒叙选取。
'''
str2='libingle'
print(str2[0:3:1])
print(str2[-1:-4:-1])#重点：步长的正负应与选取的方向一致，否则不会选取
#1.查找
'''
查找子串在字符串中的位置或出现的次数
find（）检测某个子串是否包含在这个字符串中，
如果在返回这个子串开始的位置下标，否则返回-1
语法：str.find（所查找的子串，查找起始范围，查找最终范围）
'''
#find
mystr='znb zk lbl qjh zpz'
print(mystr.find('z',0,10))#找不到该子串会输出-1
#index
print(mystr.index('qjh',10,15))#如果找不到此子串则会报错substring(子串)not find
#count查找子串在字符串中出现次数
print(mystr.count('z',0,15))
#rfind,rindex从右侧开始查找下标顺序还是从左往右
print(mystr.rfind('z',0,15))
print(mystr.rindex('z',0,18))

#1,startswith判断开头
str='hello world and hello python'
print(str.startswith('h') )
print(type(str.startswith('h')))
#2，endswith判断结尾（顺序依然是从左往右）
print(str.endswith('no') )
#3，isalpha判断非空字符串，组成是否全部为字母
print(str.isalpha())#str字符串中又空格
#4，isdigit 组成是否全部为数字
str_='5201314'
print(str_.isdigit() )
#5,isalnum 组成是否为数字和字母
_str_='love1314'
print(_str_.isalnum() )
#6,isspace 组成是否为空白
_str='     '
print(_str.isspace())
'''
1.大小写转换
capitalize()使字符串第一个字母大写，其他全部小写
title()将字符串每个单词的开头大写
lower()所有大写转小写
upper()所有小写转大写
'''

'''
2.删除空白
lstrip()删除左侧空白
rstrip()删除右侧空白
strip()删除所有空白
'''

'''
3.对齐
rjust  右对齐  str.rjust(对应长度，'填充字符')
ljust  左......
center 居中......
'''
#2.修改
#replace(旧子串，新子串，替换次数)不写替换次数默认为全部
mystr_='znb and zk and zj and zyx'
print(mystr_.replace('z','l',))
#***原字符串数据不修改，调用replace函数输出的数据是其返回值
#得出结论：数据类型分为可变与不可变两类，而字符串属于不可变数据类型。
#split(分割字符，分割次数）返回一个列表，丢失分割字符
print(mystr_.split('and',2))
print(type(mystr_))
print(type(mystr_.split('and',2)))
#join（）合并列表里面的字符串为一个大的字符串
list=['aa','bb','cc','dd']
newlist=''.join(list)
print(newlist)
#列表
name1=['jack','lily','judy','sindy']
print(name1[0])
#index查找数据
print(name1.index('lily',0,3))
#count计算该元素在列表中的出现次数
print(name1.count('judy'))
#len计算列表所含元素数
print(len(name1))

#1,for循环实现
print('     ','秋词')
poem=['自古逢秋悲寂寥','我言秋日胜春朝','晴空一鹤排云上','便引诗情到碧霄']
for index,item in enumerate (poem):
    print(index,item)
print('     ','长歌行')
poem=['青青园中葵','朝露待日晞','阳春布德泽','万物生光辉','常恐秋节至','焜黄华叶衰','百川东到海',
      '何时复西归','少壮不努力','老大徒伤悲']
for index,item in enumerate (poem):
    if index%2==0:
        print(item+'，',end='')
    else:
        print(item+'。')

name=['zsy','lpf','lyj','wjh','lm']
print('wjh'in name)
print('zsy'not in name)
you_name=input('用户名：')
if you_name in name:
    print('该用户名已存在，请重试。')
else:
    print('注册成功!')

#append列表结尾追加数据
name2=['cxk','lx','ll','yy','dzq']
your_name=input('用户名：')
if your_name in name2:
    print('该用户名已存在，请重试。')
else:
    name.append(your_name)
    print('注册成功!')
print(name2)
#将一个列表中的所有元素添加到另一个列表中
allname=['wb']
allname.extend(name)
print(allname)
#修改
allname[1]='cb'
print(allname)
#删除
del allname[-1]
print(allname)
#根据元素值来删除(删除的元素不在其中时，会报错）
allname.remove('ll')
print(allname)
#计算
#count.
#index查找元素首次出现的位置（即索引）.
#sum求和sum（list）
#排序
num=[12,23,43,54,65,76,34,38,94]
num.sort()
print(num)

