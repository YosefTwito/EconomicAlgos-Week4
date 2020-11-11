import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import time

total_time = 0

for i in range(400):
    G = nx.Graph()
    mates = ("A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13","A14","A15","A16","A17","A18","A19","A20","A21","A22","A23","A24","A25","A26","A27","A28","A29","A30","A31","A32","A33","A34","A35","A36","A37","A38","A39","A40")

    G.add_nodes_from(mates, bipartite='mates')

    rooms = ("B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14","B15","B16","B17","B18","B19","B20","B21","B22","B23","B24","B25","B26","B27","B28","B29","B30","B31","B32","B33","B34","B35","B36","B37","B37","B39","B40")
    G.add_nodes_from(rooms, bipartite='rooms')

    for x in mates:
        for y in rooms:
            w = random.randrange(10,100,5)
            G.add_weighted_edges_from([(x,y,w)])

    # print(G.edges(data=True))
    # print('\n')

    start_time = time.time()
    maxG = nx.max_weight_matching(G)
    end_time = (time.time() - start_time)
    total_time+=end_time
# print("Size: %s" % (len(mates)))
print("---- %s seconds ---" % (total_time/400))





# pos = {node:[0, i] for i,node in enumerate(mates)}
# pos.update({node:[1, i] for i,node in enumerate(rooms)})
# nx.draw(G, pos, with_labels=True)
# nx.draw_networkx_labels(G, pos)
#
# plt.show()

# G = nx.complete_bipartite_graph(3, 3)
# print(G.edges(data=True))

