from node import Node

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None

    def print_list(self):
        if not self.head:
            return

        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

            if current == self.head:
                break
        print()

    def insert_at_start(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.prev = new_node
            self.head.next = self.head
            self.head.prev = self.prev
        else:
            new_node.next = self.head
            new_node.prev = self.prev
            self.head.prev = new_node
            self.prev.next = new_node
            self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        current = self.head

        while True:
            if current.data == data:
                break
            current = current.next
            if current == self.head:

                return

        if current.next == self.head and current.prev == self.head:
            self.head = None
        else:
            if current == self.head:
                self.head = current.next


            current.prev.next = current.next
            current.next.prev = current.prev


        current.prev = None
        current.next = None

    def update(self, old_data, new_data):
        if not self.head:
            return

        current = self.head
        while current.data != old_data:
            current = current.next
            if current == self.head:
                return

        current.data = new_data

    def search(self, data):
        if not self.head:
            print("La lista está vacía.")
            return

        current = self.head
        while True:
            if current.data == data:
                print(f"El elemento {data} está en la lista.")
                return

            current = current.next
            if current == self.head:
                print(f"El elemento {data} no está en la lista.")
                return