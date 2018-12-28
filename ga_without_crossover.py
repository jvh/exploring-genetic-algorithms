import common_functions as cf
import random


def main():
    """
    Runs the main loop after initialisation has taken place, and attempts to find a solution.

    Prints metrics of the solution once found.
    """
    seen_strings, population = cf.initialise()
    solution_found = False
    solution = ''
    total_mutations = 0
    generation = 0

    while not solution_found:
        max_fitness = 0
        best_string = ''

        # Selecting 2 random members, picking best one to be parent (out of the random choice) #
        ran_word_1, fitness_1, _, ran_word_2, fitness_2, _ = cf.random_2_members(population)

        if fitness_1 > fitness_2:
            parent = ran_word_1
        else:
            parent = ran_word_2

        child, mutations = cf.mutate(parent)
        child_str = ''.join(child)

        # If mutated child is solution, break #
        if child_str == cf.TARGET:
            solution_found = True
            solution = ''.join(child)
            break
        else:
            if seen_strings[child_str] >= max_fitness:
                max_fitness = seen_strings[child_str]
                best_string = child_str

        # Select 2 more random population members and choose who to replace according to population #
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
