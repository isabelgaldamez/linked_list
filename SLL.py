import list

mylist = list.SList() # instantiating the class of SLL
mylist.add_to_back(10)
mylist.add_to_back(1)
mylist.print_list()
print("******")
mylist.add_to_front(2)
mylist.print_list()
print("******")
mylist.insert_after_node(2, 4)
mylist.insert_after_node(1, 5)
mylist.print_list()
