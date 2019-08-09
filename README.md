# methinks it is like a weasel

Creation of a simple genetic algorithm in order to find the phrase "methinks it is like a weasel", with and without the use of crossover. We begin with a random 28-character string at which point we have a 'generation' where some letters are changed, this new string is given a score, the _fitness_, whereby a higher fitness indicates a string where more letters are the same as in the target string.

We measure speed in terms of the number of mutations which needed to take place to reach the solution. Given this, I found that a genetic algorithm with crossover performed better than without, often up to 4x better.

There are 3 methods explored in this repository: genetic algorithm _with_ crossover, genetic algorithm _without_ crossover, and a simple mutation hill climber algorithm.

## Usage Instructions

These commands should both be ran in the **top-level** directory of the repository.

### Prerequisites

Install [python3](https://www.python.org/download/releases/3.0/).

### Commands

* Mutation hill-climber: `python src/python src/mutation_hill_climber.py`.
* Genetic algorithm _without_ crossover: `python src/ga_without_crossover.py`.
* Genetic algorithm _with_ crossover: `python src/ga_without_crossover.py`.
