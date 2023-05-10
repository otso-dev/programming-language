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
# 1000아래 모든 소수를 찾기
n = 2
list_prime = []
for n in range(2,1000):
    prime_flag = True
    for i in range(2,n):
        if n % i == 0:
            prime_flag = False
            break
    if prime_flag == True:
        #print(n,'prime')
        list_prime.append(n)

print(list_prime)
    

# -



prime_list = []
for n in range(2, 1000):
    flag = 0
    for i in range(2,n):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        prime_list.append(n)
print(prime_list)


# +
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
def is_prime_List(arg):
    list_prime = []
    for n in range(2, arg):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            list_prime.append(n)
    return list_prime

prime = is_prime(23) #returns true
Not_prime = is_prime(24) #return false
print(prime,Not_prime)
print(is_prime_List(500))
# -

prime_list = []
for i in range(2,100):
    if is_prime(i) == True:
        prime_list.append(i)
print(prime_list)
