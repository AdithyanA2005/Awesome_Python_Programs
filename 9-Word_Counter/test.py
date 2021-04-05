from collections import Counter

# This is my lsit
my_groceries = ['apple', 'banana', 'banana', 'orage', 'banana', 'apple',
                'beet', 'carrot', 'ginger', 'kale', 'ginger', 'ginger', 'kale', 'ginger']

# This will Print The List
print("My Grocery List: ")
for i in my_groceries:
    print(f"    - {i}")


# This is the counter variable
counter_thingy = Counter(my_groceries)
print("\n")
print("\n")


# This will print the count of list items in descending order
print("Grocery list Items Count: ")
d_count_item = counter_thingy.most_common()
for i in d_count_item:
    print(f"    - {i}")


# This will print the one mostly commonly used item
print('\n')
print("Commonly Used List Item is ")
for i in counter_thingy.most_common(1):
    print(f"    - {i}")
