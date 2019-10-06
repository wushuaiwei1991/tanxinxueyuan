# 输入我要加密的字符串
message = input("please input your message >>>>")

# 加密过程
# 声明一个变量用来存放加密后的结果
result = ""
for char in message:
    value = ord(char)
    # 这里使用|将字符串result进行分割
    result += str(value) + "|"
print("加密后的数据>>>>>" + result)

# 这里去掉|，结果是一个数组
index_list = result.split("|")
print(index_list)

# 移除数据中的空元素
index_list.remove("")
print(index_list)

# 解密过程
# 声明一个变量用来存放解密后的结果
response_result = ""

# 遍历我的数组
for index in index_list:
    # 数组中的字符串转成int值
    int_index = int(index)
    response_result += chr(int_index)
print("解密后的数据>>>>>" + response_result)
