from collections import Counter

sentence = """    Hey there what is going on?
    One thing that is worrying to me is,
    how do I count how often something is
    repeating within this sentence?
    It is a mind boggling proposition and
    I do not think I have found a solution.
    The solution could be simple,
    or it could be difficult.
    When it comes to solving this problem,
    I guess the question is not how but rather when.
    Or, perhaps the question is what?
    """

print("\n")
print("Our String is: ".upper())
print(sentence)


# We will make a list of words
print("\n")
list_of_words = sentence.split()
print("The List of Words is: ".upper())
for i in list_of_words:
    print(f"    - {i}")


# To create a Frequency of the words used
print("\n")
counter_thingy = Counter(list_of_words)
print("The count for words used: ".upper())
count_items = counter_thingy.most_common()
for i in count_items:
    print(f"    - {i}")
