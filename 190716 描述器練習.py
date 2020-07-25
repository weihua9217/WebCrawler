class Human(object):
    height = 180

    def __init__(self, height, age):
        self.height = height
        self.weight = 60
        self.age = age

    def get_age(self):
        return self.age

# @property
# def weight(self):
# return 60

# @weight.setter
# def weight(self, weight):
# raise Exception('不可改變')

# @weight.deleter
# def weight(self):
# raise Exception('不可刪除')

# 覆寫__getattribute__，改變原本的行為
    def __getattribute__(self, attrname):
        if attrname == 'weight':
            return 50
        return super(Human, self).__getattribute__(attrname)

    def __setattr__(self, attrname, value):
        if attrname == 'weight':
            object.__setattr__(self, attrname, value-10)
        else:
            object.__setattr__(self, attrname, value)

    def __delattr__(self, attrname):
        if attrname == 'weight':
            print('已刪除你的體重')
            return object.__delattr__(self, attrname)

    def del_weight(self):
        del self.weight

    # def __call__(self, key):
        # try:
            # return self[key]
        # except KeyError:
            # return None


Matthew = Human(170, 20)
# print(Human.__dict__['get_age'])
# print(Matthew.get_age())
# print(Human.get_age(Matthew))
# print(Matthew.get_age)
# print(Human.__dict__['get_age'].__get__(Matthew, Human)())
# print(Human.__dict__)
# Matthew.weight = 100
print(Matthew.weight)
Human.del_weight(Matthew)
print(Matthew.weight)
Matthew.height = 172
print(Matthew.height)




