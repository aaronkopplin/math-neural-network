import NeuralNetwork, Neuron, Layer
import random


def mate_networks(a: NeuralNetwork.NeuralNetwork, b: NeuralNetwork.NeuralNetwork):
    if a.topology != b.topology:
        raise ValueError("mated networks must have same topology")

    new_network = NeuralNetwork.NeuralNetwork([])  # empty network, will construct it here
    for a_layer, b_layer in zip(a.layers, b.layers):
        # empty layer, will construct it here
        new_layer = Layer.Layer(0, 0)
        for a_neuron, b_neuron in zip(a_layer.nodes, b_layer.nodes):
            new_synapses = []

            # randomly get genes from a or b neuron
            for a_synapse, b_synapse in zip(a_neuron.synapses, b_neuron.synapses):
                new_synapses.append(a_synapse) if random.getrandbits(1) else new_synapses.append(b_synapse)

            # randomly get a bias from either a or b neuron
            new_bias = a_neuron.bias if random.getrandbits(1) else b_neuron.bias

            # construct a new neuron from the randomly gathered genes
            new_neuron = Neuron.Neuron(0).accept_genes(new_synapses, new_bias)

            # add the node to the current layer
            new_layer.nodes.append(new_neuron)

        # add each new layer to the network
        new_network.layers.append(new_layer)

    return new_network

