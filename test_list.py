import unittest
from list_module import List

class TestList(unittest.TestCase):
    def test_append_and_length(self):
        lst = List()
        self.assertEqual(lst.length(), 0)
        lst.append('A')
        lst.append('B')
        self.assertEqual(lst.length(), 2)

    def test_insert_valid(self):
        lst = List()
        lst.append('A')
        lst.insert('B', 1)
        self.assertEqual(lst.get(1), 'B')

    def test_insert_invalid(self):
        lst = List()
        with self.assertRaises(IndexError):
            lst.insert('X', -1)
        with self.assertRaises(IndexError):
            lst.insert('X', 100)

    def test_delete_valid(self):
        lst = List()
        lst.append('A')
        lst.append('B')
        self.assertEqual(lst.delete(1), 'B')
        self.assertEqual(lst.length(), 1)

    def test_delete_invalid(self):
        lst = List()
        with self.assertRaises(IndexError):
            lst.delete(0)

    def test_delete_all(self):
        lst = List()
        lst.append('A')
        lst.append('B')
        lst.append('A')
        lst.deleteAll('A')
        self.assertEqual(lst.length(), 1)
        self.assertEqual(lst.get(0), 'B')

    def test_get_valid_invalid(self):
        lst = List()
        lst.append('X')
        self.assertEqual(lst.get(0), 'X')
        with self.assertRaises(IndexError):
            lst.get(1)

    def test_clone(self):
        lst = List()
        lst.append('A')
        clone = lst.clone()
        clone.append('B')
        self.assertEqual(lst.length(), 1)
        self.assertEqual(clone.length(), 2)

    def test_reverse(self):
        lst = List()
        lst.append('A')
        lst.append('B')
        lst.reverse()
        self.assertEqual(lst.get(0), 'B')

    def test_find_first_last(self):
        lst = List()
        lst.append('X')
        lst.append('Y')
        lst.append('X')
        self.assertEqual(lst.findFirst('X'), 0)
        self.assertEqual(lst.findLast('X'), 2)
        self.assertEqual(lst.findFirst('Z'), -1)

    def test_clear(self):
        lst = List()
        lst.append('A')
        lst.clear()
        self.assertEqual(lst.length(), 0)

    def test_extend(self):
        lst1 = List()
        lst2 = List()
        lst1.append('A')
        lst2.append('B')
        lst2.append('C')
        lst1.extend(lst2)
        self.assertEqual(lst1.length(), 3)
        self.assertEqual(lst1.get(2), 'C')

if __name__ == "__main__":
    unittest.main()