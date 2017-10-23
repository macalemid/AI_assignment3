import unittest
from search import Node
import search
import board
from board import Board
import evalFunction as e
class generalTests(unittest.TestCase):
    def test_Board_makeMove(self):
        b = Board()
        self.assertEqual(b.state[len(b.state) -1], [0,0,0,0,0,0,0])
        b.make_move(1)
        self.assertEqual(b.state[len(b.state) -1], [0,1,0,0,0,0,0])
        b.make_move(1)
        self.assertEqual(b.state[len(b.state) -2], [0,2,0,0,0,0,0])
        b.make_move(6)
        self.assertEqual(b.state[len(b.state) -1], [0,1,0,0,0,0,1])
        b.make_move(5)
        self.assertEqual(b.state[len(b.state) -1], [0,1,0,0,0,2,1])

    def test_Board__switchTurns(self):
        b = Board()
        self.assertEqual(b._turn, 1)
        b._switchTurns();
        self.assertEqual(b._turn, 2)
        b._switchTurns();
        self.assertEqual(b._turn, 1)



    def test_Board_generateMoves(self):
        aBoardState = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        b = Board()
        b.state = aBoardState
        moves = b.generate_moves()
        self.assertEqual(moves, [0, 1, 2, 3, 4, 5, 6])
        aBoardState = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        b.state = aBoardState
        moves = b.generate_moves()
        self.assertEqual(moves, [1, 2, 3, 4, 5, 6])

        aBoardState = [
            [1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        b.state = aBoardState
        moves = b.generate_moves()
        self.assertEqual(moves, [1, 2, 4, 5])
        aBoardState = [
            [1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        b.state = aBoardState
        moves = b.generate_moves()
        self.assertEqual(moves, [])


    def test_Board_unmake_last_move(self):
        aBoardState = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        aBoardState3 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0]
        ]
        b = Board()
        b.state = aBoardState
        self.assertRaises(ValueError, b.unmake_last_move)

        aBoardState2 = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        b = Board()
        b.state = aBoardState2
        b._previous_move_col = [0]
        b.unmake_last_move()
        self.assertEqual(aBoardState, b.state)

        c = Board()
        self.assertEqual(c._turn, 1)
        c.make_move(4)
        self.assertEqual(c.state, aBoardState3)
        # print(c)
        self.assertEqual(c._turn, 2)
        self.assertEqual(c._previous_move_col, [4])
        c.unmake_last_move()
        self.assertEqual(c._turn, 1)
        self.assertEqual(c._previous_move_col, [])
        self.assertEqual(b.state, aBoardState)
        # print(c)



        # def test_createChild(self):
        #     n = Node(True, board.blank)
        #     child = n.createChild();
        #     self.assertEqual(child.parent, n);
        #
        # def test_get_grandparents_value(self):
        #     board2 = Board()
        #     node1 = Node(True, board2)
        #     node2 = node1.createChild()
        #     node3 = node2.createChild()
        #     node3.get_grandparents_value()
        #     node2.get_grandparents_value()
        #
        #     self.assertEqual(node3.value, node1.value)
        #     self.assertNotEquals(node2.value, node1.value)
        #
        #     node2.value = -10
        #     node4 = node3.createChild()
        #     node4.get_grandparents_value()
        #
        #     self.assertEqual(node4.value, -10)
        #
        # def test_update_value(self):
        #     board = Board()
        #     node1 = Node(True, board)
        #     node2 = node1.createChild()
        #     node3 = node2.createChild()
        #     node3.get_grandparents_value()
        #     node2.get_grandparents_value()
        #     node3.value = 10
        #     node2.update_value()
        #     self.assertEqual(node2.value, node3.value)
        #     node1.value = 100
        #     node1.update_value()
        #     self.assertEqual(node1.value, 100)
        #     node3.update_value()
        #     self.assertEqual(node3.value, 10)
        #
        # def test_expand_procedure(self):
        #     frontier = [Node(True, Board())]
        #     search.expand(frontier)
        #     self.assertEqual(len(frontier), 7)
        #     for node in frontier:
        #         self.assertFalse(node.isMaxNode)
        #         self.assertEqual(node.value, float("inf"))
        #         self.assertEqual(node.depth, 1)
        #         self.assertFalse(node.board.last_move_won())
        #
        #     search.expand(frontier)
        #     self.assertEqual(len(frontier), 13)
        #     self.assertFalse(node.board.last_move_won())
        #
        # def test_evalFunction(self):
        #     self.assertEqual(e.evalFunction(Board().state), 0);


        # def test_explore(self):
        #     frontier = [Node(True, Board())]
        #     search.explore(2, frontier)





generalSuite = unittest.TestLoader().loadTestsFromTestCase(generalTests)
unittest.TextTestRunner(verbosity=2).run(generalSuite)



