#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  encyr.py
#  
#  Copyright 2014 Ericson Willians <ericsonwrp@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import string

s0 = dict({(string.ascii_uppercase[x], x) for x in range(len(string.ascii_uppercase))})
s1 = dict({(x, string.ascii_uppercase[x]) for x in range(len(string.ascii_uppercase))})
limit = len(s0)

class EnCyr():
    
    def __init__(self, m, key):
        
        self.data = []
        self.encrypt(m, key)
    
    def encrypt(self, m, key, index=0, result=[]):
        if key < limit:
            if index >= len(m):
                self.data = result
            else:
                _sum = s0[m[index].upper()] + key
                if _sum >= limit:
                    _sum = _sum - limit
                self.encrypt(m, key, index+1, result+[s1[_sum]])
    
    def __call__(self):
        return ''.join(self.data)
    
    def __str__(self):
        return ''.join(self.data)
        
class DeCyr():
    
    def __init__(self, m, key):
        
        self.data = []
        self.decrypt(m, key)
    
    def decrypt(self, m, key, index=0, result=[]):
        if key < limit:
            if index >= len(m):
                self.data = result
            else:
                sub = s0[m[index].upper()] - key
                if sub <= 0:
                    sub = sub + limit
                self.decrypt(m, key, index+1, result+[s1[(lambda: sub if sub != limit else 0)()]])
    
    def __call__(self):
        return ''.join(self.data)
    
    def __str__(self):
        return ''.join(self.data)
        
if __name__ == "__main__":
    
    msg = EnCyr("Topsecretmessage", 13)
    print msg
    # decoded = DeCyr(msg(), 13)
    # print decoded
