# a = ["张三","李四","王五"]
# b = 0
# while b <= len(a)-1:
#     print("恭喜%s毕业" % a[b])
#     b += 1

# 100以内质数之和
a = 0
for b in range(2,101) :

    for c in range(2,b):
        if b % c == 0:
            break
    else:
        a = a + b
print(a)

#99乘法表
# for a in  range(1,10):
#     for b in range (1,a+1):
#         print("%d * %d = %d" % (a,b,a*b),end="\t")
#     print("")

#组成三个数，不重复
# for a in r):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a != b and a != c and b != c:
#                 print("%d%d%d" % (a,b,c))ange(1,5

#水仙花
# for a in range(2,1000):
#     b = a // 100
#     c = a % 100 // 10
#     d = a % 100 % 10 // 1
#     if b ** 3 + c ** 3 + d ** 3 == a:
#         print(a)
#

#100以奇数之和：
# for a in range(1,101,2):
#     for i in range (0,a):
#      if i % 2 == 1:
#          a = i + a
# print(a)

# 冒泡法排序：
a = [33,111,36,56]
for c in range(len(a)-1):
    for b in range(len(a)-1):
        if a[b] > a[b+1]:
            a[b],a[b+1] = a[b+1],a[b]
print(a)

#选择法
a = [33,111,36,77]
for c in range(len(a)-1):
    for b in range(c+1,len(a)):
        if a[c] > a[b]:
            a[c],a[b] = a[b],a[c]
print(a)



# 1 - 2 + 3 - 4 .... + 99
# b = 0
# c = 0
# for a in range(1,100):
#     if a % 2 == 0:
#         b = b - a
#     else:
#         c = c + a
# print(b + c)

# b = 0
# for a in range (1,101):
#     b = b + a
# print(b)

#a = 1
# b = 0
# while a <= 100:
#     b = b + a
#
#     a = a +1
# print(b)

# a = 1
# while a <= 9:
#     b = 1
#     while b <= a:
#         print("{} * {} = {}".format(a,b,a*b),end="\t")
#         b = b + 1
#     print("")
#     a += 1






print(sum(range(101)))