# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 5-27
def make_steak(d,*other):
    '''做一份牛排'''
    print('Make a steak well done in %d ' % d + 'with the other:')
    for o in other:
        print('- '+o)


# 代码 5-28
import steak
steak.make_steak(9,'salad')
steak.make_steak(8,'red wine','salad','coffee')


# 代码 5-29
from steak import make_steak
make_steak(9,'salad')
make_steak(8,'red wine','salad','coffee')

# 代码 5-30
from steak import make_steak
make_steak(9,'salad')
make_steak(8,'red wine','salad','coffee')

# 代码 5-31
from steak import make_steak as ms
ms(9,'salad')
ms(8,'red wine','salad','coffee')

# 代码 5-32
import steak as S
S.make_steak(9,'salad')
S.make_steak(8,'red wine','salad','coffee')