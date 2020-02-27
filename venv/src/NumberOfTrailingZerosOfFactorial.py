def zeros(n):
    k = 1
    result = 0
    while(5**k <= n):
        result += n//(5**k)
        k += 1
    return result
#   x = n/5
#   return x+zeros(x) if x else 0



# Number of trailing zeros of N!
#
# 5 kyu
#
# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
#
# N! = 1 * 2 * 3 * ... * N
#
# Be careful 1000! has 2568 digits...
#
# For more info, see: http://mathworld.wolfram.com/Factorial.html
#
# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
#
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.