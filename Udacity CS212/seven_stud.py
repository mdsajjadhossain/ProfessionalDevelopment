# CS 212, hw1-1: 7-card stud
#
# -----------------
# User Instructions
#
# Write a function best_hand(hand) that takes a seven
# card hand as input and returns the best possible 5
# card hand. The itertools library has some functions
# that may help you solve this problem.
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools
import time

DECK = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def timedcall(fn, *args):
    "Call function and return eapsed time"
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def timedcalls(n, fn, *args):
    "Call function n times; return min, avg, max"
    times = [timedcall(fn, *args)[0]  for _ in range(n)]
    return min(times), sum(times) / float(n), max(times)

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.

def hand_rank(hand,depth=0):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    cnt = 8
    if cnt >= depth and straight(ranks) and flush(hand):
        return (8, max(ranks))
    cnt-=1
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 
def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand." 
    
    return max(itertools.combinations(hand, 5), key=hand_rank)

reds = [c  for c in DECK  if c[1] in 'DH']
blacks = [c  for c in DECK  if c[1] in 'SC']

##def best_wild_hand(hand):
##    "Try all values for jokers in all 5-card selections."
##    tmp, wild = [], []
##    for card in hand:
##        if card == '?R':
##            wild.append(list(reds))
##            continue
##        if card == '?B':
##            wild.append(list(blacks))
##            continue
##        tmp.append(card)
##
##    r = 5 - len(wild)
##    nonwild = list(itertools.combinations(tmp, r))
##    wild = list(itertools.product(*wild))
##    result = max((tuple(list(i) + list(j)) for i in nonwild  for j in wild) , key=hand_rank)
##    return result

def replacement(card):
    if card == '?B': return blacks
    elif card == '?R': return reds
    else: return [card]
    
def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    rawCombi = list(itertools.combinations(hand, 5))
    return max((j  for c in rawCombi
                for j in itertools.product(*map(replacement, c))),
               key=hand_rank)

def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'



#print sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
print timedcalls(30, test_best_wild_hand)



