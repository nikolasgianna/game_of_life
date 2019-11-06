#!/usr/bin/env python3

import sys, argparse
from helper_functions import *

def tick(coords):

    # This is the heart of the whole Game.
    # Every time this function runs, another generation is applied.
    # A sparse representation was adopted, so the input is a set of
    # all the living cells' coordinates.

    new_coords = set([])

    # candidate_cells is the union of currently living cells and all their neighbouring cells,
    # each one only considered once using the set() function
    candidate_cells = coords.union(set(n for cell in coords for n in neighbors(cell)))
    for cell in candidate_cells:

        # If the neighboring cells are alive cells they should be in the board list,
        # so we just count how many times that's true and that's the number of living
        # cells in the neighbourhood of each living cell
        count = sum((n in coords) for n in neighbors(cell))

        # The next statement incorporates the whole logic of The Game of Life
        if count == 3 or (count == 2 and cell in coords):
            new_coords.add(cell)

    # A set of the next generation's living cells' coordinates is returned.
    return new_coords

def game(seed, iterations):

    # This is where the whole of the Game is implemented
    cells = set([])

    # seed is the initial seed, taken as input from a file
    for y, row in enumerate(seed.splitlines()):
        for x, cell in enumerate(row.strip()):
            if cell == '0':
                cells.add((y,x))

    if cells:

        # The game can run in two modes, either step by step on every press of Return from the user
        # or for a number of iterations. The number of iterations is taken as input from the user
        print("Initial seed is: \n\n" + array_to_tiles(to_array(cells)))

        if iterations > 0:
            for __ in range(iterations):
                cells = tick(cells)
            return array_to_tiles(to_array(cells))
        else:
            while True:
                input("Press Enter to run one step...\n")
                cells = tick(cells)
                print (array_to_tiles(to_array(cells)))
    else: return ("No living cells in initial seed\n")

def main():

    # Set up the command line arguments
    parser = argparse.ArgumentParser(allow_abbrev=False, description='The Game of Life')
    parser.add_argument("-in","--input",required=False, default='', help="The input file. If left empty, the initial seed has no living cells")
    parser.add_argument("-it","--iter", required=False, default=0, type=positive_int, help="The number of iterations. If left empty, the Game runs step by step")
    args = parser.parse_args()
    input = args.input
    iterations = args.iter

    # The user can choose the file to use as initial seed. For the empty seed we can either
    # use a file or an empty string
    if input != '':
        try:
            fo = open(input)
            seed = fo.read()
        except FileNotFoundError:
            print('\nNo such file found\n')
            sys.exit()
    else:
        print ("No living cells in initial seed\n")
        sys.exit()

    # This is the entry point to the Game
    print (game(seed,iterations))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # The game can be stopped with ctrl-C
        print('\n\nGame Stopped')
