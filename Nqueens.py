def solve_n_queens(n: int):
    """
    Finds and prints all valid board configurations for the N-Queens problem.
    'Q' represents a placed Queen, and '.' represents an empty square.
    """
    solutions = []
    # Create an empty N x N chessboard
    board = [["."] * n for _ in range(n)]

    # Sets to track columns and diagonals under attack in O(1) time
    cols = set()
    pos_diag = set()  # Tracks (row + col)
    neg_diag = set()  # Tracks (row - col)

    def backtrack(row):
        # Base Case: All queens are placed successfully
        if row == n:
            # Format the board state as a list of strings
            solution = [" ".join(r) for r in board]
            solutions.append(solution)
            return

        # Attempt to place a queen in each column of the current row
        for col in range(n):
            # Check if the cell is under attack from any previous queen
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # 1. Place the queen (Make a choice)
            board[row][col] = "Q"
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)

            # 2. Recurse to place the queen in the next row
            backtrack(row + 1)

            # 3. Remove the queen (Backtrack)
            board[row][col] = "."
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    # Start the backtracking process from the 0th row
    backtrack(0)
    return solutions


def print_solutions(solutions, n):
    """Utility function to display the found configurations."""
    print(f"Total solutions found for N = {n}: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"--- Solution {idx} ---")
        for row in sol:
            print(row)
        print()


# --- Execution Example ---
if __name__ == "__main__":
    N = 4  # Change this value to solve for different board sizes (e.g., 8)
    all_solutions = solve_n_queens(N)
    print_solutions(all_solutions, N)
          
