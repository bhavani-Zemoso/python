def count_low_high(num_list):
    if (len(num_list)==0):
        return None
    high_list = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
    low_list = list(filter(lambda n: n <= 50 and not n % 3 == 0, num_list))
    return [len(low_list), len(high_list)]


num_list = [20, 9, 51, 81, 50, 42, 77]

print(count_low_high(num_list))
