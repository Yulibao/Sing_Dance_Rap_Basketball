import networkx as nx
import random


def pagerank(G, weight='weight', alpha=0.85,
             max_iter=1000,
             tol=1.0e-6,
             nstart=None):
    if len(G) == 0:
        return {}

    out_degree_dic = G.out_degree()
    N = G.number_of_nodes()

    # Choose fixed starting vector if not given
    if nstart is None:
        x = dict.fromkeys(G, random.random())
    else:
        # Normalized nstart vector
        s = float(sum(nstart.values()))
        x = dict((k, v / s) for k, v in nstart.items())

    # power iteration: make up to max_iter iterations
    for _ in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        for n in x:
            # this matrix multiply looks odd because it is
            # doing a left multiply x^T=xlast^T*W
            for nbr in G[n]:
                x[nbr] += (alpha * xlast[n] * G[n][nbr][weight]) / out_degree_dic[n]
            x[n] += (1.0 - alpha)
        # check convergence, l1 norm
        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < N * tol:
            return x
    raise nx.PowerIterationFailedConvergence(max_iter)
