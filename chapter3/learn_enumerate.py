seasons = ['Spring', 'Summer', 'Fall', 'Winter']

for i, v in enumerate(seasons):
    print(i, v)

print('\n', '-' * 10, 'list_seasons', '-' * 10)
print(list(enumerate(seasons)))
print(tuple(enumerate(seasons)))
print(dict(enumerate(seasons)))
print(set(enumerate(seasons)))


dict_seasons = {0: 'Spring', 1: 'Summer', 2: 'Fall', 3: 'Winter'}
print('\n', '-' * 10, 'dict_seasons', '-' * 10)
print(list(enumerate(seasons)))
print(tuple(enumerate(seasons)))
print(dict(enumerate(seasons)))
print(set(enumerate(seasons)))
