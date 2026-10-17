from data.classes.FifteenPuzzle import FifteenPuzzle
import heapq



class AStarAgent:
    """Scaffold for an A* solver; implement search before using it to play."""

    #Plan:
    # - Implement something similar to Human Agent
    #       1. Look at current state
    #       2. Look at neighbors of empty space
    #       3. Calculate heuristic for each neighbor
    #       4. Choose the neighbor with the lowest heuristic value
    #       5. Repeat until the goal state is reached or no more moves are possible


    # FifteenPuzzle.get_squares() 
    # FifteenPuzzle.get_empty_square()
    # FifteenPuzzle.get_neighbors(square: Square) -> list[Square]

    def __init__(self):
        self.moves = None
        self.move_index = 0

    def choose_action(self, board: FifteenPuzzle) -> bool:
        """Apply one move and return True, or False if no solution is available."""

        if self.moves is None:
            self.moves.find_solution(self.get_state(board))

    def get_state(self, board):

    def heuristic(self, state):


    def get_neighbors(self, state):


    def find_solution(self, start):


    def reconstruct_path(self, came_from, move_used, current):
        
