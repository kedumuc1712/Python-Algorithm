from __future__ import print_function

class Graph():
	def __init__(self):
		self.vertex = {}

	# for printing the Graph vertexes
	def printGraph(self):
		print(self.vertex)
		for i in self.vertex.keys():
			print(i, ' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

	# for adding the edge between two vertexes
	def addEdge(self, fromVertex, toVertex):
		# check if vertex is already presen,
		if fromVertex in self.vertex.keys():
			self.vertex[fromVertex].append(toVertex)
		else:
			# else make a new vertex
			self.vertex[fromVertex] = [toVertex]

	def DFS(self):
		# visited array for storing already visited nodes
		visited = [False] * len(self.vertex)

		# call the recursive helper function
		for i in range(len(self.vertex)):
			if visited[i] == False:
				self.DFSRec(i, visited)

	def DFSRec(self, startVertex, visited):
		# mark start vertex as visited
		visited[startVertex] = True

		print(startVertex, end = ' ')
		# Recur for all the vertexes that are adjacent to this node
		for i in self.vertex.keys():
			if visited[i] == False:
				self.DFSRec(i, visited)

if __name__ == '__main__':
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 3)
	g.addEdge(1, 4)
	g.addEdge(2, 3)
	g.addEdge(3, 4)
	g.addEdge(3, 5)
	g.addEdge(4, 5)
	g.addEdge(5, 5)

	g.printGraph()
	print("DFS:")
	g.DFS()

