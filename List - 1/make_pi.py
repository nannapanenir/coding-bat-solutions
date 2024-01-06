"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


make_pi() → [3, 1, 4]
"""
def make_pi():
    pi=int(3.14*100)

    li=[]
    while pi >0:
        temp=pi%10
        
        li.append(temp)
        pi//=10
    li.reverse()
    return li

  
