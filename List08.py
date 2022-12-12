def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a = []
    for i in list1:
        if i==0:
            a.append(False)
        else :
            a.append(True)
    return a

print(main([1, 0, 0, 0, 0]))