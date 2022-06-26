import email
import re

# patterns = ['term1', 'term2']

# split_term = '@'

# email = 'user@gmail.com'


# print(re.split(split_term,email))

# print(match.start())


def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Search for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsds....sdsdsdsdsdsdsds..dsdsd...dsdssddddd'

test_patterns = ['s[d]+']

multi_re_find(test_patterns, test_phrase)