from list_module import List

def main():
    lst = List()

    print("Appending elements A, B, C")
    lst.append('A')
    lst.append('B')
    lst.append('C')
    print("Current length:", lst.length())

    print("Insert 'X' at position 1")
    lst.insert('X', 1)

    print("Get element at position 1:", lst.get(1))

    print("Find first index of 'B':", lst.findFirst('B'))
    print("Find last index of 'B':", lst.findLast('B'))

    print("Delete element at index 2:", lst.delete(2))

    print("Delete all 'X'")
    lst.deleteAll('X')

    print("Clone list")
    cloned = lst.clone()
    print("Original list length:", lst.length())
    print("Cloned list length:", cloned.length())

    print("Reverse list")
    lst.reverse()

    print("Extend original list with ['X', 'Y']")
    ext = List()
    ext.append('X')
    ext.append('Y')
    lst.extend(ext)

    print("Final list:")
    for i in range(lst.length()):
        print(f"{i}: {lst.get(i)}")

    print("Clearing list")
    lst.clear()
    print("Length after clear:", lst.length())

if __name__ == "__main__":
    main()