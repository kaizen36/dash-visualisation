import networkx as nx
import json

def main():
    g = nx.DiGraph()
    g.add_node('A', node_type='entity')
    for i in list('abcdefg'):
        g.add_node(i, node_type='field', type='string')
        g.add_edge('A', i)
    g.add_node('B', node_type='entity')
    for i in list('hijklmnop'):
        g.add_node(i, node_type='field', type='string')
        g.add_edge('B', i)
    g.add_edge('a', 'h')
    g.add_edge('b', 'i')
    g.add_edge('c', 'j')

    graph_data = nx.readwrite.json_graph.cytoscape_data(g)

    with open('data/example_data.json', 'w') as f:
        json.dump(graph_data, f, separators=(',',':'), indent=4)

if __name__=='__main__':
    main()
