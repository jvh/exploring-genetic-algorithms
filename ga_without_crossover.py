import common_functions as cf
import random


def main():
    """
    Runs the main loop after initialisation has taken place, and attempts to find a solution.

    Prints metrics of the solution once found.
    """
    population = cf.initialise()
    solution_found = False
    solution = ''
    total_mutations = 0
    generation = 0

    while not solution_found:
        max_fitness = 0
        best_string = ''

        index_1 = index_2 = -1
        while index_1 == index_2:
            index_1 = random.randint(0, len(cf.TARGET) - 1)
            index_2 = random.randint(0, len(cf.TARGET) - 1)

        ran_word_1 = population[index_1]
        ran_word_2 = population[index_2]
        fitness_1 = cf.fitness(ran_word_1)
        fitness_2 = cf.fitness(ran_word_2)

        # Picking best parent (out of the random choice)
        if fitness_1 > fitness_2:
            parent = ran_word_1
        else:
            parent = ran_word_2

        # Getting child from parent
        child, mutations = cf.mutate(parent)

        if child == list(cf.TARGET):
            solution_found = True
            solution = ''.join(child)
            break
        else:
            if cf.fitness(child) >= max_fitness:
                max_fitness = cf.fitness(child)
                best_string = ''.join(child)

        # Select 2 more random population members and choose who to replace according to population
        index_1 = index_2 = -1
        while index_1 == index_2:
            index_1 = random.randint(0, len(cf.TARGET) - 1)
            index_2 = random.randint(0, len(cf.TARGET) - 1)

        ran_word_1 = population[index_1]
        ran_word_2 = population[index_2]
        fitness_1 = cf.fitness(ran_word_1)
        fitness_2 = cf.fitness(ran_word_2)

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
