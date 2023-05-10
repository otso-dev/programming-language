#!/usr/bin/env python
# coding: utf-8

# In[106]:


import random as rand
list_a = [1,2,3,4,5,6]
rand.shuffle(list_a)
print(list_a)

def score_hand(hand):
    score = 0
    for card in hand:
        score = score + score_dict[card]
    return score


# In[17]:


suits = ['Clover','Diamond','Heart','Spade']
#rank = ['Ace','Jack','Queen','King']
rank = [str(i) for i in range(2,11)]
rank = ['Ace'] + rank + ['Jack','Queen','King']
print(suits)
print(rank)


# In[122]:


Deck = []

for e in suits:
    for i in rank:
        Deck.append(e + '-' + i)
#print(Deck)
score_list = [i+1 for i in range(10)]
score_list = score_list + [10]*3
score_list = score_list *4
score_dict = dict(zip(Deck,score_list))
print(score_dict)
#print(score_list)
rand.shuffle(Deck)
#print(Deck)


# In[124]:


print('Game Start\n')
rand.shuffle(Deck)
print('Dealer Hands')
dealer_hand = [Deck.pop() for _ in range(2)]
delear_sum = score_hand(dealer_hand)
print(dealer_hand, score_hand(dealer_hand))
print('\n\nPlayer Hands')
Player_hand = [Deck.pop() for _ in range(2)]

print(Player_hand, score_hand(Player_hand))

if score_hand(Player_hand) < 21:
    ans = int(input('Deal(1)or Stop(0):'))
    if ans == 1:
        Player_hand.append(Deck.pop())
        Player_sum = score_hand(Player_hand)
        print(Player_hand,Player_sum)
    elif ans == 0:
        break

# 승부 표시
if Player_sum > 21:
    print('you lose')
elif dealer_sum > Player_sum:
    print('you lose')
else:
    print('you win')

