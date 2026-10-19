from data.classes.FifteenPuzzle import FifteenPuzzle
import heapq, time



class AStarAgent:
    """Scaffold for an A* solver; implement search before using it to play."""

    def __init__(self):
        self.moves = None
        self.move_index = 0

    def choose_action(self, board: FifteenPuzzle) -> bool:
        """Apply one move and return True, or False if no solution is available."""

        current = self.get_state(board)

        if self.moves is None:
            start_time = time.perf_counter()
            self.moves = self.find_solution(current)
            elapsed_time = time.perf_counter() - start_time
            print(f"A* search took {elapsed_time:.6f} seconds to find a solution with {len(self.moves)} moves.")
            self.move_index = 0
        if self.move_index >= len(self.moves):
            return False

        next_state = self.moves[self.move_index]
        tile_index = next_state.index(None)

        if not board.handle_move(board.squares[tile_index]):
            return False

        self.move_index += 1

        print(f"Move {self.move_index}: {next_state}")
        return True

    def get_state(self, board):
        return tuple(square.value for square in board.squares)

    def heuristic(self, state):
        distance = 0

        for index, value in enumerate(state):
            if value is None:
                continue

            goal_index = value - 1
            row, column = divmod(index, 4)
            goal_row, goal_column = divmod(goal_index, 4)

            distance += abs(row - goal_row) + abs(column - goal_column)
        return distance


    def get_neighbors(self, state):
        empty_index = state.index(None)
        row, column = divmod(empty_index, 4)

        neighbors = []

        possible_positions = [
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1)
        ]

        for next_row, next_column in possible_positions:
            if 0 <= next_row < 4 and 0 <= next_column < 4:
                tile_index = next_row * 4 + next_column

                neighbor = list(state)

                neighbor[empty_index], neighbor[tile_index] = (neighbor[tile_index], neighbor[empty_index])
                neighbors.append(tuple(neighbor))

        return neighbors


    def find_solution(self, start):
        goal = tuple(range(1, 16)) + (None, )
        if start == goal:
            return []

        frontier = []
        tie_breaker = 0

        heapq.heappush(frontier, (self.heuristic(start), tie_breaker, start))

        came_from = {}
        move_used = {}
        cost_so_far = {start: 0}

        expanded_states = 0

        print("Starting A* search...", flush=True)

        while frontier:
            _, _, current = heapq.heappop(frontier)
            expanded_states += 1

            if expanded_states % 10000 == 0:
                print(f"Expanded {expanded_states} states..." f"frontier size: {len(frontier)}", flush=True)

            if current == goal:
                print(f"A* search completed. Expanded {expanded_states} states.", flush=True)
                return self.reconstruct_path(came_from, move_used, current)

            for neighbor in self.get_neighbors(current):
                new_cost = cost_so_far[current] + 1
                if new_cost < cost_so_far.get(neighbor, float('inf')):
                    cost_so_far[neighbor] = new_cost
                    tie_breaker += 1

                    priority = new_cost + self.heuristic(neighbor) #f(n) = g(n) + h(n)

                    heapq.heappush(frontier, (priority, tie_breaker, neighbor))

                    came_from[neighbor] = current
                    move_used[neighbor] = neighbor.index(None)  # Store the index of the empty tile
        print("A* search failed to find a solution.", flush=True)
        return []





    def reconstruct_path(self, came_from, move_used, current):
        path = []

        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path
