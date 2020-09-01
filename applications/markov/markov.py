import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
replacing_text = [
    ('cats', 'and'),
    ('and', 'dogs', 'birds', 'fish'),
    ('dogs', 'and', 'birds'),
    ('birds', 'and'),
    ('fish', 'dogs')
]


# TODO: construct 5 random sentences
# Your code here

