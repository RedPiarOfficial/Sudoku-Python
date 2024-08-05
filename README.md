# Sudoku-Python

Sudoku-Python is a Python-based project for solving and generating Sudoku puzzles. This project aims to provide an easy-to-use interface for Sudoku enthusiasts and developers interested in algorithmic problem solving.

## Description

Run `Sudoku.py` and choose the difficulty level.
If you cannot solve the puzzle, open `solve.py` and set your board puzzle in the `input_str` variable, for example:

```python
input_str = """
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
"""
```
## Features

- Solve any valid Sudoku puzzle.
- Generate new Sudoku puzzles with varying difficulty levels.
- Visual representation of Sudoku grids.

## Rules
1. Grid: The game is played on a 9x9 grid divided into nine 3x3 subgrids.
2. Objective: Fill the grid with digits from 1 to 9 so that each digit appears:
    - Exactly once in each row.
    - Exactly once in each column.
    - Exactly once in each 3x3 subgrid.
3. Initial Conditions: Some cells in the grid are initially filled with digits (clues). Your task is to fill in the remaining cells.
## How to Play Sudoku
1. Start with the simple: Look for rows, columns, or subgrids with the most filled cells. This can help you find the missing digits more quickly.
2. Use elimination: If there's only one place left for a certain digit in a row, column, or subgrid, place it there.
3. Check for uniqueness: Ensure that digits do not repeat in each row, column, and subgrid.
4. Look for single candidates: Sometimes a digit may be the only possible option for a specific cell in a row, column, or subgrid.
5. Be attentive: Work through the puzzle gradually, checking each step to avoid mistakes.
