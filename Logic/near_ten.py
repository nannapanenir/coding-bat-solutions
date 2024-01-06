"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


near_ten(12) → True
near_ten(17) → False
near_ten(19) → True


Ex:

The number 31 is 1 away from 30, a multiple of 10. That number is within a distance of 2 from the nearest multiple of 10, so it meets the criterion.

The number 36 is 4 away from 40, the nearest multiple of 10, so it does not meet the criterion, because 4 is greater than 2.

So, subtract the number in question from the nearest multiple of 10, and compare the difference to 2. If it's greater than 2, it is not within 2 of a multiple of 10. If the difference is less than 2, it is within 2 of a multiple of 10.

look at the Test cases you will get clarity :

12 is true becase it isnear to 10 with mentioned distance which is 2
like wise 19 
"""

def near_ten(num):
   resul = num%10
   return True if resul in [1,2,9,8,0] else False