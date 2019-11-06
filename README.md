This is a command line, Python implementation of John Conway's Game of Life. It takes place in an infinite two-dimensional grid. Inside this grid there is an infinite number of cells. The Game evolves one iteration at a time based on a set of rules. Every cell "lives" in a neighbourhood of cells, which contains the 8 adjacent to it cells (top-bottom, left-right, diagonal). On every iteration:

  1.  Every live cell with exactly 2 or 3 live neighbour cells continues to live.

  2.  Every live cell with less than 2 or more than 3 live neighbour cells dies.

  3.  Every dead cell with exactly 3 live neighbour cells comes to life.

The Game begins with an initial seed. The seed is given as input from the user in the form of a file where '0's represent live cells and any other character represents dead cells. 

For example, a file containing the following text will be interpreted as a glider.
```
     -0  
     --0  
     000 
```

This implementation uses sparse representation to keep track of the grid, since the grid is infinite. So, only live cells' coordinates are used and every operation revolves around the live cells and their neighbours.

There are two modes. A step-wise mode, where the user has to press the Return (Enter) key for the Game to run one iteration.
To run in this mode:

```python
python3 fini.py -in <input_file>
```

The Game will stop when `ctrl-C` is pressed. 

The other mode allows the Game to run for a preset number of iterations.

Run with:

```python
python3 fini.py -in <input_file> -it <int> 
```
