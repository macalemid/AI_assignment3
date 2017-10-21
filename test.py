import unittest
from search import Node
import board
class generalTests(unittest.TestCase):
    def test_createChild(self):
        n = Node(True, board.blank)
        child = n.createChild();
        self.assertEqual(child.parent, n);

generalSuite = unittest.TestLoader().loadTestsFromTestCase(generalTests)
unittest.TextTestRunner(verbosity=2).run(generalSuite)
