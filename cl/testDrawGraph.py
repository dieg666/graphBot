import networkx as nx
import matplotlib.pyplot as plt


def drawGraph(G, idEnquesta):
    pos = nx.circular_layout(G)
    nodes = G.nodes()
    labels = {}
    for node in nodes:
        labels[node] = node
    nx.draw_networkx_nodes(G, pos)
    colors = [G[u][v]['color'] for u, v in G.edges()]
    nx.draw_networkx_edges(
            G,
            pos,
            edgelist=G.edges(),
            edge_color=colors)
    labelItem = dict(
            [((u, v,), d['labelItem'])for u, v, d in G.edges(data=True)])
    labelAlternativa = dict(
            [((u, v,), d['labelAlternativa'])for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=labelItem,
            font_color='blue',
            font_size=10)
    nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=labelAlternativa,
            font_color='green',
            font_size=10)
    nx.draw_networkx_labels(
            G,
            pos,
            labels,
            font_size=10)
    # a = nx.get_node_attributes(G, 'answer')
    # print (a['R1'])
    # a = (G['END'])
    # print (a=={})
    # plt.show()
    plt.savefig("../GeneratedGraphs/"+idEnquesta+".png", bbox_inches='tight')
