import networkx as nx ## aka le s
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Initialize an empty graph
    G = nx.Graph()

    # Read the file and add edges to the graph
    with open('input2.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            component = parts[0].strip()
            connected_components = parts[1].strip().split()

            for connected_component in connected_components:
                G.add_edge(component, connected_component)

    # Calculate edge betweenness centrality (strongness of links/redondancy)
    edge_betweenness = nx.edge_betweenness_centrality(G)

    # Sort edges by betweenness centrality
    sorted_edges = sorted(edge_betweenness.items(), key=lambda x: x[1], reverse=True)

    # Remove the top 3 edges
    for i in range(3):
        edge = sorted_edges[i][0]
        G.remove_edge(*edge)

    # Print the number of nodes in each connected component
    print([len(c) for c in nx.connected_components(G)])

    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.show()
