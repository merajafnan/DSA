
class graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes = num_nodes
        self.data = [[] for x in range(num_nodes)]

        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
            # print(self.data)

    def __repr__(self):
        return '\n'.join(["{}: {}".format(n,neighbor) for n,neighbor in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()

edges=[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
num_nodes = 5
graph1 = graph(num_nodes,edges)
print(graph1)
















# l1 = [1,2,3,5]
# l1.append(4)
# print(l1)

# l2 = [[] for x in range(10)]
# print(l2)
# l2[1].append(2)
# print(l2)

# edges=[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
# print(type(edges),"---",edges)
# for n1,n2 in edges:
#     print(n1,n2)
