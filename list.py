import node
class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, value):
        new_node = node.SLNode(value)
        current_head = self.head

    def add_to_back(self, value):
        new_node = node.SLNode(value)  # create a new node
        # if there is an empty list, make head to point to new node
        if self.head is None:
            self.head = new_node
            return 
        current_node = self.head # make another pointer to traverse the LList. until we reach the point to add the node
        while current_node.next != None: # start traversing the list
            current_node = current_node.next
        current_node.next = new_node # once we identify the end of the list, make the last node to point to the new node
    
    def add_to_front(self, value):
        new_node = node.SLNode(value) # create a new node
        new_node.next = self.head # points whenever the head is pointing to the current first node
        self.head = new_node # make head to point to the new node
        return 

    def insert_after_node(self, prev_node, value):
        new_node = node.SLNode(value)
        current = self.head # will traverse the list to find the position where we want to insert

        while current != None:
            if current.value == prev_node: # traverse through the list until we find the previous node
                new_node.next = current.next # make the new node point to where the previous is pointing
                current.next = new_node # previous node must point to the new node
            current = current.next # if the prev node has not been found keep traversing the list
        return 

    def delete_node(self, value):
        # if the node to be deleted is the first one on the list
        current = self.head
        # if the list is not empty and the value match to the value we need to delete
        if current and self.head.value == value:
            self.head = self.head.next # make head to point to the next node
            current = None # make current node to point to none so that we can remove the reference
            return 
        else:
            # while we have not reached the end of the list
            while current.next != None: 
                if current.next.value == value:  
                    current.next = current.next.next
                    return 
                current = current.next 
    
    def delete_at_index(self, index):
        current = self.head # current pointer should be at head position
        count = 0
        if index == 0 and current.next != None: # if the first node
            self.head = self.head.next # move head to the following node
            current = None # release current pointer
            return 
        prev = self.head # create a prev pointer so we can keep track of the prev node and the one we will delete
        while current != None: # while we do not reach the end of the list
            if index == count: # if we have found the right index
                # print("index found", index, count)
                prev.next = current.next # prev.next pointer must move to the next node after the index we want to remove
                current = None # remove the node
                return
            else: # keep traversing the lis
                prev = current # prev will always go one node behind current
                current = current.next # move current to the next node
                count += 1
    # Test Case 
    # 2 -> 4 -> 10 -> 5 -> 11 -> 22 -> None
    # Expect => 22 -> 11 -> 5 -> 10 -> 4 -> 2 -> None
    def reverse(self):
        # We need three pointers previous, current, next_node

        prev = None # Points to nothing at the beggining 
        current = self.head # points to the first node
        next_node = current.next # points to the second node

        if next_node == None: # assume there are only two nodes on the list
            current.next = prev
            self.head = current
            prev = None
        while next_node != None: # while we do not reach the end of the list
            current.next = prev # current pointer points to the prev node
            prev = current # at this point current looses contact with the next_node 
            current = next_node # current is pointing to the next_node
            next_node = next_node.next # next_node moves to the following one
        current.next = prev #need to update the last node as it is left witout a link to the rest of the list   
        self.head = current # make the head point to the new current position

    def swap_nodes(self, key_1, key_2):
        # we will use two pointers to find key_1
        current_1 = self.head
        prev_1 = None

        # we will use two pointers to find key_1
        current_2 = self.head
        prev_2 = None

        if key_1 == key_2:
            return 

        # Assuming key_1 is the first node
        if self.head.value == key_1:
            # move the pointers one node over
            prev_2 = current_2 
            current_2 = current_2.next
            # keep looping until we find the second value
            while current_2 != None and current_2.value != key_2: 
                prev_2 = current_2
                current_2 = current_2.next
            # update the pointers so that the head is on the correct swapped node
            prev_2.next = current_2.next
            current_2.next = prev_2
            self.head = current_2
            return 

        # if the nodes are in bettwen the list, loop through it until found
        while current_1 != None and current_1.value != key_1:
                prev_1 = current_1 
                current_1 = current_1.next

        while current_2 != None and current_2.value != key_2:
                prev_2 = current_2 
                current_2 = current_2.next
        
        # swap the two nodes
        if prev_1 != None:
            prev_1.next = current_2
            prev_2.next = current_2.next
            current_2.next = current_1

        # if one of the elements is not present on the list
        if not current_1 or not current_2: 
            return

    def list_length_iterative(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        print("length is:",count)

    def list_length_recursive(self, node):
        if node == None:
            return 0
        return 1 + self.list_length_recursive(node.next)

    def find_nth_to_last(self, position):
        current = self.head
        count = position
        # first move current node
        while count != 0 and current != None:   
            count -= 1
            current = current.next

        nth_node = self.head
        # Once we have nth distance, start moving the back node nth distance
        while current != None:
            current = current.next 
            nth_node = nth_node.next
        print("None at position: " , position , " is " , nth_node.value)
        return 

    def isPalindrome(self):
        word = ""
        current = self.head
        while current != None:
            word += current.value
            current = current.next   

        if word == word[::-1]:
            return True
        else:
            return False

    def print_list(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next
        # print(current.value)