def iq_test(numbers):
    list = map(lambda num: int(num) % 2, numbers.strip().split(" "))
    # list = [int(i) % 2 == 0 for i in numbers.split()]
    # if list.count(1) == 1: return list.index(1) + 1
    # else: return list.index(0) + 1
    return list.index(1) + 1 if list.count(1) else list.index(0) + 1