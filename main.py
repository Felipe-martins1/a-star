import heapq

class AStar:
    import heapq

class AStar:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows, self.columns = len(matrix), len(matrix[0])

    def find_best_path(self, start, end):
        def manhattan(node, end):
            return abs(node[0] - end[0]) + abs(node[1] - end[1])

        def get_total_cost(start):
            total_cost = {(row, col): float('inf') for row in range(self.rows) for col in range(self.columns)}
            total_cost[start] = 0
            return total_cost

        def get_final_path(current, parents, start):
            path = []
            while current in parents:
                path.insert(0, current)
                current = parents[current]
            path.insert(0, start)
            return path

        def is_neighbor_in_matrix(neighbor):
            return 0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.columns

        def is_valid_path_neighbor(neighbor):
            return self.matrix[neighbor[0]][neighbor[1]] == 1

        def get_neighbor(current, dr, dc):
            return current[0] + dr, current[1] + dc

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        priority_list = [(0, start)]
        parents = {}

        total_cost = get_total_cost(start)

        while priority_list:
            f, current = heapq.heappop(priority_list)

            if current == end:
                return get_final_path(current, parents, start), total_cost[current]

            for dr, dc in directions:
                neighbor = get_neighbor(current, dr, dc)

                if is_neighbor_in_matrix(neighbor) and is_valid_path_neighbor(neighbor):
                    custo_tentativa = total_cost[current] + 1
                    custo_atual_vizinho = total_cost.get(neighbor, float('inf'))

                    if custo_tentativa < custo_atual_vizinho:
                        parents[neighbor] = current
                        total_cost[neighbor] = custo_tentativa
                        custo_f = custo_tentativa + manhattan(neighbor, end)
                        heapq.heappush(priority_list, (custo_f, neighbor))

        return None, None


matrix = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1]
]

start = (0, 0)
end = (3, 5)

a_star = AStar(matrix)
path, total_cost = a_star.find_best_path(start, end)

bg_green = '\033[92m'
bg_end = '\033[0m'

if path:
    print("Caminho encontrado:")
    print("Custo Total: ", total_cost)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (row, col) == start:
                print(bg_green + "S" + bg_end, end=' ')
            elif (row, col) == end:
                print(bg_green + "D" + bg_end, end=' ')
            elif (row, col) in path:
                print(bg_green + "." + bg_end, end=' ')
            elif matrix[row][col] == 1:
                print(".", end=' ')
            else:
                print("|", end=' ')
        print()
else:
    print('\033[91m' + "Não foi possível encontrar um caminho." + bg_end)
