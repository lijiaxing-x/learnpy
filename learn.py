

print("hola")
#wo xie lai play play
'''
BUZZ & WOODY are best friends
'''
if True:
    print("1st")
    print("BUZZ LIGHTYEAR")
else:
    print("answer")
    print("false")
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
    item_two + \
        item_three
if total == 6:
    print("WOODY")
else:
        print("hh")
days = ['SUN','MON','TUE',
'WED','THUR']
print(days[2])

#input("按下ENTER退出，其他键显示。。。\n")

#创建类
'''
class classname:
    class_suite 
'''
class employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", salary: ", self.salary)
"创建 Employee第一个对象,访问属性"
emp1 = employee("Woody", 10)
emp2 = employee("BUZZ", 20)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % employee.empCount)

emp1.age = 7
emp1.age = 8
#del emp1.age
print(hasattr(emp1, 'age'))#has attribute
print(getattr(emp1,'age'))
setattr(emp1,'age', 10)
print(emp1.age)
print("Employee._doc_:",employee.__doc__)
print("employee._name_:",employee.__name__)
print("employee._module_:",employee.__module__)
print("employee._bases_:",employee.__bases__)
print("employee._dict_:",employee.__dict__)