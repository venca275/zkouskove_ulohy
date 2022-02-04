import argparse
from graph import Graph

def read(input_name):
        try:
            with open(input_name, "r", encoding="UTF-8") as physicFile:
                return physicFile.read().splitlines()
        except FileNotFoundError: # Verifies if the file exist
            print(f"CHYBA: Požadovaný soubor {input_name} neexistuje. Program skončí.")
            exit()
        except PermissionError: # Verifies if its acces to the file
            print(f"CHYBA: Nemám přístup k {input_name}.Program skončí.")
            exit()
        except ValueError as e: # Verifies if the file is valid
            print(f"CHYBA: Soubor {input_name} není validní. Program skončí.\n", e)
            exit()

# Main function, which creates queue list and than adds vertices
def breadth_first_search(graph):
    queue = []
    visited = [False for i in range(len(graph.vertices))]
    queue.append(graph.first_vertex)
    visited[graph.first_vertex.index] = True

    result = [[graph.first_vertex]]
    currentLevel = []

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


    except PermissionError:
        print(f"CHYBA: Nemůžu uložit výsledný soubor, protože nemám přístup k ukládání.")
        exit()
    except:
        print("CHYBA: Výsledný soubor se nepodařilo uložit.")
        exit()


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=False, default=None) # input file as an argument
parser.add_argument('-o', '--output', required=False, default=None) # output file as an argument
args = parser.parse_args()
if args.input != None and args.output != None:
    lines = read(args.input)
    result_tree = breadth_first_search(Graph(lines))
    save(args.output, result_tree)
else:
    print("Nezadali jste povinne argumenty (-i pro vstupni soubor, -o pro vystupni soubor.")
    exit()