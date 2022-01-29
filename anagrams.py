def validate_anagram(val1, val2):
    if [list(val1.lower())].sort() == [list(val2.lower())].sort():
        print('anagram..')

validate_anagram("Mary", "Army")