from search import SearchSpace

class PacmanFoodSearchSpace(SearchSpace):
    def __init__(self, maze):
        self.height = maze["height"]
        self.width = maze["width"]
        self.walls = maze["walls"]
        self.start_pos = maze["pacman"]

        self.start_food = tuple(sorted(maze["food"])) #immutable


    def get_start_state(self):
        return(self.start_pos, self.start_food)

    def is_final_state(self, state):
        pacman_pos, food = state
        return len(food) == 0

    def get_successors(self, state):
        successors = []
        (x, y), food = state

        moves = {
            'North': (0, 1),
            'South': (0, -1),
            'East': (1, 0),
            'West': (-1, 0)
        }
        for move in moves:
            dx, dy = moves[move]
            nx, ny = x + dx, y + dy
            new_pos = (nx, ny)

            if (nx, ny)in self.walls: #don't hit a wall
                continue
    
            if not(0 <= nx < self.width and 0 <= ny < self.height): #don't leave maze
                continue
            
            if new_pos in food:
                new_food = tuple(f for f in food if f != new_pos)
            else:
                new_food = food
            
            next_state = (new_pos, new_food)
            successors.append((next_state, move, 1)) #1 is cost
            
        return successors
