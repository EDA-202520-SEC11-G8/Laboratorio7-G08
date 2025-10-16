from DataStructures.Tree import bst_node as bn
def new_map():
    """
        Crea un nuevo arbol
    """
    return {"root":None}

    
    
def insert_node(root, key, value):
    """
        Insert a new node in the tree
    """
    if root is None:
        root = bn.new_node(key,value)

    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    return root


def put(my_bst, key, value):
    """
        Put a new node in the tree
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst