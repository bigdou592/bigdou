#encoding utf-8
# -*- coding: cp936 -*-
# -*- coding: utf-8 -*
f = open("/home/bigdou/PycharmProjects/untitled/produce.txt", "r")
while True:  
    line = f.readline()  
    if line:  
        #pass#以后可以添加点什么
        line=line.strip()
        with open('/home/bigdou/PycharmProjects/untitled/space traveler.txt') as file:
            k = 0
            for lines in file.readlines():
                if line in lines:
                    k = k + 1
            print k#输出每个关键词在评论中出现的次数，我想把该变量放在数组里累加起来再输出，我试了好多遍都没成。
    else:  
        break
f.close()
