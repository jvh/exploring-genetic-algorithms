import random


POPULATION_SIZE = 500
TARGET = 'hello world'
MUTATION_RATE = 1/len(TARGET)
# This is the number of mutations which must take place before target is found
speed = 0
CHAR_POSSIBILITIES = 'abcdefghijklmnopqrstuvwxyz '

# This holds all strings that we have come across, allows for lookup even when they are not in the current string
# selection in the case in which they have been seen before
string_fitness = {}


def fitness(word):
    """
    Calculates the fitness of a certain word, measured by how many characters are correctly in the right place relative
    to the target
    :param word: The word we are testing the fitness of
    :return: (float) The fitness of that word
    """
    fitness_measure = 0
    for i in range(len(word)):
        if word[i] == TARGET[i]:
            fitness_measure += 1

    return fitness_measure


def initialise(population_size=POPULATION_SIZE):
    """
    Initialises population of N size (in this case defined by POPULATION_SIZE). These strings are bounded to be only
    lowercase English alphabetic characters, along with the space character.

    :param: (int) The size of the population needed
    :return: ({str: int}) N strings with their corresponding fitness
    """
    # Holds a list of the current strings with POPULATION_SIZE elements
    current_strings = []

    for i in range(population_size):
        new_str = ''
        for y in range(len(TARGET)):
            ran_char = random.choice(CHAR_POSSIBILITIES)
            new_str += ran_char
        string_fitness[new_str] = fitness(new_str)
        current_strings.append(new_str)

    return string_fitness, current_strings


def random_2_members(population):
    """
    Chooses 2 random members of the population, given that they are not in the same position
    :param: ([[char]]) List of population members

    :return: ([char]) Random member 1
    :return: (float) Random member 1's fitness
    :return: (int) Random member 1's index in the population
    :return: ([char]) Random member 2
    :return: (float) Random member 2's fitness
    :return: (int) Random member 2's index in the population
    """
    index_1 = index_2 = -1
    while index_1 == index_2:
        index_1 = random.randint(0, len(population) - 1)
        index_2 = random.randint(0, len(population) - 1)

    ran_word_1 = population[index_1]
    ran_word_2 = population[index_2]
    fitness_1 = string_fitness[''.join(ran_word_1)]
    fitness_2 = string_fitness[''.join(ran_word_2)]

    return ran_word_1, fitness_1, index_1, ran_word_2, fitness_2, index_2


def mutate(string):
    """
    Mutate a given string with a chance of MUTATION_RATE of a char taking on a random char

    :param: (str) Given string to mutate
    :return: (str) Mutated string
    :return: (int) Number of mutations taken
    """
    number_of_mutations = 0
    string = list(string)
    for i in range(len(string)):
        random_num = random.randint(1, len(TARGET))
        # Randomly select letter
        if random_num == 1:
            number_of_mutations += 1

            temp = string.copy()
            temp[i] = random.choice(CHAR_POSSIBILITIES)
            temp_str = ''.join(temp)

            # Adding to string_fitness if never seen before
            if temp_str not in string_fitness:
                string_fitness[temp_str] = fitness(temp)

            if string_fitness[temp_str] > string_fitness[''.join(string)]:
                string = temp

    return ''.join(string), number_of_mutations
