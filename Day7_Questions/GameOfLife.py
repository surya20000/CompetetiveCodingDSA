# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


#Question Link:- https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

#Solution Class

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        liveCount = 0
        toChange = {}

        def valid(r, c):
            return (0 <= r < rows) and (0 <= c < cols)

        for r in range(rows):
            for c in range(cols):
                liveCount = 0
                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc
                    if valid(newRow, newCol) and board[newRow][newCol] == 1:
                        liveCount += 1
                if board[r][c] == 1:
                    if liveCount < 2 or liveCount > 3:
                        toChange[(r, c)] = 0 
                else:
                    if liveCount == 3:
                        toChange[(r, c)] = 1  
        for (r, c), nextState in toChange.items():
            board[r][c] = nextState       