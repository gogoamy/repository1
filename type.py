# -*- coding: utf-8 -*-



# Number类型（int, float, boolean, complex）
print('Number类型（int, float, boolean, complex）')


a = 10                      
print('整形(int) a = ',a)


b = 10.2                    
print('浮点型(float) b = ',b)


c = 1.5e11                 
print('浮点型,科学计数法(float) c = ',c)


d = True                   
print('布尔型(boolean) d = ',d)


e = False                   
print('布尔型(boolean) e = ',e)


f = 3.14j                   
print('复数(complex) f = ',f)

g = complex(1.2,2.3)        
print('复数(complex) g = ',g)


print()
print()
print()


# String类型
print('String类型')


s1 = 'hello'
print('String类型 s1 = ',s1)

s2 = "let's go"
print('String类型 s2 = ',s2)



# 转义符号\，\n,\t
s3 = 'let\'s go'           
print('String类型 s3 = ',s3)


s4 = 'abc\ncba'             
print('String类型 s4 = ',s4)


s5 = '\\\t\\'
print('String类型 s5 = ',s5)


#跨越多行
s6 = '''abc
123
erf
ghj
tyu
'''
print('String类型 s6 = ',s6)


# 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数
s7 = 'hello world '*5
print('String类型 s7 = ',s7)


print()
print()
print()


# String中字符串检索
print('String中字符串检索')


test = 'hello'
print('test[0]: ',test[0])
print('test[1]: ',test[1])
print('test[2]: ',test[2])
print('test[3]: ',test[3])
print('test[4]: ',test[4])



# String中的切片
# str[x:y]: 输出从x位置开始的字符一直到y位置（不包括y）

print('test[0:2]: ',test[0:2])
print('test[2:4]: ',test[2:4])
print('test[2:5]: ',test[2:5])


# 索引切片可以有默认值，切片时，忽略第一个索引的话，默认为0
# 忽略第二个索引，默认为字符串的长度

print('test[:2]: ',test[:2])
print('test[2:]: ',test[2:])


# 索引也可以是负数，这将导致从右边开始计算

print('test[-1]: ',test[-1])
print('test[-2]: ',test[-2])
print('test[-3]: ',test[-3])
print('test[-4]: ',test[-4])
print('test[-5]: ',test[-5])


print('test[-2:]: ',test[-2:])
print('test[:-2]: ',test[:-2])


# 内置函数 len() 返回字符串长度

s = 'abcdefghijk'
print('字符串s的长度是： ',len(s))


print()
print()
print()


# 格式化字符串
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换
# 有几个%占位符，后面就跟几个变量或者值，顺序要对应好
print('格式化字符串')


print('hello,%s' % 'world')
print('your name is %s, your score is %d' % ('testing',98))
print('浮点数：%f' % 3.14)
print('浮点数：%.2f' % 3.14)
