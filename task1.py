class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList: 
    def __init__(self):
        self.head = None

    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data): 
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head 
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end=" ")
            current = current.next
        print('None')

    def reverse(self):
        # реалізувати метод реверсування однозвязного списку, змінюючи посилання
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        # Реалізувати метод сортуванням для однозвязного списку (можна і не злиттям)
        if not self.head or not self.head.next:
            return self.head
        
        mid = self.get_middle(self.head)
        next_to_mid = mid.next
        mid.next = None

        left = LinkedList()
        left.head = self.head
        left.merge_sort()

        right = LinkedList()
        right.head = next_to_mid
        right.merge_sort()

        self.head = self.sorted_merge(left.head, right.head)

    def get_middle(self, head):
        # Отримати елемент в середені однозвязного списку 
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result
    

    def merge_sorted_lists(self, a, b):
        # Реалізувати метод, що обєднює два відсортовані однозвязні списки в один відсортований
        dummy = Node()  #  вузол для об'єднання
        tail = dummy

        a, b = a.head, b.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        elif b:
            tail.next = b

        result_list = LinkedList()
        result_list.head = dummy.next
        return result_list


# --- Тестування ---
first_list = LinkedList()
first_list.insert_at_beginning(5)
first_list.insert_at_beginning(10)
first_list.insert_at_beginning(15)
first_list.insert_at_end(20)
first_list.insert_at_end(25)

print("Зв'язний список 1:")
first_list.print_list()

first_list.reverse()
print("Реверсований список 1:")
first_list.print_list()

first_list.merge_sort()
print("Відсортований список 1:")
first_list.print_list()

# Додавання другого списку для об'єднання
second_list = LinkedList()
second_list.insert_at_end(3)
second_list.insert_at_end(5)
second_list.insert_at_end(6)
second_list.insert_at_end(8)
second_list.insert_at_end(12)

print("Зв'язний список 2:")
second_list.print_list()

second_list.merge_sort()
print("Відсортований список 2:")
second_list.print_list()

# Об'єднання двох відсортованих списків
merged_list = first_list.merge_sorted_lists(first_list, second_list)
print("Об'єднаний відсортований список:")
merged_list.print_list()