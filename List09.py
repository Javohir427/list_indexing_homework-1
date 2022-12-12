def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a = list1[0]

    for i in list1:
        if i==a:
            x = True
        else:
            x = False
    return x

print(main([1, 0, 0, 0, 0]))