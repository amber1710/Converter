ages=[20,50,85,95,12,45]
ages= list(map(lambda x:x +1, ages))

print(ages)

from functools import reduce

words= ['open', 'season']

def slugify(word , s):
    if s == '' :
        return word
    return s + '-' + word
slug= reduce(slugify,words,'')

print(slug)
