from tree import Tree


def test_find_existing_node():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    node = tree._find(7, tree.root)
    assert node is not None
    assert node.data == 7


def test_find_missing_node():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    node = tree._find(4, tree.root)
    assert node is None
