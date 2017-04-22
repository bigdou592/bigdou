#encoding:utf-8
aString = 'hello word'
bString = "tomorrow"
listString = str(range(4))
print listString
# [0, 1, 2, 3]
print aString[1]
print aString[-1]
print bString[1:5]
print bString[-3:-2]
print aString[0:6] + bString
firstSet = set([1, 2, 3])
secondSet = set([3, 4, 5])
print firstSet & secondSet
print firstSet | secondSet
print firstSet - secondSet
def power(x, n =2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
print power(2)
def my_abs(a,b):
    if a>b:
        return 1
    else:
        if a<b:
            return -1
        else:
            return 0
print my_abs(2,3)
print my_abs(3,2)
print my_abs(2,2)
file = open('/home/bigdou/文档', 'r')
for line in file.read():
    print line
