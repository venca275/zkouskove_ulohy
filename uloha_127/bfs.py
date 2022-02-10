import argparse
from cProfile import label
from graph import Graph

# Function for reading the input file
def read(input_name):
        try:
            with open(input_name, "r", encoding="UTF-8") as physicFile:
                return physicFile.read().splitlines()
        except FileNotFoundError: # Verifies if the file exist
            print(f"ERROR: The requested file {input_name} does not exist. The program ends.")
            exit()
        except PermissionError: # Verifies if its acces to the file
            print(f"ERROR: I do not have access to {input_name}. The program ends.")
            exit()
        except ValueError as e: # Verifies if the file is valid
            print(f"ERROR: The file {input_name} is not valid. The program ends.\n", e)
            exit()

# Main function, which creates queue list and than adds vertices
def breadth_first_search(graph, first_vertex ):
    queue = []
    visited = [False for i in range(len(graph.vertices))]
    queue.append(first_vertex)
    visited[first_vertex.index] = True

    result = [[first_vertex]]
    currentLevel = []
    # Queue browsing and leveling
    while queue:
        vertex = queue.pop(0)
        if vertex in currentLevel:
            result.append(currentLevel)
            currentLevel = []
        
        for neighbour in vertex.neighbours:
            if not visited[neighbour.index]:
                queue.append(neighbour)
                visited[neighbour.index] = True
                currentLevel.append(neighbour)

    return result

# save the file under the given conditions
def save(file_name, tree): 
    try: 
        with open(file_name, "w", encoding="UTF-8") as physicFile:
            for level_index in range(len(tree)):
                row_str = ""

                for vertex in tree[level_index]:
                    if row_str=="":
                        row_str = str(vertex.label)
                    else:
                        row_str += " " + str(vertex.label) # inserts a space between the numbers in the line

                if level_index!=len(tree)-1:
                    row_str += '\n'
                    
                physicFile.write(row_str)

    # Exceptions for saving
    except PermissionError:
        print(f"ERROR: I can't save the resulting file because I don't have access to save.")
        exit()
    except:
        print("ERROR: The resulting file could not be saved.")
        exit()

# Opening the input and output files as an arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=False, default=None) # input file as an argument
parser.add_argument('-o', '--output', required=False, default=None) # output file as an argument
args = parser.parse_args()
if args.input != None and args.output != None:
    lines = read(args.input)
    g = Graph(lines)
    begin_vertex = list(g.vertices.values())[0] # Getting the first vertex
    result_tree = breadth_first_search(Graph(lines), begin_vertex)
    save(args.output, result_tree)
else:
    print("You did not enter mandatory arguments (-i for the input file, -o for the output file.")
    exit()