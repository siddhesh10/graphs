class dfs(object):

    def depth_first_search(self,node):
        if not node.visited:
            print(node.name)
            node.visited=True
        for neighbour in node.links:
            self.depth_first_search(neighbour)
