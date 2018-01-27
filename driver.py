from agent import Agent # import class file
import argparse # used for parsing arguments

# Parsing arguments from the command line.
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, \
        help="Input file that contains a representation of a maze", required=True)
    parser.add_argument("-a", "--algorithm", type=str, \
        help="Choose preferred algorithm. dfs - Depth First Search, \
        bfs - Breadth First Search, gbfs - Greedy Best Fisrt Search, \
        sastar - single-reward A* Search, mastar - multi-reward A* search",required=True)
    return parser.parse_args()

def initializeAgent(input_file):
    maze = []
    total_rewards = 0 
    row = 0
    start_loc = (0,0)

    for lines in input_file:
        column = 0
        line_maze = []
        for line in lines.strip():
            if line == '.':
                total_rewards += 1
            elif line == 'P':
                start_loc = (row, column)
            line_maze.append(line)
            column += 1
        maze.append(line_maze)
        row += 1

    print(total_rewards)
    agent = Agent(start_loc, total_rewards, maze)

    return agent

def single_bfs(agent):
    start_loc = agent.getCurrentLoc()
    queue = [start_loc]
    pred_of = {}
    pred_of[start_loc] = None
    visited = []

    # for i in agent.getNeighbors():
    #     queue.append(i)

    while queue != []:

        next_loc = queue.pop(0)


        if agent.goalTest():
            return construct_path(start_loc, pred_of, agent)

        for i in agent.getNeighbors():
            if i not in visited and i not in queue:
                queue.append(i)
                pred_of[i] = agent.getCurrentLoc()

        agent.move(queue[0])
        visited.append(next_loc)

def construct_path(start, pred, agent):
    current = agent.getCurrentLoc()
    path = []

    while current != start:
        path.append(current)
        current = pred[current]

    path.append(start)
    return display_path(agent, path)

def display_path(agent, path):
    maze = agent.getMaze()
    
    for i,j in path:
        maze[i][j] = '#'

    for i in maze:
        print(''.join(i))


def single_dfs(agent):
    pass

def single_gbfs(agent):
    pass

def single_astar(agent):
    pass

def multi_astar(agent):
    pass

if __name__ == "__main__":
    args = parser()
    #func_avail = [bfs, dfs, gbfs, astar]
    try:
        input_file = open(args.input, 'r')
        algorithm = args.algorithm
    except IOError:
        print("Error handling Input file. Check the correctness of specified file name.")

    mouse = initializeAgent(input_file)

    if algorithm == 'bfs':
        single_bfs(mouse)
    elif algorithm == 'dfs':
        single_dfs(mouse)
    elif algorithm == 'gbfs':
        single_gbfs(mouse)
    elif algorithm == 'sastar':
        single_astar(mouse)
    else:
        multi_astar(mouse)


