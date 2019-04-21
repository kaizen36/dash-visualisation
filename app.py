import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import json


EDGE_COLOR = '#F2EFD7'
NODE_COLOR_1 = '#19888E'
NODE_COLOR_2 = '#19647E'
EXTRA_COLOR_1 = '#583575'
EXTRA_COLOR_2 = '#CB8618'


def load_data():
    with open('data/example_data.json', 'r') as f:
        return json.load(f)


def filter_data(data, filter_key, filter_value):
    new_data = dict()
    new_data['nodes'] = [
        n 
        for n in data['nodes']
        if n['data'][filter_key] == filter_value
    ]
    return new_data
    

data = load_data() 
default_elements = filter_data(data['elements'], 'node_type', 'entity')

graph_cyto = cyto.Cytoscape(
    id='cyto-graph',
    layout={'name': 'cose'},  
    style={'width': '100%', 'height': '600px'},
    elements=default_elements,
    stylesheet=[
        # style for all nodes
        {
            'selector': 'node',
            'style': {
                'label': 'data(id)',
            },
        },
        # style specific nodes
        {
            'selector': '[node_type *= "entity"]',
            'style': {
                'background-color': NODE_COLOR_1,
            }
        },
        {
            'selector': '[node_type != "entity"]',
            'style': {
                'background-color': NODE_COLOR_2, 
            }
        },
        # style all edges
        {
            'selector': 'edge',
            'style': {
                'line-color': EDGE_COLOR,
                'mid-target-arrow-shape': 'vee',
                'mid-target-arrow-color': EDGE_COLOR
            }
        },
    ]
)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Graph Explorer'),
    html.Div(
        graph_cyto,
        style={'width': '70%', 'display': 'inline-block', 'vertical-align': 'top'},
    ),
    html.Div(
        dcc.Markdown(id='hover-node-output'),
        style={'width': '25%', 'display': 'inline-block', 'vertical-align': 'top'},
    )
])


@app.callback(Output('cyto-graph', 'elements'), [
    Input('cyto-graph', 'tapNodeData'),],
    [State('cyto-graph', 'elements')]
)
def click_node(selected_node, current_elements):
    if selected_node is None:
        return default_elements

    _id = selected_node['id']
    _nodes = [n['data']['id'] for n in current_elements['nodes']]
    first_neighbour_edges = [
        e
        for e in data['elements']['edges']
        if _id == e['data']['source'] or _id == e['data']['target']
    ]
    first_neighbour_node_id = [
        e['data']['target'] 
        if _id == e['data']['source']
        else e['data']['source']
        for e in first_neighbour_edges         
    ]
    first_neighbour_nodes = [
        n
        for n in data['elements']['nodes']
        if n['data']['id'] in first_neighbour_node_id
    ]

    # add first neighbours
    current_elements['nodes'].extend(first_neighbour_nodes)

    # add first neighbour edges and all edges for nodes going to appear
    new_edges = [
        e
        for e in data['elements']['edges']
        if e['data']['source'] in _nodes + first_neighbour_nodes \
            or e['data']['target'] in _nodes + first_neighbour_nodes
    ]
    if 'edges' not in current_elements:
        current_elements['edges'] = []

    current_elements['edges'].extend(first_neighbour_edges)
    current_elements['edges'].extend(new_edges)

    return current_elements


@app.callback(
    Output('hover-node-output', 'children'), [
    Input('cyto-graph', 'mouseoverNodeData'),],
)
def mouse_over_node(node):
    if node is None:
        return 'Hint: Hover over a node to display its properties here.'
    else:
        return "```\n" + json.dumps(node, indent=4, separators=(',',':')) + "\n```"


if __name__ == '__main__':
        app.run_server(debug=True)
