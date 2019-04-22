# Colors
EDGE_COLOR = '#B2DBBF' 
NODE_COLOR_1 = '#F3FFBD' 
NODE_COLOR_2 = '#247BA0'
EXTRA_COLOR_1 = '#FF1654' 
EXTRA_COLOR_2 = '#70C1B3'


# Stylesheet
default_stylesheet = [
    # style for all nodes
    {
        'selector': 'node',
        'style': {
            'label': 'data(id)',
            'color': EXTRA_COLOR_2,
            'text-margin-y': -2,
        },
    },
    # style specific nodes
    {
        'selector': '[node_type *= "entity"]',
        'style': {
            'background-color': NODE_COLOR_1,
            'border-width': 1,
            'border-color': EDGE_COLOR,
            'width': 10,
            'height': 10,
            'font-size': 7,
        }
    },
    {
        'selector': '[node_type != "entity"]',
        'style': {
            'background-color': NODE_COLOR_2, 
            'border-width': 1,
            'border-color': EDGE_COLOR,
            'width': 10,
            'height': 10,
            'font-size': 5,
        }
    },
    # style all edges
    {
        'selector': 'edge',
        'style': {
            'line-color': EDGE_COLOR,
            'mid-target-arrow-shape': 'vee',
            'mid-target-arrow-color': EDGE_COLOR,
            'width': 1,
            'arrow-scale': 0.5,
        }
    },
]

