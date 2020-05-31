import Neuron
import random


# Neural Networks consist of synapse-neuron layers.
class Layer:
    def __init__(self, num_left_nodes: int, num_right_nodes: int):
        # each node has num_left_nodes synapses
        self.nodes = [Neuron.Neuron(num_left_nodes) for x in range(num_right_nodes)]

    def fire(self, data_input: list):
        return [node.fire(data_input) for node in self.nodes]

    def mutate(self):
        random.choice(self.nodes).mutate()

    def get_genes(self):
        return self.nodes

    def mate(self, nodes: list):
        new_nodes = []
        for new_node, old_node in zip(nodes, self.nodes):
            new_nodes.append(new_node.mate(old_node.get_genes()))

        new_layer = Layer(0, 0)
        new_layer.nodes = new_nodes
        return new_layer

    def __str__(self):
        return "layer: " + str([str(node) for node in self.nodes])
