# 计算字符串中每个字符出现的次数
# setdefault() 方法调用确保存在count中键的默认值为0，这样执行第7行加法时就不会抛出KeyError错误。
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
# 优化输出格式 以下两个打印方式是等价的
print('pprint漂亮打印 ：')
pprint.pprint(count)
print('pprint文本作为字符串输出 ：')
print(pprint.pformat(count))