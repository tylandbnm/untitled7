

my_str = "my name is %s " % ('lisi')
print(my_str)

my_str1= "张三今年 %d 岁 " % (25)
print(my_str1)


my_str2= "一斤苹果 %f 元 " % (5.3)
print(my_str2)

my_str3= "一斤苹果 %12.2f 元 " % (5.388)
print(my_str3)

my_str4= "一斤苹果 %-12.2f 元 " % (5.388)
print(my_str4)

my_str5= "一斤苹果 %+12.2f 元 " % (5.388)
print(my_str5)

my_str6= "一斤苹果 %012.2f 元 " % (5.388)
print(my_str6)




my_str7={ }.format(7)
print(my_str7)


{}{}.format()

# 使用format去格式化 ： "{}".format("字符串")
my_str8 = "张三 今年 {} 岁".format(25)
print(my_str8)

# format格式化两个参数 ：" {}  {}".format(参数1,参数2)
my_str9 = "今天星期{}，张三买了{}斤苹果".format('一','5')
print(my_str9)

# fomrat的位置参数 ： "{0}{2}{1}{3}".format(第一个数,第二个数,第三个数,第四个数)
my_str10 = "今天星期{0}，张三买了{1}斤苹果".format('一','5')
print(my_str10)


# format的关键字参数 ： "{x}{y}".format(x='hello',y='world')
my_str11 = "今天星期{x}，张三买了{y}斤苹果".format(y='2',x='五')
print(my_str11)

# 位置参数和关键字参数结合使用 ："{0}{x}".format('hello',x='world')
my_str12 = "今天星期{0}，张三买了{x}斤苹果".format('2',x='五')
print(my_str12)