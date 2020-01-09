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
            

    def print_list(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next
        # print(current.value)