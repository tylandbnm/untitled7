


alst=[]
blst=[11,23,'hds',None]

print(alst)
print(blst)

for x in blst:
    print("列表中的值",x)

clst = ['red','green','blue']

clst.append('black')
print('使用append添加元素后的列表：',clst)

clst.extend(blst)
print("追加blst后的结果:",clst)

clst.reverse()
print('翻转后的结果:',clst)

# clst.sort()
# print("排序后的结果:",clst)
# 同一数据类型才能进行排序

print(clst.count('blue'))
# 统计在列表中出现的次数
print(clst.index('black'))
# 从列表中找出某元素的位置

clst.insert(1,'hello')
print(clst)


for x in range(2,11,2):
    print(x)