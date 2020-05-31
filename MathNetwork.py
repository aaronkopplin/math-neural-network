import NeuralNetwork
import math


def convert_activation_to_binary(activation: list):
    return [int(val >= .5) for val in activation]


def judge_fitness(expected: list, actual: list):
    # expected is the 0, 1, 1, 0, ...
    # actual is the .5672, .3572, .01124, .78872 ...
    if len(expected) != len(actual):
        raise ValueError("the length of the expected and actual are not the same. cannot judge fitness")

    # square the differences and sum. Lower score is better
    return sum([math.pow((first - second), 2) for first, second in zip(expected, actual)])


class MathNetwork:
    def __init__(self, layout):
        if isinstance(layout, list):
            self.network = NeuralNetwork.NeuralNetwork(layout)
        if isinstance(layout, NeuralNetwork.NeuralNetwork):
            self.network = layout
        self.cumulative_fitness = 0
        self.trials = 0

    def get_genes(self):
        return self.network

    def get_fitness(self):
        return self.cumulative_fitness / self.trials

    def compute(self, first: list, second: list, expected: list):
        if len(first + second) != len(self.network.layers[0].nodes[0].synapses):
            raise ValueError(str(len(first + second)) + " != " + str(len(self.network.layers[0].nodes)) +
                             str(first + second))
        actual = self.network.fire(first + second)
        actual = convert_activation_to_binary(actual)
        self.trials += 1
        self.cumulative_fitness += judge_fitness(expected, actual)
        return actual

    # genes is the list of layers of the mate
    def mate(self, genes: NeuralNetwork.NeuralNetwork, mutation_rate: int):
        return MathNetwork(self.network.mate(genes.layers, mutation_rate))
