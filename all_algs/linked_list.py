class LinkedList: # Класс связного списка
    class Node: # Класс узла связного списка
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Добавление в конец связного списка
    def append(self, obj):
        if not self.head:
            self.head = self.Node(obj)  
        elif not self.tail:
            self.tail = self.Node(obj)
            self.head.next = self.tail
        else:
            prev_tail = self.tail
            self.tail = self.Node(obj)
            prev_tail.next = self.tail

        self.length += 1

    # Удаление по индексу из связного списка
    def pop(self, indx):
        i = 0
        if indx == 0:
            del self.head
            self.length -= 1
            return
            
        prev_node = self.head
        node = self.head

        while i != indx:
            prev_node = node
            node = node.next
            i += 1

        if node:
            prev_node.next = node.next
            del node
        else:
            raise ValueError('Указан неверный индекс!')
        
        self.length -= 1

    # Вставка по индексу в связный список
    def insert(self, indx, obj):
        i = 0
        if indx == 0:
            self.head = self.Node(obj, next=self.head)
            self.length += 1
            return

        prev_node = self.head
        node = self.head

        while i != indx:
            prev_node = node
            node = node.next
            i += 1

        if node:
            prev_node.next = self.Node(obj, next=node)
        else:
            raise ValueError('Указан неверный индекс!')

        self.length += 1

    def __iter__(self):
        try:
            node = self.head

            while node:
                yield node.data
                node = node.next
        except:
            raise ValueError('Список пуст.')


llist = LinkedList()
llist.append(5)
llist.append(2)
llist.append(10)

llist.pop(2)
llist.insert(0, 100)

for i in llist:
    print(i)