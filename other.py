#encoding utf-8
# -*- coding: cp936 -*-
# -*- coding: utf-8 -*
f = open("/home/bigdou/PycharmProjects/untitled/produce.txt", "r")
while True:  
    line = f.readline()  
    if line:  
        #pass#�Ժ������ӵ�ʲô
        line=line.strip()
        with open('/home/bigdou/PycharmProjects/untitled/space traveler.txt') as file:
            k = 0
            for lines in file.readlines():
                if line in lines:
                    k = k + 1
            print k#���ÿ���ؼ����������г��ֵĴ���������Ѹñ��������������ۼ�����������������˺ö�鶼û�ɡ�
    else:  
        break
f.close()
