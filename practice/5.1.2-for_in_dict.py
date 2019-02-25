spam = {'color': 'red', 'age': 42}
print("this is spam's values :")
for v in spam.values():
    print(v)

print("this is spam's keys :")
for k in spam.keys():
    print(k)

print("this is spam's items :")
for i in spam.items():
    print(i)

print("字典中结果组成列表 ：")
print(list(spam.keys()))
print(list(spam.values()))
print(list(spam.items()))

# in & not in 检查键值是否在字典中
# 当对比 key 的时候才可以简写为字典本身
print('color' in spam.keys()) # True
print('color' in spam) # True
print('red' in spam.values()) # True
print('red' in spam) # False

