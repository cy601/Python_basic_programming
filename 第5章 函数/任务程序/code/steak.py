# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:40:08 2017

@author: Dell
"""

def make_steak(d,*other):
    '''做一份牛排'''
    print('Make a steak well done in %d ' % d + 'with the other:')
    for o in other:
        print('- '+o)

make_steak(1,)