import unittest
from inf_monkey_shakespeare import str_rand_generate, str_percision, str_rand_eval, str_climbing_eval ,str_singlechr_swap


class inf_monkeys(unittest.TestCase):

    def test_str_rand_generate(self):
        self.assertEqual(len(str_rand_generate(1)), 1)
        self.assertEqual(len(str_rand_generate(10)), 10)
        self.assertEqual(len(str_rand_generate(0)), 0)
        self.assertEqual(len(str_rand_generate(26)), 26)
        self.assertEqual(len(str_rand_generate(48)), 48)
        self.assertEqual(len(str_rand_generate(1000)), 1000)

    def test_str_percision(self):
        self.assertEqual(str_percision("abc", 'aaa'), (1/3) * 100)
        self.assertEqual(str_percision("", ''), 100)
        self.assertEqual(str_percision("a", 'a'), 100)
        self.assertEqual(str_percision("abcdefa", 'aaaaaaa'), (2 / 7) * 100)
        self.assertEqual(str_percision("Abcdefa", 'aaaaaaa'), (1 / 7) * 100)
        self.assertEqual(str_percision("men with hats", 'menwithhats  '), (4 / 13) * 100)


    def test_str_single_generate(self):
        self.assertEqual(len(str_singlechr_swap('e')), 1)
        self.assertEqual(len(str_singlechr_swap('abcd')), 4)
        self.assertEqual(len(str_singlechr_swap('')), 0)
        self.assertEqual(len(str_singlechr_swap(' a')), 2)
        self.assertEqual(len(str_singlechr_swap('at besaf')), 8)
        self.assertEqual(len(str_singlechr_swap(' ')), 1)


if __name__ == '__main__':
    unittest.main()