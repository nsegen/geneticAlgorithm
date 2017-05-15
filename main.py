from dilemma_values import DilemmaValues

from random import randint


def paly(strategy_1, strategy_2):
    choice_1 = strategy_1[0][0] if strategy_2[2] is dilemma_values.cooperation else strategy_1[0][1]
    choice_2 = strategy_2[0][0] if strategy_1[2] is dilemma_values.cooperation else strategy_2[0][1]
    new_game = dilemma_values.compare(choice_1, choice_2)
    strategy_1[1] += new_game[0]
    strategy_2[1] += new_game[1]
    strategy_1[2] = choice_1
    strategy_2[2] = choice_2
    # print(new_game, strategy_1, strategy_2)
    # input()


def selection(population, number):

    fitness_population = [[ind, 0, dilemma_values.cooperation] for ind in population]

    for i in fitness_population:
        for j in fitness_population:
            if j is not i:
                paly(i, j)
    fitness_population.sort(key=lambda ind: -ind[1])
    return [ind[0] for ind in fitness_population][:number]


def mix(individual1, individual2):

    cut = randint(0, len(individual1) - 1)

    child_1 = list(individual1[:cut] + individual2[cut:])
    child_2 = list(individual2[:cut] + individual1[cut:])

    child_1[randint(0, len(child_1) - 1)] = not child_1[randint(0, len(child_1) - 1)]
    child_2[randint(0, len(child_2) - 1)] = not child_2[randint(0, len(child_2) - 1)]

    return [tuple(child_1), tuple(child_2)]


N = 150
dilemma_values = DilemmaValues(c=0.1, d=0.2, C=0.8, D=0.9)
population = []
for i in range(N):
    population.append(
        (
            dilemma_values.get_random_value(),
            dilemma_values.get_random_value(),
        )
    )

what_we_need = (dilemma_values.cooperation, dilemma_values.defence)
strategies = (
    (dilemma_values.cooperation, dilemma_values.cooperation),
    (dilemma_values.cooperation, dilemma_values.defence),
    (dilemma_values.defence, dilemma_values.cooperation),
    (dilemma_values.defence, dilemma_values.defence)
)
percentage = 0.95
count_of_loops = 0

while population.count(what_we_need) / N < percentage:
    count_of_loops += 1
    childs = []
    for individual in population:
        pair = population[randint(0, len(population) - 1)]
        childs += mix(individual, pair)

    population += childs
    population = selection(population, N)
