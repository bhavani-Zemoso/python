def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    hash_table = dict()
    
    for i in range(0, len(str1)):
        if str1[i] in hash_table:
            hash_table[str1[i]] = hash_table.get(str1[i]) + 1
        else:
            hash_table[str1[i]] = 1
        
        if str2[i] in hash_table:
            hash_table[str2[i]] = hash_table.get(str2[i]) - 1
        else:
            hash_table[str2[i]] = -1
    
    for key in hash_table:
        if hash_table.get(key) != 0:
            return False
    
    return True

str1 = 'ababa'
str2 = 'ababc'
print(check_permutation(str1, str2))