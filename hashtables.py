# Learning HashTables.
# leetCode: Design HashSet
# Discription: Design a HashSet without using any built-in hash table libraries

class MyHashSet:

    def __init__(self):
        self.table = []

    def add(self, key: int) -> None:
        self.table.append(key)

    def remove(self, key: int) -> None:
        self.table.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.table


def main():
    my_hash_set = MyHashSet()
    my_hash_set.add(1)
    print(my_hash_set.table) # [1]
    my_hash_set.add(2)
    print(my_hash_set.table)
    print(my_hash_set.contains(1))
    print(my_hash_set.contains(3))
    my_hash_set.add(2)
    print(my_hash_set.table)
    print(my_hash_set.contains(2))
    my_hash_set.remove(2)
    print(my_hash_set.table)
    print(my_hash_set.contains(2))



if __name__ == "__main__":
    main() 

# Example:
        # Input
        # ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
        # [[], [1], [2], [1], [3], [2], [2], [2], [2]]
        # Output
        # [null, null, null, true, false, null, true, null, false]

        # Explanation
        # MyHashSet myHashSet = new MyHashSet();
        # myHashSet.add(1);      // set = [1]
        # myHashSet.add(2);      // set = [1, 2]
        # myHashSet.contains(1); // return True
        # myHashSet.contains(3); // return False, (not found)
        # myHashSet.add(2);      // set = [1, 2]
        # myHashSet.contains(2); // return True
        # myHashSet.remove(2);   // set = [1]
        # myHashSet.contains(2); // return False, (already removed)

# ****************** Notes For Me *********************************************
# Needs: HashFunction, Collision Resolution - Make the table
# insert, delete, search - Alter the table.



