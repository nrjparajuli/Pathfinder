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

    agent = Agent(start_loc, total_rewards, maze)

    return agent

def single_bfs(agent):
    queue = []
    path = [agent.getCurrentLoc()]
    visited = [agent.getCurrentLoc()]

    for i in agent.getNeighbors():
        queue.append(i)

    while queue != []:
        next_loc = queue.pop(0)
        agent.move(next_loc)
        visited.append(next_loc)

        if agent.goalTest():
            print("SUCCESS")
            break

        for i in agent.getNeighbors():
            if i not in visited:
                queue.append(i)
                path.index([i]).append()



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


