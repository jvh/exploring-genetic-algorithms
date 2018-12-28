import common_functions as cf
import random


def crossover(parent1, parent2):
    """
    Creates a child from the crossover of 2 parents, with each parent having an equal chance of passing each separate
    gene.

    :param parent1: ([char]) The first parent
    :param parent2: ([char]) The second parent
    :return: ([char]) The child
    """
    child = []
    for i in range(len(parent1)):
        rand_int = random.randint(0, 1)
        # When zero, we take parent1's gene
        if rand_int == 0:
            child.append(parent1[i])
        else:
            child.append(parent2[i])

        # Adding to string_fitness if never seen before
        if ''.join(child) not in cf.string_fitness:
            cf.string_fitness[''.join(child)] = cf.fitness(child)

    return child


def main():
    """
    Runs the main loop after initialisation has taken place, and attempts to find a solution.

    Prints metrics of the solution once found.
    """
    seen_strings, population = cf.initialise()
    solution_found = False
    total_mutations = 0
    generation = 0

    while True:
        max_fitness = 0
        best_string = ''

        # Selecting first parent #
        ran_word_1, fitness_1, _, ran_word_2, fitness_2, _ = cf.random_2_members(population)

        if fitness_1 > fitness_2:
            parent1 = ran_word_1
        else:
            parent1 = ran_word_2

        # Selecting second parent #
        ran_word_1, fitness_1, _, ran_word_2, fitness_2, _ = cf.random_2_members(population)

        if fitness_1 > fitness_2:
            parent2 = ran_word_1
        else:
            parent2 = ran_word_2

        # Creation of child #
        child = crossover(parent1, parent2)
        mutated_child, mutations = cf.mutate(child)
        child_str = ''.join(mutated_child)

        # If mutated child is solution, break #
        if child_str == cf.TARGET:
            solution = ''.join(child)
            break
        else:
            if seen_strings[child_str] >= max_fitness:
                max_fitness = seen_strings[child_str]
                best_string = child_str

        # Choosing individual to replace in population #
        ran_word_1, fitness_1, index_1, ran_word_2, fitness_2, index_2 = cf.random_2_members(population)

        if fitness_1 > fitness_2:
            population[index_2] = child
        else:
            population[index_1] = child

        total_mutations += mutations

        if not solution_found:
            generation += 1

        print("Best solution found at generation {}: '{}', with fitness {}".format(generation, best_string,
                                                                                   max_fitness))

    print("\nSolution '{}' has been found.".format(solution))
    print("Finished with {} total mutations.".format(total_mutations))
    print("The solution was found in {} generations.".format(generation))


if __name__ == '__main__':
    main()
