my_dict = {
    'tuple': (1, 2, 3, 4, 5, 6),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {'red', 'green', 'blue', 'yellow', 'black'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(60)
del my_dict['list'][1]

my_dict['dict'][('i am a tuple',)] = 'anything'
my_dict['dict'].pop('c')

my_dict['set'].add('white')
my_dict['set'].remove('yellow')

print(my_dict)
