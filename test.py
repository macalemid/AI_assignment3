import unittest
from search import Node
import search
import board
from board import Board
import evalFunction as e
import utils


class generalTests(unittest.TestCase):
    def test_createChild(self):
        n = Node(True, board.blank)
        child = n.createChild()
        self.assertEqual(child.parent, n)

    def test_Board_generateMoves(self):
        aBoardState = utils.transpose_back([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        b = Board()
        b.state = aBoardState
        moves = b.generate_moves()
        self.assertEqual(moves, [0, 1, 2, 3, 4, 5, 6])
        aBoardState = utils.transpose_back([
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        b.state = aBoardState
        moves = b.generate_moves()
        self.assertEqual(moves, [1, 2, 3, 4, 5, 6])

        aBoardState = utils.transpose_back([
            [1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        b.state = aBoardState
        moves = b.generate_moves()
        self.assertEqual(moves, [1, 2, 4, 5])
        aBoardState = utils.transpose_back([
            [1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        b.state = aBoardState
        moves = b.generate_moves()
        self.assertEqual(moves, [])

    def test_Board_makeMove(self):
        b = Board()
        self.assertEqual(utils.transpose(b.state)[5], [0,0,0,0,0,0,0])
        b.make_move(1)
        self.assertEqual(utils.transpose(b.state)[5], [0,1,0,0,0,0,0])
        b.make_move(1)
        self.assertEqual(utils.transpose(b.state)[4], [0,2,0,0,0,0,0])
        b.make_move(6)
        self.assertEqual(utils.transpose(b.state)[5], [0,1,0,0,0,0,1])
        b.make_move(5)
        self.assertEqual(utils.transpose(b.state)[5], [0,1,0,0,0,2,1])

    def test_get_grandparents_value(self):
        board2 = Board()
        node1 = Node(True, board2)
        node2 = node1.createChild()
        node3 = node2.createChild()
        node3.get_grandparents_value()
        node2.get_grandparents_value()

        self.assertEqual(node3.value, node1.value)
        self.assertNotEquals(node2.value, node1.value)

        node2.value = -10
        node4 = node3.createChild()
        node4.get_grandparents_value()

        self.assertEqual(node4.value, -10)

    def test_update_value(self):
        board = Board()
        node1 = Node(True, board)
        node2 = node1.createChild()
        node3 = node2.createChild()
        node3.get_grandparents_value()
        node2.get_grandparents_value()
        node3.value = 10
        node2.update_value()
        self.assertEqual(node2.value, node3.value)
        node1.value = 100
        node1.update_value()
        self.assertEqual(node1.value, 100)
        node3.update_value()
        self.assertEqual(node3.value, 10)

        self.assertEqual(node1.children[0].children[0], node3)
        self.assertEqual(node1.children[0], node2)
        self.assertEqual(node3.parent.parent, node1)
        self.assertEqual(node3.parent, node2)

    def test_expand_procedure(self):
        frontier = [Node(True, Board())]
        search.expand(frontier)
        self.assertEqual(len(frontier), 7)
        for node in frontier:
            self.assertFalse(node.isMaxNode)
            self.assertEqual(node.value, float("inf"))
            self.assertEqual(node.depth, 1)
            self.assertFalse(node.board.last_move_won())

        search.expand(frontier)
        self.assertEqual(len(frontier), 13)
        self.assertFalse(node.board.last_move_won())

    def test_evalFunction(self):
        self.assertEqual(e.evalFunction(Board().transpose()), 0)



    # def test_explore(self):
    #     b = Node(True, Board())
    #     frontier = [b]
    #     search.explore(5, frontier)
    #     for child in b.children:
    #         for grandchild in child.children:
    #             print(grandchild.value)


    def test_search_minimax(self):
        b = Board()
        i = search.minimax(b, 3)





generalSuite = unittest.TestLoader().loadTestsFromTestCase(generalTests)
unittest.TextTestRunner(verbosity=2).run(generalSuite)



