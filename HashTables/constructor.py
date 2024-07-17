# pylint: disable=locally-disabled, line-too-long, W0105
class HashTable:
    def __init__(self, size=7):
        # create a list with seven items which contain none
        self.data_map = [None] * size

    # this is what we pass the key to determine what address we store the key value pair in
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # Ascii number for each letter as we are looping through it
            # multiplies it by 23, which is a prime number,
            # get the remainder of the number divided by 7
            # this will produce a number from -6 which is our address space
            """
            my_hash: This variable likely starts with an initial value, often 0 or some seed value, which will be updated iteratively for each letter in a given string.
            ord(letter): The ord() function in Python returns the Unicode code point (an integer) for a given character letter. For example, ord('A') returns 65.
            ord(letter) * 23: The Unicode code point of the character letter is multiplied by 23. 
            The number 23 is a constant chosen to help spread out the hash values, reducing collisions in the hash table. It’s common to use prime numbers or constants in hashing to improve distribution.
            my_hash + ord(letter) * 23: The current value of my_hash is updated by adding the product of the Unicode code point and the constant 23.
            % len(self.data_map): The modulo operation is used to ensure the hash value stays within the bounds of the hash table's array. self.data_map is the array (or list) representing the hash table, and len(self.data_map) gives the size of this array. 
            he modulo operation ensures the hash value wraps around if it exceeds the array length, keeping the index within valid bounds.
            """
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


my_hash_table = HashTable()
my_hash_table.print_table()
