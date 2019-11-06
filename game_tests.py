#!/usr/bin/env python3

import unittest
from game_of_life import game

class TestSum(unittest.TestCase):

    def test_empty(self):

        out = 'No living cells in initial seed\n'

        f = open('./input_templates/empty.txt')
        seed = f.read()
        f.close()

        number_of_iterations = 1

        result = game(seed,number_of_iterations )
        self.assertEqual(result, out, "Not the expected result")

    def test_glider(self):

        out = ('▓▓░░▓▓\n'
               '░░▓▓▓▓\n'
               '░░▓▓░░\n')

        f = open('./input_templates/glider.txt')
        seed = f.read()
        f.close()

        number_of_iterations = 1

        result = game(seed,number_of_iterations )
        self.assertEqual(result, out, "Not the expected result")

    def test_block(self):

        out = ('░░░░▓▓▓▓░░░░\n'
               '░░▓▓░░░░▓▓░░\n'
               '▓▓░░░░░░░░▓▓\n'
               '▓▓░░░░░░░░▓▓\n'
               '░░▓▓░░░░▓▓░░\n'
               '░░░░▓▓▓▓░░░░\n')

        f = open('./input_templates/block.txt')
        seed = f.read()
        f.close()

        number_of_iterations = 1

        result = game(seed,number_of_iterations )
        self.assertEqual(result, out, "Not the expected result")

    def test_penta_dec_multi(self):

        out = ('▓▓░░░░▓▓░░▓▓▓▓░░▓▓░░░░▓▓\n'
               '▓▓▓▓▓▓▓▓░░▓▓▓▓░░▓▓▓▓▓▓▓▓\n'
               '▓▓░░░░▓▓░░▓▓▓▓░░▓▓░░░░▓▓\n')

        f = open('./input_templates/penta_decathlon.txt')
        seed = f.read()
        f.close()

        number_of_iterations = 1000

        result = game(seed,number_of_iterations )
        self.assertEqual(result, out, "Not the expected result")

if __name__ == '__main__':
    unittest.main()
