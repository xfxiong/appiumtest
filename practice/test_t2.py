'''
回文的定义：回文就是正读倒读都一样的
如奇数个：'98789'，正读和倒读都是一样的，偶数个数字'3223'也是回文数，字母'abcba'也是回文,
判断一个字符串是否是回文字符串，是打印true，不是打印false
'''
a = 'abcba'

# 1.切片,前闭后开 步长为-1 反转字符串
# print(a[:2:])   #print(a[0:2:1]),print(a[::-1])
print(a == a[::-1])

# 2.reversed
# b =reversed(a) #reversed object 迭代器 next() ['a','b','c','b','a']
# print(b)
# c ="".join(b)
print(a == "".join(reversed(a)))
