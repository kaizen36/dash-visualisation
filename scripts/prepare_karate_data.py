import networkx as nx
import json
import os

def main():
    g = nx.karate_club_graph()
    karate_cytoscape_data = nx.readwrite.json_graph.cytoscape_data(g)
    
    path = 'data/karate_cytoscape_data.json'
    dir_path = os.path.dirname(path)
    print(dir_path)
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print('made directory: {}'.format(dir_path))
        
    with open(path, 'w') as f:
        json.dump(
            karate_cytoscape_data, 
            f, 
            separators=(',',':'), 
            indent=4
        )
    
    print('data written to: {}'.format(path))
        
if __name__=='__main__':
    main()