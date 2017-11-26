import unittest
from bowling import getScoreFor

class MyTests(unittest.TestCase):
    def test_gutter_game(self):
        self.assertEqual(getScoreFor("--------------------"),  0)
    def test_all_ones(self):
        self.assertEqual(getScoreFor("11111111111111111111"),  20)
    def test_one_spare(self):
        self.assertEqual(getScoreFor("5/3-----------------"),  16)
    def test_roll_strike(self):
        self.assertEqual(getScoreFor("X34----------------"),   24)
    def test_perfect_game(self):
        self.assertEqual(getScoreFor("XXXXXXXXXXXX"),          300)
    def test_case_sensitivity(self):
        self.assertEqual(getScoreFor("XXxxxXXXXxXx"),          300)
    def test_everything_is_fine_please(self):
        self.assertEqual(getScoreFor("11111111112222222222"), 30)
        self.assertEqual(getScoreFor("5/11------------3/11"), 26)
        self.assertEqual(getScoreFor("1/35XXX458/X3/23"),     160)
        self.assertEqual(getScoreFor("1/35XXX458/X3/XX6"),    189)

if __name__ == '__main__':
    unittest.main()
