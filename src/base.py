"""Changing bases."""

from operator import is_


digits = {}

for i in range(0, 10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'

def change_to_base(n: int, b: int) -> str:
    """
    Return `n` in base `b`.

    The base `b` must be in the range 2 to 16.

    >>> change_to_base(1, 2)
    '1'
    >>> change_to_base(31, 2)
    '11111'
    >>> change_to_base(31, 8)
    '37'
    >>> change_to_base(31, 16)
    '1F'
    """
    assert 2 <= b <= 16
    lst = []
    ## assert 0/negative values
    is_negative = 0
    if n == 0:
        return "0"
    elif n < 0 : 
        n = -n
        is_negative = True
    
    ## change base
    while n != 0:
        lst.append(digits[n % b]) ## transform the "last" number from the right
        n = n // b
        
    lst =  lst[::-1]
    
    if is_negative: 
        return "-".join(lst)
    else:
        return "".join(lst)  



    
  