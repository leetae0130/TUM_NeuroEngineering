from ete3 import Tree, TreeStyle

class Binary_Leaf:
    def __init__(self, name, prob_value, l_child = None, r_child = None, parent_node = None, is_root = False, code = ""):
        self.name = name
        self.probability =  prob_value
        self.left_child = l_child
        self.right_child = r_child
        self.parent = parent_node
        self.is_tree = is_root
        self.code = code
    def get_leftchild(self):
        return self.left_child
    def get_rightchild(self):
        return self.right_child
    def get_parent(self):
        return self.parent_node
    def branch_info(self):
        return self.is_tree
    def get_code(self):
        return self.code
    def set_code(self, codeword):
        self.code = codeword
    def set_childcode(self):
        self.left_child.code = self.code + "0"
        self.right_child.code = self.code + "1"
        if self.left_child.is_tree :
            self.left_child.set_childcode()
        if self.right_child.is_tree :
            self.right_child.set_childcode()
    def set_leftchild(self, node):
        self.left_child = node
    def set_rightchild(self, node):
        self.right_child = node

class Leaf_List:
    def __init__(self, leaf_list):
        self.leaves = leaf_list
    def sort_leaf(self):
        return sorted(self.leaves, key=lambda leaf : leaf.probability, reverse = True)
    def compress_leaf(self):
        sorted_leaf = self.sort_leaf()
        least_prob = sorted_leaf[-1]
        next_prob = sorted_leaf[-2]
        merged_leaf = Binary_Leaf("branch", least_prob.probability + next_prob.probability, 
                                  l_child = least_prob, r_child = next_prob, is_root = True)
        self.leaves = sorted_leaf[:-2] + [merged_leaf]
    def show_codes(self):
        for leaf in self.leaves :
            print str(leaf.probability) + " : " + leaf.get_code()            
    def size(self):
        return len(self.leaves)
            
def Tree_search(root):        
    s = ""
    if root.is_tree == False :
        s += root.name
        print root.name + " : " + root.get_code() + " with probability " + str(root.probability)
    else :
        s += "("
        s += Tree_search(root.left_child)
        s += ","
        s += Tree_search(root.right_child)
        s += ")"
    return s
            
def Huffman(leaves):
    while(leaves.size() > 1):
        leaves.compress_leaf()
    root = leaves.leaves[0]
    root.set_childcode()
    s = Tree_search(root) + ";"
    t = Tree(s, format=1)
    return t
    
        
a1 = Binary_Leaf("a1", 0.4)
a2 = Binary_Leaf("a2", 0.3)
a3 = Binary_Leaf("a3", 0.2)
a4 = Binary_Leaf("a4", 0.1)

List = [a1, a2, a3, a4]
Leaves = Leaf_List(List)

tree = Huffman(Leaves)
ts = TreeStyle()
ts.show_scale = False
ts.min_leaf_separation = 30
tree.render('Basic_Huffman.png', tree_style = ts)

List2 = []

for l1 in List:
    for l2 in List:
        a = Binary_Leaf(l1.name+l2.name, l1.probability*l2.probability)
        List2.append(a)

Leaves = Leaf_List(List2)

tree = Huffman(Leaves)
ts2 = TreeStyle()
ts2.show_scale = False
ts2.min_leaf_separation = 30
tree.render('Huffman2.png', tree_style = ts2)