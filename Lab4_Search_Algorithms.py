"""
BFS and DFS
"""

def readFile(filename):
  cube = []
  with open(filename, 'r') as f:
    for line in f:
      row = [int(char) for char in line.strip('\n')] # removing the newlines using strip()
      cube.append(row)
  return cube

def BFS(cube):
  n = m = len(cube)
  visited = [[0 for i in range(m)] for i in range(n)] # declaring 2d visited array and a queue for bfs
  queue = [(0, 0)]
  parent = {}

  queueIndex = 0 # for 'popping' from queue

  while queueIndex < len(queue):
      row, col = queue[queueIndex]
      queueIndex += 1

      # reached goal
      if row == n - 1 and col == m - 1:
          path = []
          while (row, col) in parent:
              path.append((row, col))
              row, col = parent[(row, col)]
          path.append((0, 0))
          path.reverse()
          return path

      # if not
      visited[row][col] = 1
      moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
      for dr, dc in moves:
          new_row, new_col = row + dr, col + dc
          if 0 <= new_row < n and 0 <= new_col < m and cube[new_row][new_col] == 0 and not visited[new_row][new_col]:
              queue.append((new_row, new_col))
              parent[(new_row, new_col)] = (row, col)
  return -1
def DFS(cube):
  n = m = len(cube)
  visited = [[0 for i in range(m)] for i in range(n)] # declaring 2d visited array and a queue for bfs
  path = []
  stack = [(0, 0)]

  while stack:
    row, col = stack.pop()

    if not visited[row][col]:
        path.append((row, col))
        visited[row][col] = 1

        # reached goal
        if row == n - 1 and col == m - 1:
            return path

        # if not, check all neighbours
        neighbors = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]
        for r, c in neighbors:
            if 0 <= r < n and 0 <= c < m and cube[r][c] == 0 and not visited[r][c]:
                stack.append((r, c))

  return -1

# main
cube = readFile('input.txt')
print(cube)

print("BFS Path:", BFS(cube))
print("DFS Path:", DFS(cube))

"""UCS"""

def ucs(graph, start, goal):
    priority_queue = [(0, start, [])]  # (cost, node, path)
    visited = set()

    while priority_queue:
        priority_queue.sort()  # Sort the priority queue based on the cost
        cost, current_node, path = priority_queue.pop(0)  # Pop the node with the lowest cost
        if current_node not in visited:
            visited.add(current_node)
            path = path + [current_node]

            if current_node == goal:
                return path, cost

            for neighbor, neighbor_cost in graph.get(current_node, []):
                if neighbor not in visited:
                    priority_queue.append((cost + neighbor_cost, neighbor, path))

    return None, float('inf')

graph = {
    1: [(2, 3), (3, 2)], # node 1 is connected to 2 and 3 with costs 3 and 2 resp.
    2: [(1, 3), (4, 3)],
    3: [(1, 2), (4, 2)],
    4: [(2, 3), (3, 2)],
}

start_node = 1
goal_node = 4
optimal_path, total_cost = ucs(graph, start_node, goal_node)
if optimal_path:
    print("Optimal Path:", optimal_path)
    print("Total Cost:", total_cost)
else:
    print("No path found from", start_node, "to", goal_node)
