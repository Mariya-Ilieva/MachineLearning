import numpy as np


# solution 1
matrix = np.arange(64).reshape(8, 8)
chessboard = (matrix // 8 + matrix % 8) % 2
print(chessboard)

# solution 2
template = np.array([[0, 1], [1, 0]])
chessboard = np.tile(template, (4, 4))
print(chessboard)

# solution 3
x, y = np.meshgrid(np.arange(8), np.arange(8))
indices = x + y
chessboard = indices % 2
print(chessboard)
