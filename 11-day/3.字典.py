id = {"姓名":"张轩轩","性别":"女","民族":"回族","年龄":19}
print(id)

#增加
id['地址'] = "新乡市"
id['身份证号'] = 123456
id.setdefault("爱好","睡觉")
print(id)

#删除
id.pop('地址')
id.popitem()#随机删除
print(id)

#修改
id['姓名'] = "轩轩"
print(id)

#查找

print(id['姓名'])
print(id.get("姓名"))

#合并
id = {'name':'xuan''age':12}

