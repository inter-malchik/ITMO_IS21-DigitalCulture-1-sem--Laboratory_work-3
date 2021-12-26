from main import BinarySearchTree
from random import randint, uniform, choice
import pytest


def tree_interpretator(bst, argument):
    marks = {
        "insert": bst.insert,
        "delete": bst.delete,
        "exists": bst.exists,
        "prev": bst.predecessor,
        "next": bst.successor,
    }
    return marks.get(argument)


@pytest.mark.parametrize("a", [0, uniform(0, 1), randint(-10 ** 6, 10 ** 6)])
def test_adding_node(a):
    bst = BinarySearchTree()
    bst.add(a)
    assert bst.root


@pytest.mark.parametrize("a", [0, uniform(0, 1), randint(-10 ** 6, 10 ** 6)])
def test_empty_tree(a):
    bst = BinarySearchTree()
    assert not bst.root and not bst.exists(a, bst.root)


@pytest.mark.parametrize("nodes", [tuple(randint(-1000, 1000) for _ in range(randint(0, 100))), (0, 0)])
def test_seeking_node(nodes):
    bst = BinarySearchTree()
    for node in nodes:
        bst.add(node)
    assert bst.exists(choice(nodes), bst.root)


@pytest.mark.parametrize("nodes", [tuple(randint(-1000, 1000) for _ in range(randint(0, 100)))])
def test_deleting_node(nodes):
    bst = BinarySearchTree()
    for node in nodes:
        bst.add(node)
    deleting = choice(nodes)
    bst.delete(deleting, bst.root)
    assert not bst.exists(deleting, bst.root)


@pytest.mark.parametrize("commands, expected",
                         [(["insert 1", "insert 1", "insert 0", "delete 1", "prev 0", "next 0"], [None] * 6)])
def test_finding_next_prev(commands, expected):
    bst = BinarySearchTree()
    output = []
    for command in commands:
        call = tree_interpretator(bst, command.split()[0])
        value = int(command.split()[1])
        outs = call(value, bst.root)
        if outs:
            output.append(outs.key)
        else:
            output.append(None)
    assert output == expected
