class node:
    def __init__(self, value, root = None, branch = ''):
        self.value = value
        self.root = root
        self.branch = branch
        self.left_branch = None
        self.right_branch = None
        return
    
    def search(self, target):
        if target == self.value:                            # Found the value
            location, branch = self, ''
        elif self.value is None:
            location, branch = self, ''
        elif target > self.value:                           # Value is higher
            if self.right_branch is not None:
                location, branch = self.right_branch.search(target)
            else: 
                location, branch = self, 'r'
        elif target < self.value:                           # Value is lower
            if self.left_branch is not None:
                location, branch = self.left_branch.search(target)
            else: 
                location, branch = self, 'l'
        return location, branch
                
        return
    
    def insert(self, value):
        location, branch = self.search(value)
        if branch == '':
            if location.value == None: # If top node is valueless, due to deletion
                location.value = value
                return 1
            else:
                return 0
        if branch == 'l':
            location.left_branch = node(value, location, branch)
        elif branch == 'r':
            location.right_branch = node(value, location, branch)
        return 1
    
    def delete(self):
        
        #No children
        if self.left_branch is None and self.right_branch is None:
            self.value = None
            if self.branch == 'l':
                self.root.left_branch = None
            elif self.branch == 'r':
                self.root.right_branch = None
            
        
        #2 children
        elif self.left_branch is not None and self.right_branch is not None:
            if self.branch == 'l':
                replacer = self.right_branch.min_node()
            else:
                replacer = self.left_branch.max_node()
            self.value = replacer.value
            replacer.delete()
        
        #1 child
        else:
            if self.left_branch is None:
                replacer = self.right_branch.min_node()
            else:
                replacer = self.left_branch.max_node()
            self.value = replacer.value
            replacer.delete()
        return
    
    def delete_value(self, value):
        to_be_deleted, branch = self.search(value)
        if branch != '':
            return 0
        else:
            to_be_deleted.delete()
            return 1
    
    def min_node(self):
        location = self
        while location.left_branch is not None:
            location = location.left_branch
        return location
    
    def max_node(self):
        location = self
        while location.right_branch is not None:
            location = location.right_branch
        return location
    
    def __nodecount(self, number):
        number += 1
        children = []
        if self.left_branch is not None:
            children.append(self.left_branch)
        if self.right_branch is not None:
            children.append(self.right_branch)
        return number, children
    
    def no_of_nodes(self):
        number = 0
        children = [self]
        while children != []:
            nodelist = children
            for node in nodelist:
                number, children = node.__nodecount(number)
        return number
    
    def weight(self):
        if self.right_branch is not None:
            right = self.right_branch.no_of_nodes()
        else:
            right = 0
        if self.left_branch is not None:
            left = self.left_branch.no_of_nodes()
        else:
            left = 0
        return right - left
            
    def is_balanced(self):
        if abs(self.weight()) > 1:
            balanced =  False
        else:
            balanced =  True
        return balanced
    
    def tree_list(self):
        tree = []
        layer = [self]
        while layer.count(None) < len(layer):
            layer_values = []
            children = []
            for node in reversed(layer):
                if node is None:
                    layer_values.append(None)
                else:
                    layer_values.append(node.value)
            tree.append(layer_values)
            for node in layer:
                if node is None:
                    children.append(None)
                    children.append(None)
                else:
                    children.append(node.right_branch)
                    children.append(node.left_branch)
            layer = children
        return tree
  
    def balance_node(self):
        if self.is_balanced() == True:
            return
        values = str(self).split()
        values = [int(i) for i in values]
        input_list = middle_out(values)
        branch = self.branch
        root = self.root
        for item in input_list:
            self.delete_value(item)
        for item in input_list:
            self.insert(item)
        self.branch = branch
        self.root = root
        if self.branch == 'l':
            self.root.left_branch = self
        elif self.branch == 'r':
            self.root.right_branch = self
        return
    
    def balance(self):
        self.balance_node()
        values = str(self).split()
        values = [int(i) for i in values]
        values = middle_out(values)
        for value in values:
            node = self.search(value)[0]
            node.balance_node()
        return
        
    
    def tree(self):
        tree = ""
        number_width = len(str(self.max_node().value))
        tree_list = self.tree_list()
        depth = len(tree_list)
        for layer in range(depth):
            initial_whitespace = 2 ** (depth - layer) - number_width
            between_whitespace = 2 ** (depth - layer + 1) - number_width
            tree += " " * initial_whitespace
            for pos in range(len(tree_list[layer])):
                if tree_list[layer][pos] is None:
                    tree += " " * number_width
                else:
                    next_value = str(tree_list[layer][pos])
                    tree += next_value
                    tree += ' ' * (number_width - len(next_value))
                tree += " " * between_whitespace
            tree += "\n"
        print(tree)
        return
    
    def __str__(self):
        rep = f'{self.left_branch} {self.value} {self.right_branch}'
        rep = rep.replace('None', '')
        rep = " ".join(rep.split())
        return rep
        
def middle_out(values):
        
        halfway = round(len(values)/2)
        low_values = values[:halfway]
        high_values = values[halfway:]
        low_values.reverse()
        input_list = low_values + high_values
        return input_list

def tests():
    tree = node(5)
    nodelist = [2,7,8,9,1,7,6]
    for i in nodelist:
        tree.insert(i)
        
    target = [[5],
              [2, 7],
              [1, None, 6, 8],
              [None, None, None, None, None, None, None, 9]]
    assert tree.tree_list() == target
    
    tree.delete_value(2)
    
    target = [[5],
              [1, 7],
              [None, None, 6, 8],
              [None, None, None, None, None, None, None, 9]]
    assert tree.tree_list() == target

    tree.balance()
    target = [[6], 
              [5, 8], 
              [1, None, 7, 9]]
    assert tree.tree_list() == target

    return

tests()
