from graphviz import Digraph

g = Digraph('G', filename='cluster.gv')

# NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
#       so that Graphviz recognizes it as a special cluster subgraph

# with g.subgraph(name='cluster_0') as c:
#     c.attr(style='filled')
#     c.attr(color='lightgrey')
#     c.node_attr.update(style='filled', color='white')
#     c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
#     c.attr(label='process #1')
#
# with g.subgraph(name='cluster_1') as c:
#     c.node_attr.update(style='filled')
#     c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
#     c.attr(label='process #2')
#     c.attr(color='blue')

g.edge('raw image', 'culled images')
g.edge('culled images', 'image vectors')

g.edge('raw audio', 'preprocessed audio')
g.edge('preprocessed audio', 'audio vectors')

g.edge('image vectors', 'data samples')
g.edge('audio vectors', 'data samples')

g.edge('trained model', 'predictions')
g.edge('data samples', 'predictions')

with open('graph.dot', 'w') as fp:
    fp.write(g.source)
