class TreeInfo:
    def __init__(self, tree):
        self.tree = tree
        self.nullable = self.is_nullable(self.tree)
        self.first_pos = None
        self.last_pos = None
        self.forward_pos = None

    
    def compute_first(self, tree):
        if(tree.root == "|"):
            arr1 = tree.left.first_pos 
            arr2 = tree.right.first_pos
            unified = self.union(arr1, arr2)
            tree.first_pos = unified
            return unified

        elif(tree.root == "?" and (self.is_nullable(tree.left))):
            arr1 = tree.left.first_pos 
            arr2 = tree.right.first_pos
            unified = self.union(arr1, arr2)
            tree.first_pos = unified
            return unified
        elif(tree.root == "?" and not (self.is_nullable(tree.left))):
            arr1 = tree.left.first_pos 
            tree.first_pos = arr1
            return arr1

        elif(tree.root == "*"):
            arr1 = tree.left.first_pos 
            tree.first_pos = arr1
            return arr1
        
        elif(self.tree.root == "&"):
            return []

        else:
            #si es un simbolo..
            tree.first_pos = [tree.number]
            self.first_pos = [tree.number]
            return [tree.number]


    def union(self, arr1, arr2):
        for elem in arr1:
            if elem not in arr2:
                arr2.append(elem)
        return arr2

    def is_nullable(self, node):
        if node:
            if node.root == "*":
                node.nullable = True
                return True
            elif node.root == "&":
                node.nullable = True
                return True
            elif node.root == "|":
                left = node.left.nullable
                right = node.right.nullable
                return left or right

            elif node.root == "?":
                left = node.left.nullable
                right = node.right.nullable
                return left and right

            #es un simbolo.
            else:
                node.nullable = False
                return False

    def __repr__(self):
        return f"<TreeInfo number is: {self.tree.number} first_pos: {self.first_pos} last_pos: {self.last_pos}>"


    #def compute_last(self):

    #def compute(self):


    
    