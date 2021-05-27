'''1.a的值是hello，b的值是world,如何交换a和b的值？
得到a的值为world，b的值是hello'''

# 1.2 python独特的
a = 'hello'
b = 'world'
a, b = b, a
print("a的值是：", a)
print("b的值是：", b)

# 1.1 中间变量-解决
a = 'hello'
b = 'world'
c = a
a = b
b = c
print("a的值是：", a)
print("b的值是：", b)
