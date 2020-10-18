"""
hasattr(obj, attr):
这个方法用于检查obj是否有一个名为attr的值的属性，返回一个布尔值。
getattr(obj, attr):
调用这个方法将返回obj中名为attr值的属性的值，例如如果attr为'bar'，则返回obj.bar。
setattr(obj, attr, val):
调用这个方法将给obj的名为attr的值的属性赋值为val。例如如果attr为'bar'，则相当于obj.bar = val
delattr(obj, attr)
删除某个属性或者方法
"""
# 类
class Person(object):
    # 构造方法：实例化对象时自动执行
    def __init__(self, name):
        # 属性
        self.name = name
    # 方法
    def eat(self):
        return  'eating.....'


# 反射/自省： 判断对象是否有某一个属性或者方法, 获取属性或者方法， 设置属性或者方法，删除属性或者方法。
p = Person('小明')
print("是否有name属性: ", hasattr(p, 'name'))
print("是否有age属性: ", hasattr(p, 'age'))
print("是否有eat方法: ", hasattr(p, 'eat'))
print("是否有learning方法: ", hasattr(p, 'learning'))
if hasattr(p, 'name'):
    print("有name属性, name属性的值是: ", getattr(p, 'name'))
else:
    print("没有name属性, 正在设置......")
    setattr(p, 'name', '郭家星')
    print("有name属性, name属性的值是: ", getattr(p, 'name'))

if hasattr(p, 'age'):
    print("有age属性, age属性的值是: ", getattr(p, 'age'))
else:
    print("没有age属性, 正在设置......")
    setattr(p, 'age', 18)
    print("设置成功，  age属性的值是: ", getattr(p, 'age'))