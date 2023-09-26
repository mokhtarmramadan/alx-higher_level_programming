class Node:
    def __init__(self, data, next_node):
        self.__data = data
        self.__next_node = next_node


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data


    @property
    def next_node(self):
        return self.__next_node


    @next_node.setter
    def next_node(self, next_node=None):
        if not isinstance(next_node, Node) or not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node



