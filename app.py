import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
import json

EDGE_COLOR = '#F2EFD7'
NODE_COLOR_1 = '#19888E'
NODE_COLOR_2 = '#19647E'
EXTRA_COLOR_1 = '#583575'
EXTRA_COLOR_2 = '#CB8618'

def load_data():
    with open('data/example_data.json', 'r') as f:
        return json.load(f)

data = load_data() 

graph_cyto = cyto.Cytoscape(
    id='cyto-graph',
    layout={'name': 'cose'},  
    style={'width': '100%', 'height': '600px'},
    elements=data['elements'],
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
                'target-arrow-shape': 'triangle',
            }
        },
    ]
)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Graph Explorer'),
    html.Div('Example data.'),
    html.Div(graph_cyto)
])

if __name__ == '__main__':
        app.run_server(debug=True)
