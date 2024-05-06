class Node:
    def __init__(self, data, level, fval):
        self.data = data  # data will be a list representing columns where queens are placed
        self.level = level  # level or depth of the node in the tree
        self.fval = fval  # f = g + h (total cost)

    def generate_child(self):
        """Generate all possible child configurations by moving each queen to a different row in its column"""
        children = []
        n = len(self.data)
        for col in range(n):
            current_row = self.data[col]
            for row in range(n):
                if row != current_row:
                    child_data = self.data[:]
                    child_data[col] = row
                    child_node = Node(child_data, self.level + 1, 0)
                    children.append(child_node)
        return children

    def find_conflicts(self):
        """Count the number of pairs of queens that threaten each other"""
        n = len(self.data)
        conflicts = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.data[i] == self.data[j] or abs(self.data[i] - self.data[j]) == abs(i - j):
                    conflicts += 1
        return conflicts


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def f(self, node):
        """Heuristic function to calculate f(x) = h(x) + g(x)"""
        h = node.find_conflicts()
        g = node.level
        return h + g

    def process(self):
        """Process to solve the N-Queen problem"""
        # Initialize with a starting configuration, possibly random or empty
        start = [0] * self.n  # Starting with all queens in the first row (not a valid solution, just initial state)
        start_node = Node(start, 0, 0)
        start_node.fval = self.f(start_node)
        self.open.append(start_node)

        while True:
            current = self.open[0]
            print("Level:", current.level, "Board:", current.data, "Fval:", current.fval)

            if current.find_conflicts() == 0:  # If no conflicts, solution found
                print("Solution found:")
                self.print_board(current.data)
                break

            for child in current.generate_child():
                child.fval = self.f(child)
                self.open.append(child)
            self.closed.append(current)
            del self.open[0]
            self.open.sort(key=lambda x: x.fval)

    def print_board(self, data):
        """Utility to print the board"""
        n = len(data)
        for row in range(n):
            line = ""
            for col in range(n):
                if data[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")


# Example usage
n_queen_puzzle = Puzzle(8)  # Adjust size for different N
n_queen_puzzle.process()
