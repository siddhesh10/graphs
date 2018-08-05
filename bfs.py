class bfs(object):

    def breadth_first_search(self,node):
        queue=[]

        queue.append(node)
        node.visited=True

        while queue:
            s=queue.pop(0)
            
            print(s.name)

            for neighbours in s.links:
                if neighbours.visited==False:
                    queue.append(neighbours)
                    neighbours.visited=True
