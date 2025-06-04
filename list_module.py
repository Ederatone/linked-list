class Node:
    def __init__(self, value: str):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.tail = None
        self._length = 0

    def length(self):
        return self._length

    def append(self, element: str):
        new_node = Node(element)
        if not self.tail:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def insert(self, element: str, index: int):
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")
        new_node = Node(element)
        if not self.tail:
            if index != 0:
                raise IndexError("Index out of bounds")
            self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.tail.next
            self.tail.next = new_node
        elif index == self._length:
            self.append(element)
            return
        else:
            prev = self.tail.next
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
        self._length += 1

    def delete(self, index: int):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        if self._length == 1:
            value = self.tail.value
            self.tail = None
        elif index == 0:
            value = self.tail.next.value
            self.tail.next = self.tail.next.next
        else:
            prev = self.tail.next
            for _ in range(index - 1):
                prev = prev.next
            to_delete = prev.next
            value = to_delete.value
            prev.next = to_delete.next
            if to_delete == self.tail:
                self.tail = prev
        self._length -= 1
        return value

    def deleteAll(self, element: str):
        if not self.tail:
            return
        changed = True
        while changed:
            changed = False
            prev = self.tail
            curr = self.tail.next
            for _ in range(self._length):
                if curr.value == element:
                    if curr == self.tail:
                        self.tail = prev
                    if curr == self.tail.next:
                        self.tail.next = curr.next
                    prev.next = curr.next
                    self._length -= 1
                    changed = True
                    break
                prev, curr = curr, curr.next

    def get(self, index: int):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        curr = self.tail.next
        for _ in range(index):
            curr = curr.next
        return curr.value

    def clone(self):
        cloned = List()
        if not self.tail:
            return cloned
        curr = self.tail.next
        for _ in range(self._length):
            cloned.append(curr.value)
            curr = curr.next
        return cloned

    def reverse(self):
        if self._length <= 1:
            return
        prev = self.tail
        curr = self.tail.next
        for _ in range(self._length):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.tail = self.tail.next

    def findFirst(self, element: str):
        if not self.tail:
            return -1
        index = 0
        curr = self.tail.next
        for _ in range(self._length):
            if curr.value == element:
                return index
            curr = curr.next
            index += 1
        return -1

    def findLast(self, element: str):
        if not self.tail:
            return -1
        index = 0
        last_index = -1
        curr = self.tail.next
        for _ in range(self._length):
            if curr.value == element:
                last_index = index
            curr = curr.next
            index += 1
        return last_index

    def clear(self):
        self.tail = None
        self._length = 0

    def extend(self, elements):
        cloned = elements.clone()
        if cloned._length == 0:
            return
        if self._length == 0:
            self.tail = cloned.tail
        else:
            current = self.tail.next
            self.tail.next = cloned.tail.next
            cloned.tail.next = current
            self.tail = cloned.tail
        self._length += cloned._length