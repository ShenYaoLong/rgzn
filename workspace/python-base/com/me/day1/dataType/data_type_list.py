'''
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
'''

list = ['abcd', 786, 2.23, 'runobb', 70.2]
tinyList = [123, 'runoob']
print(list)                 # 输出完整列表
print(list[0])              # 输出列表第一个元素
print(list[1:3])            # 从第二个开始输出到第三个元素
print(list[2:])             # 输出从第三个元素开始的所有元素
print(list[2::2])           # 输出从第三个元素开始的所有元素，并设置步长为2
print(tinyList * 2)         # 输出两次列表
print(list + tinyList)      # 连接列表
list.append(1)              # 列表添加元素
print(list)
print(list.pop(0))          # 列表弹出下标为0的元素
print(list)

# list中的元素是可以改变的

'''
List 内置了有很多方法，例如 append()、pop() 等等，这在后面会讲到。

注意：

1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。

列表截取可以接收第三个参数，参数作用是截取的步长
'''
