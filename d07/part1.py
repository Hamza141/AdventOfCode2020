from collections import defaultdict


def readFile(file):
    with open(file, 'r') as f:
        return f.readlines()


lines = readFile('input.txt')

# version 1
# seen = set()


# class Graph:

#     def __init__(self, vertices):
#         # No. of vertices
#         self.V = vertices

#         # default dictionary to store graph
#         self.graph = defaultdict(list)

#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)

#     '''A recursive function to print all paths from 'u' to 'd'.
#     visited[] keeps track of vertices in current path.
#     path[] stores actual vertices and path_index is current
#     index in path[]'''

#     def printAllPathsUtil(self, u, d, visited, path):

#         # Mark the current node as visited and store in path
#         visited[u] = True
#         path.append(u)

#         # If current vertex is same as destination, then print
#         # current path[]
#         if u == d:
#             global seen
#             if path[0] not in seen:
#                 seen.add(path[0])
#                 # print(path)
#         else:
#             # If current vertex is not destination
#             # Recur for all the vertices adjacent to this vertex
#             for i in self.graph[u]:
#                 if visited[i] == False:
#                     self.printAllPathsUtil(i, d, visited, path)

#         # Remove current vertex from path[] and mark it as unvisited
#         path.pop()
#         visited[u] = False

#     # Prints all paths from 's' to 'd'

#     def printAllPaths(self, s, d):

#         # Mark all the vertices as not visited
#         visited = [False]*(self.V)

#         # Create an array to store paths
#         path = []

#         # Call the recursive helper function to print all paths
#         self.printAllPathsUtil(s, d, visited, path)


# index = 0
# mapping = defaultdict(list)
# visited = defaultdict(list)

# color_mapping = {}

# vertices = 0

# for l in lines:
#     l = l.strip()
#     if 'no other' in l:
#         continue
#     contain = l.split('contain')
#     key = contain[0].split('bags')[0].strip()
#     if key not in color_mapping.keys():
#         color_mapping[key] = index
#         index += 1
#     vs = contain[1].split(',')
#     values = []
#     for v in vs:
#         v = v.split('bag')[0].strip().split(' ')
#         values.append(' '.join(v[1:]))
#         vertices += 1
#     mapping[key] = values
#     visited[key] = [False] * len(values)

# g = Graph(vertices)

# for key, values in mapping.items():
#     if key not in color_mapping.keys():
#         continue
#     for v in values:
#         if v not in color_mapping.keys():
#             continue
#         g.addEdge(color_mapping[key], color_mapping[v])

# for i in range(vertices):
#     g.printAllPaths(i, color_mapping['shiny gold'])

# print(len(seen) - 1)


# version 2
mapping = defaultdict(list)

for l in lines:
    l = l.strip()
    if 'no other' in l:
        continue
    contain = l.split('contain')
    key = contain[0].split('bags')[0].strip()
    vs = contain[1].split(',')
    values = []
    for v in vs:
        v = v.split('bag')[0].strip().split(' ')
        values.append(' '.join(v[1:]))
    mapping[key] = values


def dfs(adj_list, start, end):
    seen = set()
    stack = []
    stack.append(start)
    while len(stack) > 0:
        val = stack.pop()
        for color in adj_list[val]:
            if color in seen:
                continue
            if color != end and color in adj_list.keys():
                stack.append(color)
                seen.add(color)
            elif color == end:
                return True
    return False


count = 0
for k in mapping.keys():
    if k == 'shiny gold':
        continue
    if dfs(mapping, k, 'shiny gold'):
        count += 1
print(count)
