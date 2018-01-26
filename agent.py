class Agent(object):

	def __init__(self, start_loc, total_rewards, maze):
		self.current_loc = start_loc
		self.collected_rewards = 0
		self.total_rewards = total_rewards
		self.maze = maze
		self.cost = 0


	def getCurrentLoc(self):
		return current_loc

	def getNeighbors(self):
		height = len(self.maze)
		width = len(self.maze[0])
		i,j = self.current_loc
		neighbors = []

		if self.maze[i+1][j] != '%':
			neighbors.append((i+1,j))
		elif self.maze[i-1][j] != '%':
			neighbors.append((i-1, j))
		elif self.maze[i][j+1] != '%':
			neighbors.append((i, j+1))
		elif self.maze[i][j-1] != '%':
			neighbors.append((i, j-1))

		return neighbors


#Track path in driver
	def move(self, next_loc):
		self.current_loc = next_loc
		self.cost += 1
		i,j = self.current_loc

		if self.maze[i][j] = '.':
			self.collected_rewards += 1


	def goalTest(self):
		if self.collected_rewards == self.total_rewards:
			return True
		else:
			return False