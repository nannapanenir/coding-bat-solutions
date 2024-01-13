"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

def front_back(str):
  
  if len(str) == 1:
    return str
  elif len(str) == 2:
    return str[::-1]
  else:
    r = ''
    front = str[:1]
    back = str[len(str)-1:]
    r += back  
    r += str[1:len(str)-1]  
    r += front  
    return r  
