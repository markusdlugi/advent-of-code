import networkx as nx
from networkx.algorithms.clique import enumerate_all_cliques


# Simple solution with built-in networkx algorithm
def solve_with_networkx(G):
    all_cliques = list(enumerate_all_cliques(G))
    t_cliques = sum(any(node.startswith("t") for node in clique) for clique in all_cliques if len(clique) == 3)
    print(t_cliques)

    max_clique = sorted(all_cliques[-1])
    print(*max_clique, sep=",")


# Complicated & slow original solution
def solve_manually(G):
    inter_connected = set()
    for edge in G.edges():
        a, b = edge
        for node in G.nodes():
            if node == a or node == b:
                continue
            if G.has_edge(a, node) and G.has_edge(b, node):
                inter_connected.add(tuple(sorted([a, b, node])))

    with_t = set()
    for a, b, c in inter_connected:
        if a.startswith("t") or b.startswith("t") or c.startswith("t"):
            with_t.add((a, b, c))

    print(len(with_t))

    groups = inter_connected
    while True:
        new_groups = set()
        for group in groups:
            for node in G.nodes():
                if node in group:
                    continue
                if all(G.has_edge(node, x) for x in group):
                    new = [*group, node]
                    new_groups.add((tuple(sorted(new))))
        if len(new_groups) == 0 or new_groups == groups:
            break
        else:
            groups = new_groups

    print(*sorted(*groups), sep=",")


if __name__ == '__main__':
    lines = [line.strip() for line in open("input/23.txt")]

    G = nx.Graph()
    for line in lines:
        a, b = line.split('-')
        G.add_edge(a, b)

    # solve_manually(G)
    solve_with_networkx(G)
