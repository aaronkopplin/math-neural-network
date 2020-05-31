import GenerateDataSet
import NeuralNetwork
import MathNetwork
import random


# take two seven bit numbers as input, and output one 8 bit number
# two hidden layers
default_network = [14, 10, 8]


# define the mutation rate
mutation_rate = 3  # the number of genes to mutate at each child


# define the number of generations
num_generations = 100

population = [MathNetwork.MathNetwork(default_network) for i in range(100)]

count = 0
while count < num_generations:
    data = [GenerateDataSet.get_data_set(7) for i in range(50)]

    # test the data on the population
    scores = []
    for member in population:
        correct_bits_per_trial = []
        for trial in data:
            actual = member.compute(trial[0], trial[1], trial[2])
            correct = 0
            for guess, bit in zip(actual, trial[2]):
                if guess == bit:
                    correct += 1

            correct_bits_per_trial.append(correct)
        scores.append(member.get_fitness())

    print("generation: " + str(count) + "\tpopulation average fitness: " + str(sum(scores) / len(scores)) +
          "\tavg correct bits: " + str(sum(correct_bits_per_trial) / len(correct_bits_per_trial)))

    # sort the population based on fitness
    population.sort(key=lambda x: x.get_fitness(), reverse=True)

    # select the better half of the population
    reproducers = population[:int(len(population) / 2)]

    # create a child population
    children = []
    for i in range(len(reproducers)):
        children.append(random.choice(reproducers).mate(random.choice(reproducers).get_genes(), mutation_rate))
        children.append(random.choice(reproducers).mate(random.choice(reproducers).get_genes(), mutation_rate))

    population = children
    count += 1
