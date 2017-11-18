#!/bin/python3.4
dict = { 'name':'jhbian', 'nickname':'duanduan' }
print('dict\'s iteritems()...')
print(dict.iteritems());
print('dict\'s iterkeys()...')
print(dict.iterkeys())

print('dict\'s values() and keys()')
pairs = zip(dict.values(),dict.keys())
print(pairs)
