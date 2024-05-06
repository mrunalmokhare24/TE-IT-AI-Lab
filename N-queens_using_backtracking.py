def is_safe(board, row, col):
  
  # Check left side of the same row
  for c in range(col, -1, -1):
    if board[row][c] == 1:
      return False
  
  # Check upper left diagonal
  r, c = row, col
  while r >= 0 and c >= 0:
    if board[r][c] == 1:
      return False
    r -= 1
    c -= 1

  # Check lower left diagonal
  r, c = row, col
  while r < 8 and c >= 0:
    if board[r][c] == 1:
      return False
    r += 1
    c -= 1
  return True

def solve_n_queens(board, col, n):
  
  if col == n:
    return True

  for row in range(n):
    if is_safe(board, row, col):
      board[row][col] = 1
      if solve_n_queens(board, col + 1, n):
        return True
      board[row][col] = 0  # Backtrack

  return False

def main():
  
  board = [[0 for _ in range(8)] for _ in range(8)]
  if solve_n_queens(board, 0, 8):
    for row in board:
      print(*row, sep=" ")
  else:
    print("No solution exists!")

if __name__ == "__main__":
  main()
