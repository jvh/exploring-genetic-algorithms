import common_functions as cf


def main():
    """
    Runs the main loop after initialisation has taken place, and attempts to find a solution.

    Prints metrics of the solution once found.
    """
    seen_strings, population = cf.initialise(1)
    solution_found = False
    solution = ''
    total_mutations = 0
    generation = 0

    while not solution_found:
        max_fitness = 0
        best_string = ''

        for i in range(len(population)):
            mutated, mutations = cf.mutate(population[i])
            population[i] = mutated
            total_mutations += mutations

            if population[i] in seen_strings:
                word_fitness = seen_strings[population[i]]
            else:
                word_fitness = cf.fitness(population[i])

            if word_fitness > max_fitness:
                max_fitness = word_fitness
                best_string = ''.join(population[i])

            if population[i] == cf.TARGET:
                solution_found = True
                solution = ''.join(population[i])
                break

        if not solution_found:
            generation += 1
        print("Best solution found at generation {}: '{}', with fitness {}".format(generation, best_string,
                                                                                   max_fitness))

    print("\nSolution '{}' has been found.".format(solution))
    print("Finished with {} total mutations.".format(total_mutations))
    print("The solution was found in {} generations.".format(generation))


if __name__ == '__main__':
    main()
