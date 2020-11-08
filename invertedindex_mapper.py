# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:53:24 2020

@author: kvija
"""
import re
def mapper_ii(data,f):
    # remove puncuation
    data = ''.join(data)
    data = re.sub(r'([^\s\w]|_)+', '', data)
    return [(word.lower().strip(),f) for word in data.split()]