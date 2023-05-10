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

import random #random 전체를 가져옴
random.randrange(0,100,2)

from random import randrange as rr #random에서 import를 randrange만 가져와서 쓰겠다.
rr(0,100,3)

import random as rand # random을 as로 rand바꿔서 쓰겠다.

import mymodule as module
module.myfn1('my module import')
