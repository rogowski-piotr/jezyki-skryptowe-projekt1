import time
from str_strip import function

# t0 = time.time_ns()

# for i in range(20_000_000):
#     pass

# print(function(characters='acbca', exclude_characters='acc'))
# print(function(characters='  acbca  '))

# t1 = time.time_ns()
# print(f'Time elapsed: {(t1 - t0) / (10 ** 9)}')


import string

str_to_strip = ' ' + '\t' + '\r' + '\x0b' + '\x0c' + 'abc' + ' ' + '\t' + '\r' + '\x0b' + '\x0c'
print(str_to_strip)
print([ char for char in str_to_strip ])

str_strip = str_to_strip.strip()
print(str_strip)
print([ char for char in str_strip ])

my_str_strip = function(str_to_strip)
print(my_str_strip)
print([ char for char in my_str_strip ])

