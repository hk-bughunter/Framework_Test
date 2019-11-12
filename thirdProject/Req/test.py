# 1、用一行代码实现 1- 100之和
# 出题意义Python之禅有一条 简单胜于复杂 参考答案 利用sum()函数求和
a = sum(list(range(1,101)))
print(a)
print(sum(list(range(1,101,1))))
# 非一行代码实现的方案是编写循环,定义一个函数
lista = list(range(1,101,2))
print(sum(lista))