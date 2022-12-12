def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a = []
    for i in list1:
        if i == 0 :
            a.append(False)
        else:
            a.append(i)

    return a
print(main([1,1,1,1,0,0,0,1]))