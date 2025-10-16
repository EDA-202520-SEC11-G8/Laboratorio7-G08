from DataStructures.Tree import bst_node as bn
def new_map():
    """
        Crea un nuevo arbol
    """
    return {"root":None}

def get_node(root, key):
    k = bn.get_key(root)
    if k is None:
        return None
    if key < k:
        return get_node(root["left"], key)
    if key > k:   
        return get_node(root["right"], key)
    if k == key:
        return root
    

def get (my_bst, key):
    
    if my_bst["root"] is not None:
        return None
    node = get_node(my_bst["root"], key)
    return bn.get_value(node)