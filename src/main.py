"""
Author: Reza Omidi
Date Created: 5/4/2025
"""

def happy_num(n: int):
    """
    Happy Numbers

    :param n: Input Number
    :return: True if number is a happy number, else False
    """          
    seen_num: set[int] = set()
    while n != 1 and (n not in seen_num):
        seen_num.add(n)
        n = sum(int(i)**2 for i in str(n))
        
    return n == 1    


if __name__ == '__main__':
    assert happy_num(7) is True
    assert happy_num(10) is True
    assert happy_num(13) is True
    assert happy_num(19) is True

    assert happy_num(4) is False
    assert happy_num(16) is False
    assert happy_num(20) is False
    assert happy_num(123) is False

    print('successfully!')
