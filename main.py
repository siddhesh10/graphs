import sys
sys.path.insert(0, 'C:/Users/sidd/Desktop/graphs/')
import dfs
import node
import bfs

A=node.node("A")
B=node.node("B")
C=node.node("C")
D=node.node("D")
E=node.node("E")

A.links.append(B)
A.links.append(C)
B.links.append(D)
D.links.append(E)

dfs.dfs().depth_first_search(A)
bfs.bfs().breadth_first_search(A)
