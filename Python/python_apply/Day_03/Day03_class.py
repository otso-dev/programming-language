# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
class myclass:
    myvar1 = 10
    myvar2 = 'abc'
    
    def __init__(self,a = 0,b = 'aaa'):
        self.myvar1 = a
        self.myvar2 = b
    
    def mymethod1(self, n):
        print(self.myvar1 * n,self.myvar2)
    
    def __str__(self):
        return 'myclass: {},{}'.format(self.myvar1, self.myvar2)

a = myclass(100,'def')
print(a)
print(type(a))
a.mymethod1(5)


# -

class myclass2(myclass):
    def mymethod1(self, n):
        print('myclass2 - mymethod',self.myvar1 * n)
    def mymethod2(self):
        print('myclass2 - mymethod2')
b = myclass2()
b.mymethod1(10)
b.mymethod2()


def printlist(list,/):
    print(list)
list_1 = list('abcdefcghi')
list_1.remove('b')
printlist(list_1)


def list_remove_all(target_list, target_value):
    for i in target_list:
        if target_value == i:
            target_list.remove(target_value)
    return target_list
def list_remove_all_v1(target_list,target_value):
    while target_value in target_list:
        target_list.remove(target_value)
    return target_list
def list_remove_all_v2(target_list,target_value):
    while True:
        try:
            target_list.remove(target_value)
        except:
            return target_list
ret_list = list_remove_all_v2(list('abcdefcghi'),'c')
print(ret_list)


class mylist(list):
    def remove_all(self,target_value):
        while target_value in self:
            self.remove(target_value)
        return self
mylist_1 = mylist(list('abccdc'))
mylist_1.append(1)
mylist_1.append(2)
print(mylist_1)
print(mylist_1.remove_all('c'))
