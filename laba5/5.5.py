import re

string = input()

print('new string: {}, replaces: {}'.format(re.sub(r':', '%', string), string.count(':')))