# -*- coding: utf-8 -*-
# 2018-06-21
# 写一个商品管理的程序的
	#1、添加商品
	#2、修改商品信息
	#3、查看商品
# 运行程序的时候，提示你 输入1、添加商品 输入2、修改商品信息 3、输入3、查看商品
# 输入其他的就提示输入错误
# 添加、修改商品前需要查看商品是否已经存在

import pickle

product_info = {'apple':['red','100','1'],'book':['orange','20','1']}
f = file('product.pkl','wb')
pickle.dump(product_info,f)
f.close()
# f = file("product.txt")

def search():
    line = raw_input("Which product would you want to see?")
    global line
    f = open('product.pkl', 'r+')
    product_info = pickle.load(f)
    f.close()
    if line in product_info:
        print(product_info[line])
    else:
        print("we don't have",line)
        return False

def insert():
    if search() == False:
        add_name = raw_input("Now you can insert, please input product name:")
        add_attribute = raw_input("Please input attribute of %s:" %(add_name)).split(",")
        product_info[add_name] = add_attribute
        # add_attribute need change
        print(product_info)

    else:
        print("We already have %s, you can not insert it." %(line))

def modify():
    if search() != False:
        # add_name = raw_input("Now you can modify, please input product name:")
        add_attribute = raw_input("Please input attribute of %s:" % (line)).split(",")
        product_info[line] = add_attribute
        # add_attribute need change
        print(product_info)
    else:
        print("We don't have %s, you can not modify it. Please try to add." %(line))

while True:
    input = int(raw_input("What do you want to do?\n"
                          "Press 1 for insert; press 2 for modify; press 3 for search.\n"
                          "Please input:"))
    if input == 1:
        insert()
    elif input == 2:
        modify()
    elif input == 3:
        search()
    else:
        input = raw_input("invalid input, please try again.")
    f = open('product.pkl', 'w+')
    pickle.dump(product_info,f)
    f.close()