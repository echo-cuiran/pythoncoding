# coding:utf-8


name = "XiaoMi Hello world"

# 将字符串的首字母大写，其他字母小写

print(name.capitalize())

print("————————————————————————————————————————")
# 将字符串全体小写

print(name.casefold())

print(name.lower())

print("————————————————————————————————————————")

# 将字符串全体大写

print(name.upper())

print("————————————————————————————————————————")

# 将字符串中大小写进行转换

print(name.swapcase())

print("————————————————————————————————————————")

# 为字符串定义长度，如不满足，缺少的部分用0填补

print(name.zfill(15))

print("————————————————————————————————————————")

# 返回当前字符串中某个成员（元素）的个数,如果查询的成员（元素）不存在，则返回0

print(name.count("l"))

print("————————————————————————————————————————")

# startswith 判断字符串开始是否是某成员（元素）
# endswith 判断字符串结尾是否是某成员(元素）

print(name.startswith("X"))
print(name.endswith("d"))

print("————————————————————————————————————————")

# find 与 index 都是返回你想寻找的成员的位置
# 如果find找不到元素，会返回-1
# 如果index 找不到元素，会导致程序报错

print(name.find("H"))
print(name.index("w"))

print("————————————————————————————————————————")

# strip 将去掉字符串左右两边的指定元素，默认是空格

print(" Hello word ".strip())
print("Hello word ".strip("H"))

print("————————————————————————————————————————")

# 将字符串中的old（旧元素）替换成new（新元素），并能指定替换的数量

print(name.replace("XiaoMi", "Xiaoming"))
print(name.replace("l", "L", 2))

print("————————————————————————————————————————")
# isspace 判断字符串是否是一个由空格组成的字符串
print(' '.isspace())

print("————————————————————————————————————————")

# istitle 判断字符串是否是一个标题类型
print(name.istitle())
print('Hello World'.istitle())

print("————————————————————————————————————————")

# isupper 判断字符串中的字母是否都是大写
print(name.isupper())
print('HELLO'.isupper())

print("————————————————————————————————————————")
# islower判断字符串中的字母是否都是小写
print('xiaomi'.islower())

print("————————————————————————————————————————")
# 字符串格式化

str_name = "小红"
age = 18
phone = 15227197021

print('我叫%s,今年%s岁，电话号码是：%s' % (str_name, age, phone))

print('我叫{},今年{}岁，电话号码是：{}'.format(str_name, age, phone))

print('我叫{0},今年{1}岁，电话号码是：{2}'.format(str_name, age, phone))

print(f'我叫{str_name},今年{age}岁，电话号码是：{phone}')