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
    
    if my_bst["root"] is None:
        return None
    node = get_node(my_bst["root"], key)
    if node is None:
        return None
    return bn.get_value(node)

def size(my_bst):
    """
    Retorna el número de elementos en el árbol.
    """
    return size_tree(my_bst["root"])

def size_tree(root):
    """
    Cuenta los nodos desde un nodo dado.
    """
    if root is None:
        return 0
    return 1 + size_tree(root["left"]) + size_tree(root["right"])

def is_empty(my_bst):
    """ 
    Retorna True si el arbol está vacio, False si tiene nodos
    """
    return size(my_bst)==0