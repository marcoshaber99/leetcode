class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = self.first.next
        self.length -= 1
        return temp.value




class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Initialize the student queue and sandwich stack
        student_queue = Queue()
        sandwich_stack = Queue()

        for student in students:
            student_queue.enqueue(student)

        for sandwich in sandwiches:
            sandwich_stack.enqueue(sandwich)

        # Initialize a counter to keep track of skipped sandwiches
        skip_counter = 0  

        while True:
            # All students skipped the current sandwich
            if skip_counter == student_queue.length:  
                break
            
            # Get the first student and first sandwich
            curr_student = student_queue.dequeue()
            curr_sandwich = sandwich_stack.first.value if sandwich_stack.first else None

            if curr_student == curr_sandwich:
                # Student eats the sandwich
                sandwich_stack.dequeue()
                skip_counter = 0  # Reset the skip counter
            else:
                # Student skips the sandwich & goes to the back of the queue
                student_queue.enqueue(curr_student)
                skip_counter += 1  # Increment the skip counter

        return student_queue.length 