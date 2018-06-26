#-*- coding: utf-8 -*-
# 2018-06-22
# 公交卡计算

sum = 0
for _ in range(30):
    for i in [2.5,5]:
        if sum < 100:
            sum = i + sum
        elif 100<=sum<150:
            sum = 0.8*i + sum
        elif sum>= 150:
            sum = 0.5*i +sum
print('Totally cost:%s' %(sum))
