"""
forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""
def sorta_sum(a, b):
  return  20 if 9 <a+b <=19 else a+b 
