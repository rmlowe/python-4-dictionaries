import re

def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')


test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'

test_patterns = [r'\W+']

multi_re_find(test_patterns,test_phrase)
