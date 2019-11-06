#!/usr/bin/env python3

import sys,argparse

MAX_ARRAY = 100
MAX_ITERATIONS = 1000

def neighbors(cell):

    # This is a function that returns the coordinates of a given cell's neighbour cells
    x, y = cell
    block = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)]
    # We only want the surrounding cells
    del block[4]
    return block

def to_array(coords):

    # This is a function that takes as input a set of coordinates of living cells
    # and returns a 2d array (technically a list for python) of zeros and ones,
    # where ones represent living cells
    # The array is cropped around the living cells

    alive_cells = list(coords)

    try:
        # We will need these measures to crop around the living cells
        # This is also a way to check for lack of living cells
        max_x = max( x for (x,y) in alive_cells)
        min_x = min( x for (x,y) in alive_cells)
        max_y = max( y for (x,y) in alive_cells)
        min_y = min( y for (x,y) in alive_cells)
    except ValueError:
        print ("No living cells left!!!")
        sys.exit()

    # This is effectively the cropping mechanism. We only care about the living cells
    new_height = max_x - min_x
    new_width = max_y - min_y

    # This is a way to control how big the Game can get
    if new_height > MAX_ARRAY or new_width > MAX_ARRAY:
            print ("{} {} {}".format("Maximum array size of", MAX_ARRAY, "exceeded"))
            sys.exit()

    #The input coordninates might not start from zero.
    new_coords = [(z-min_x, y-min_y) for (z,y) in alive_cells]

    # A new array of the above dimensions is created and filled with zeros
    out_array = [[0] * (new_width + 1) for row in range(new_height+1)]

    # Every spot that contains a living cell is filled with a '1'
    for cell in new_coords:
        out_array[cell[0]][cell[1]] = 1

    return out_array

def array_to_tiles(array):

    # This function turns an array of 1's and 0's into an array of tiles
    # The tiles are extended ASCII characters (ASCII codes \xB0 and \xB2, low and high density dotted)

    s = []
    for x,row in enumerate(array):
        for y,cell in enumerate(row):
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)

def positive_int(x):

    # This is to limit the number of iterations and in doing so, the time the Game will run
    x = int(x)
    if x < 1:
        raise argparse.ArgumentTypeError("Minimum number of iterations is 1")
    if x > MAX_ITERATIONS:
        raise argparse.ArgumentTypeError("{} {}".format("Maximum number of iterations is", MAX_ITERATIONS))

    return x
