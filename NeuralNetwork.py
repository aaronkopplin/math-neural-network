import random
import Layer


class NeuralNetwork:
    def __init__(self, layout: list):
        # layout is a list of the numbers of nodes in the network
        # ex) [2, 3, 4, 5]... 2 inputs, 5 outputs
        self.topology = layout
        self.layers = [Layer.Layer(layout[x], layout[x + 1]) for x in range(len(layout) - 1)]

    def mutate(self):
        random.choice(self.layers).mutate()

    def mate(self, layers: list, mutation_rate: int):
        new_layers = []
        for new_layer, old_layer in zip(layers, self.layers):
            new_layers.append(new_layer.mate(old_layer.get_genes()))

        new_net = NeuralNetwork([])
        new_net.layers = new_layers

        for i in range(mutation_rate):
            new_net.mutate()

        return new_net

    def get_genes(self):
        return self.layers

    def fire(self, input_values: list):
        # if len(input_values) !=

        temp = input_values
        for layer in self.layers:
            temp = layer.fire(temp)

        # return the activation of the last layer of neurons
        return temp

    def __str__(self):
        return str([str(layer) for layer in self.layers])
