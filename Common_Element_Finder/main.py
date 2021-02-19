# To find the most frequent element in a list
from collections import Counter


my_groceries = ['apple', 'banana', 'banana', 'orage', 'banana', 'apple', 'beet', 'carrot', 'ginger', 'kale', 'ginger', 'ginger', 'kale', 'ginger']

print('Here are my groceries...\n')
print(my_groceries)

counter_thingy = Counter(my_groceries)


# list of all tuples/pairs in descending order of how commonly they showed up
print('\nHere is a list of all the tuples/pairs in descending order of how commonly each fruit showed up...\n')

print(counter_thingy.most_common())


# find the most common element
print('\nFind the most common element. If there is a tie, it will pick randomly...\n')
print(counter_thingy.most_common(1))


# Real world use case.
# Let's say you are trying to create a word counter.
# This counter should show how frequently each word was used with.

sentence = 'Hey there what is going on buddy? One thing that is worrying to me is how do I count how often something is repeating within this sentence? It is a mind boggling proposition and I do not think I have found a solution. The solution could be simple, or it could be difficult. When it comes to solving this problem, I guess the question is not how but rather when. Or, perhaps the question is what?'

# Here's how we'll solve this

# 1 - Turn it into a list of words
# 2 - Turn it into a counter object
# 3 - Print out how frequently each word is used

list_of_words = sentence.split()

counter_thingy = Counter(list_of_words)


print('\nPrint out how frequently each word is used as list of tuples...\n')
print(counter_thingy.most_common())

# For bonus points if you want to turn it into a dictionary instead of a list of tuples...

print('\nFor bonus points, turn it into a dictionary instead...\n')
print(dict(counter_thingy.most_common()))


# Your challenge:
# Write a one liner solution.
