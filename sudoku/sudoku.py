import os
import random
import numpy as np
import time

def print_board(board, errors):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("   " + " ".join(f"{i + 1:2}" for i in range(9)))
    for i, row in enumerate(board):
        row_display = f"{i + 1:2} "
        for num in row:
            if num == 0:
                row_display += f' {".":2}'
            else:
                row_display += f"{num:2} "
        print(row_display)
    print(f"\nОшибки: {errors[0]}/{errors[1]}")

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in [board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]:
        return False
    return True

def is_solved(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0 or not is_valid(board, row, col, board[row][col]):
                return False
    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def generate_puzzle(difficulty):
    board = np.zeros((9, 9), dtype=int)
    solve_sudoku(board)
    
    puzzle = board.copy()
    
    if difficulty == 'easy':
        num_remove = random.randint(20, 30)  
        errors_allowed = 25
    elif difficulty == 'medium':
        num_remove = random.randint(40, 50)
        errors_allowed = 20
    elif difficulty == 'hard':
        num_remove = random.randint(60, 70)
        errors_allowed = 10
    elif difficulty == 'extreme':
        num_remove = random.randint(70, 81)
        errors_allowed = 5
    elif difficulty == 'master':
        num_remove = 70
        errors_allowed = 3
    elif difficulty == 'impossible':
        num_remove = 81  # Оставляем 0 чисел
        errors_allowed = 0
    else:
        raise ValueError("Incorrect difficulty level")
    
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    
    for i in range(num_remove):
        row, col = cells[i]
        puzzle[row][col] = 0
    
    return puzzle, errors_allowed

def play_sudoku(board, errors_allowed):
    errors = [0, errors_allowed]
    while True:
        print_board(board, errors)
        try:
            row = int(input("Enter line number (1-9):")) - 1
            col = int(input("Enter column number (1-9):")) - 1
            num = int(input("Enter a number (1-9):"))
            
            if not (0 <= row < 9) or not (0 <= col < 9):
                print("Error: Row and column number must be from 1 to 9.")
                time.sleep(1)
                continue
            
            if not (1 <= num <= 9):
                print("Error: The number must be from 1 to 9.")
                time.sleep(1)
                continue

            if board[row][col] != 0:
                print("Error: This field is already filled.")
                time.sleep(1)
                continue

            if is_valid(board, row, col, num):
                board[row][col] = num
            else:
                print("Error: Invalid number for this field.")
                errors[0] += 1
                time.sleep(1)
                if errors[0] >= errors[1]:
                    print("Game over: number of errors exceeded.")
                    break
                continue

            if is_solved(board):
                print("Congratulations! You have completed Sudoku.")
                time.sleep(1)
                break
        except ValueError:
            print("Error: Please enter a numeric value.")
            time.sleep(1)

if __name__ == "__main__":
    difficulty = int(input("""
Press difficulty:
1. easy
2. medium
3. hard
4. extreme
5. master
6. impossible
> """))
    difficulties = {
        1: "easy",
        2: "medium",
        3: "hard",
        4: "extreme",
        5: "master",
        6: "impossible"
    }
    puzzle, errors_allowed = generate_puzzle(difficulties.get(difficulty))
    play_sudoku(puzzle, errors_allowed)
