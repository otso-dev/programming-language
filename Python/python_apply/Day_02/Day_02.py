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
#함수
#define

def fuction_name():
    print('myfuction')

fuction_name()


# +
# fuction argument
def myfn1():
    print('myfn1')
def myfn2(arg1):
    print(arg1)
def myfn3(arg1= 'a',arg2 = 'b'):
    print(arg1,arg2)
def myfn4(*arg1): # 매개변수를 몇개를 줘야할지 모를때 
    for i in arg1:
        print(i)

# keyword function
def myfn5(arg1,*,arg2,arg3):# *이후에 매개변수는 인자를 받을 때 반드시 명시해줘야한다.
    print(arg1,arg2,arg3)
def myfn6(arg1, /, arg2,arg3):# / 앞쪽부터 positinal funtion으로 사용하겠다.
    print(arg1,arg2,arg3)
def myfn7(arg1,arg2):
    print(arg1)
    arg2('abc','def')
a = 1
list_a = [1,2,3,4,5,'list_a',{1,2,3,4},(1,2,3,4)]
#myfn2(list_a)
#myfn3(10,20)
#myfn3(arg2 = 10, arg1 = 20) 매개변수에 명시 해준다면 순서가 상관없다.
#myfn3() 매개변수에 default 값을 준다면 값을 넣어주지 않아도 된다.
#myfn4(1,2,3,4) -> (tuple)로 리턴함
#myfn2([1,2,3,4])
#myfn5('a',arg2 = 'b',arg3 = 'c')
#myfn5(arg3 = 'a', arg1= 'c', arg2 = 'b')
#myfn6('a','b','c')
#myfn6('a','c','c')
#myfn7('fn7 start',myfn3)

# +
# fuction return
def myfn8():
    print('myfn8')
def myfn9():
    return 10
def myfn10():
    return 10,20
#ret_value = myfn8()
ret_value = myfn10()
print(ret_value)


