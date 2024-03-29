#1.1 implement a recursive function to calculate the factorial of a given number

"""
1! = 1 * 1
2! = 2 * 1! --->2 * 1
3! = 3 * 2! --->3 * 2 * 1
.
.
10! = 10 * 9! ---> 10 * 9 * 8 *...* 1

formula - n * (n-1)!
"""


def fact_rec(n):
  if n==0 or n==1:
     return 1
  else:
    return n*fact_rec(n-1)
    
number = int(input("Enter a value : "))
res = fact_rec(number)

print("the factorial of {} is {}.".format(number,res))