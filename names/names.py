import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

'''
Using a binary search tree, the runtime of this operation can be significantly reduced.
The inherent alphabetized organization of the strings will reduce the number of names iterated
through when checking for duplicates. Binary search trees also do not contain duplicates themselves,
so any duplicates within a single list are implicitly ignored as well. This implementation of a binary search
tree to optimize the duplicate detection improves the original method's runtime from a polynomial complexity to
a much more usable logarithmic complexity. 
'''

# Using BST class created during the sprint assignments
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # No node exists
        if not self.value:
            self.value = BSTNode(value)
        # General Case
        else:
            # Left subtree case
            if value < self.value:
                # No child node exists
                if not self.left:
                    # If no child node, set self.left to new node
                    self.left = BSTNode(value)
                # Child node exists
                else:
                    # If child exists, recursively loop
                    self.left.insert(value)
            # Right subtree case
            else:
                # No child node exists
                if not self.right:
                    # If no child node, set self.right to new node
                    self.right = BSTNode(value)
                # Child node exists
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Root node = Target
        if self.value == target:
            return True
        elif target < self.value:
            # No child node to check
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)


# Instantiate BST using first name in list
# This duplicate entry into tree be implicitly ignored later by BST
# Because there is no mechanism to insert entries of equal value
bst = BSTNode(names_1[0])

# Insert names_1 into BST
for name in names_1:
    bst.insert(name)

# Use BSTNode Contains method to check for duplicates
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Runtime of 0.0690 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

'''
Python has a built in data structures in the form of sets that have their own methods and attributes
that are optimized for general speed and efficiency. By converting my iterables to sets and returning the
intersection of those sets as a list, I will retrieve the duplicates between the two files of names. 
https://docs.python.org/3/library/stdtypes.html#frozenset.intersection
'''

# Create a second timer to run specifically for this implementation
start_time2 = time.time()

# Use non operator syntax to return set intersection
set_intersection_duplicates = set(names_1).intersection(names_2)

# Stop timer
end_time2 = time.time()

# Duplicate above reporting and alter to fit this second method
print (f"{len(set_intersection_duplicates)} duplicates:\n\n{', '.join(set_intersection_duplicates)}\n\n")
print (f"runtime: {end_time2 - start_time2} seconds")

# Runtime of 0.0013 seconds