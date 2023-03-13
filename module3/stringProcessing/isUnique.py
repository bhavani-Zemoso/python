def is_unique(string):
    string = string.lower()

    hash_table = dict()

    for character in string:
        if character in hash_table:
            return False
        else:
            hash_table[character] = 1

    return True

string = "bbcdef"
print(is_unique(string))

