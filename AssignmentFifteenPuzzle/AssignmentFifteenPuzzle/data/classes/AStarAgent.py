from data.classes.FifteenPuzzle import FifteenPuzzle


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
    def choose_action(self, board: FifteenPuzzle) -> bool:
        """Apply one move and return True, or False if no solution is available."""
        raise NotImplementedError(
            "A* is not implemented yet. Add the search and move-selection logic here."
        )
