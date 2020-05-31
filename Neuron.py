import math
import random


# static methods
def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def new_gene():
    return random.uniform(-1.2, 1.2)


class Neuron:
    def __init__(self, synapses, bias=''):
        if isinstance(synapses, int):
            self.synapses = [new_gene() for i in range(synapses)]
        elif isinstance(synapses, list):
            self.synapses = synapses
        else:
            raise ValueError("must pass in list or int for synapses")

        self.bias = new_gene()
        if bias != '':
            self.bias = bias

    def mate(self, genes: list):
        if len(genes[0]) != len(self.synapses):
            raise ValueError("incorrect genes length")

        new_genes = []
        for foreign_gene, old_gene in zip(genes[0], self.synapses):
            new_genes.append(foreign_gene if random.randint(0, 1) else old_gene)

        new_bias = genes[1] if random.randint(0, 1) else self.bias

        return Neuron(new_genes, new_bias)

    def fire(self, input_values: list):
        if len(input_values) != len(self.synapses):
            raise ValueError("input values: " + str(len(input_values)) + " != synapses: " + str(len(self.synapses)))

        return sigmoid(sum([val * weight + self.bias for val, weight in zip(input_values, self.synapses)]))

    def accept_genes(self, new_synapses: list, new_bias: int):
        self.synapses = new_synapses
        self.bias = new_bias

    def get_genes(self):
        return self.synapses, self.bias

    def mutate(self):
        temp_genes = self.synapses
        temp_genes.append(self.bias)
        temp_genes[random.randint(0, (len(temp_genes) - 1))] = new_gene()
        self.accept_genes(new_bias=temp_genes.pop(), new_synapses=temp_genes)

    def __str__(self):
        return "synapses: " + str(self.synapses) + " bias: " + str(self.bias)
