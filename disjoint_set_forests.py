class Node:

    def __init__(self, value):

        self.rank = 0
        self.parent = self
        self.value = value

    def union(self, node1, node2):

        self.link(node1.find_set(), node2.find_set())

    def link(self, node1, node2):

        if node1.get_rank() > node2.get_rank():
            node2.set_parent(node1)
        else:
            node1.set_parent(node2)
            if node1.get_rank() == node2.get_rank():
                node2.increment_rank()

    def find_set(self):

        if self.parent != self:
            self.parent = self.parent.find_set()
        return self.parent

    def get_rank(self):
        return self.rank

    def increment_rank(self):
        self.rank = self.rank + 1

    def get_parent(self):
        return self.parent

    def set_parent(self, newparent):
        self.parent = newparent

    def get_value(self):
        return self.value
