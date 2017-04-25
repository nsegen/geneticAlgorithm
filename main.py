from dilemma_values import DilemmaValues

from random import randint


def finish(examples, result):

    n = 0
    for s in examples:
        if s[1] is result:
            n += 1
    return (len(examples) - n) <= 1


def mix(individual1, individual2):

	individual1 = [individual1[0][0], individual1[0][1], individual1[1]]
	individual2 = [individual2[0][0], individual2[0][1], individual2[1]]


N = 20
dilemma_values = DilemmaValues(c=1, d=2, C=3, D=4)
population = []
for i in range(N):
    population.append((dilemma_values.compare(
        dilemma_values.get_random_value(),
        dilemma_values.get_random_value()),
        dilemma_values.get_random_value())
    )

while not (finish(population, dilemma_values.cooperation) or finish(population, dilemma_values.defence)):
	a = population[randint(0, N)]
	b = population[randint(0, N)]
