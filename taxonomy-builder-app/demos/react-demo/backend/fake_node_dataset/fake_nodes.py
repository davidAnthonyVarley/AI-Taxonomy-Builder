# this file exists purely to create a test dataset, will not be used to generate real responses in the production app
# mostly for unit tests


def load_fake_nodes():

    nodes = [
        {
            "id": "node-1",
            "type": "textUpdater",
            "position": {"x": 100, "y": 200},
            "data": {"label": "Circle Node"},
            "width": 50,
            "height": 50,
            "selected": False,
            "dragging": False,
        },
        {
            "id": "node-2",
            "type": "textUpdater",
            "position": {"x": 300, "y": 400},
            "data": {"label": "Rectangle Node"},
            "width": 80,
            "height": 60,
            "selected": True,
            "dragging": False,
        },
        {
            "id": "node-3",
            "type": "textUpdater",
            "position": {"x": 500, "y": 100},
            "data": {"label": "Triangle Node"},
            "width": 70,
            "height": 70,
            "selected": False,
            "dragging": True,
        },
        {
            "id": "node-4",
            "type": "textUpdater",
            "position": {"x": 200, "y": 300},
            "data": {"label": "Star Node"},
            "width": 60,
            "height": 60,
            "selected": True,
            "dragging": False,
        },
        {
            "id": "node-5",
            "type": "textUpdater",
            "position": {"x": 400, "y": 500},
            "data": {"label": "Ellipse Node"},
            "width": 90,
            "height": 70,
            "selected": False,
            "dragging": True,
        },
        {
            "id": "node-6",
            "type": "textUpdater",
            "position": {"x": 600, "y": 200},
            "data": {"label": "Hexagon Node"},
            "width": 80,
            "height": 60,
            "selected": True,
            "dragging": True,
        },
        {
            "id": "node-7",
            "type": "textUpdater",
            "position": {"x": 150, "y": 450},
            "data": {"label": "Pentagon Node"},
            "width": 70,
            "height": 70,
            "selected": False,
            "dragging": False,
        },
        {
            "id": "node-8",
            "type": "textUpdater",
            "position": {"x": 350, "y": 250},
            "data": {"label": "Octagon Node"},
            "width": 60,
            "height": 80,
            "selected": True,
            "dragging": True,
        },
        {
            "id": "node-9",
            "type": "textUpdater",
            "position": {"x": 550, "y": 450},
            "data": {"label": "Diamond Node"},
            "width": 80,
            "height": 80,
            "selected": False,
            "dragging": False,
        },
    ]
    return nodes


# these edges were made specifically to connect the nodes above
def load_fake_edges():
    edges = [
        {"id": "edge-1", "source": "node-1", "target": "node-2"},
        {"id": "edge-2", "source": "node-2", "target": "node-3"},
        {"id": "edge-3", "source": "node-3", "target": "node-4"},
        {"id": "edge-4", "source": "node-4", "target": "node-5"},
        {"id": "edge-5", "source": "node-5", "target": "node-6"},
        {"id": "edge-6", "source": "node-6", "target": "node-7"},
        {"id": "edge-7", "source": "node-7", "target": "node-8"},
        {"id": "edge-8", "source": "node-8", "target": "node-9"},
        {"id": "edge-9", "source": "node-9", "target": "node-1"},
    ]
    return edges
