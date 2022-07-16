class Node:
    def __init__(self, value, next_node=None, prev_node=None) -> None:
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None
        # Object can be initialized with a list
        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return "->".join([str(node) for node in self])

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def values(self):
        return [node.value for node in self]

    # Adding node at the tail
    def add_node(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    # Add multiple nodes at the tail
    def add_multiple_nodes(self, list):
        for value in list:
            self.add_node(value)

    def add_node_as_head(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def search_by_value(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            else:
                current = current.next
        return None

    def search_by_index(self, index):
        current = self.head
        counter = 0
        while index <= len(self) and index != counter:
            counter += 1
            current = current.next
        return current

    def insert_value_at_index(self, value, index):
        # If the index is the beginning of the list, just add to the head
        if index == 0:
            self.add_node_as_head(value)
        else:
            counter = 0
            current = self.head

            while counter < index - 1:
                current = current.next
                counter += 1

            # Make new node point to prev's next node
            new_node = Node(value, current.next)

            # Make prev node point to new node
            current.next = new_node

    def delete_by_value(self, value):
        current = self.head

        while current:
            if value == current.next.value:
                current.next = current.next.next
                return current.next
            else:
                current = current.next

    def print_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next


arr = [2, 59, 4, 92, 33, 12]
l = LinkedList(arr)
print(l.search_by_index(5).value)
print(l)
