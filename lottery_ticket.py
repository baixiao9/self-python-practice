# -*- coding: UTF-8 -*-
# 2018-06-21
# .中奖号码由6个红色球号码和1个蓝色球号码组成。 ...
	#random模块的用法
		#写一个函数，产生双色球号码,输入几就产生多少条，这些号码不能重复，要写到文件里面
		# 1个篮球         1-16
		# 6个红色球       1-33

import random

times = int(input("How much lottery do you want?"))

def rea_ball():
    red = []
    while len(red)<6:
        newone = random.randint(1, 33)
        if newone in red:
            continue
        else:
            red.append(newone)
            line = sorted(red)
    return (line)

for i in range(times):
    # red = [random.randint(1, 33) for _ in range(6)]
    # red = r.sort() 为什么不好使，注意.sort()和sorted的用法
    # new = sorted(red_ball)
    blue = random.randint(1, 16)
    print("%s:%s %s" %(i+1,rea_ball(),blue))

#参考信息：
# print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
# print( random.random() )             # 产生 0 到 1 之间的随机浮点数
# print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
# print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
#
# a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
# random.shuffle(a)
# print(a)
# https://zhidao.baidu.com/question/516550997.html 关于一次性取出多个随机数，看不懂