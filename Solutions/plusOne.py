#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.


def plusOne(digits):
    fin = ""
    for x in digits:
        fin += str(x)
    ans = str(int(fin) + 1)
    res = [int(j) for j in str(ans)]
    print(res)


plusOne([1,2,3])