from random import randint, random, uniform, choice


class Individual:
    x1 = 0
    x2 = 0

    def __init__(self, x1, x2):
        self._x1 = x1
        self._x2 = x2

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, value):
        if -3 <= value <= 3:
            self._x1 = value
        else:
            raise ValueError("x1 might be between -3 and 3")

    @property
    def x2(self):
        return self._x2

    @x2.setter
    def x2(self, value):
        if -2 <= value <= 2:
            self._x2 = value
        else:
            raise ValueError("x1 might be between -2 and 2")


def fitness(individual):
    x1 = individual.x1
    x2 = individual.x2
    return (4 - 2.1 * pow(x1, 2) + pow(x1, 4) / 3) * pow(x1, 2) + x1 * x2 + (-4 + 4 * pow(x2, 2)) * pow(x2, 2)


def recombination(i1, i2):
    if i1 == i2:
        raise ValueError("First individual and second individual are equals")
    d = 0.25
    offspring = Individual(0, 0)
    try:
        alpha = uniform(-d, 1 + d)
        offspring.x1 = i1.x1 + alpha * (i2.x1 - i1.x1)
        alpha = uniform(-d, 1 + d)
        offspring.x2 = i1.x2 + alpha * (i2.x2 - i1.x2)
    except ValueError:
        offspring = recombination(i1, i2)
    return offspring


def mutation(ind, m):
    probability = 1/m
    sign1 = choice([-1, 1])
    alpha1 = 0.5 * 6
    delta1 = 0
    for i in range(1, m+1):
        delta1 += (1 if random() < probability else 0) * pow(2, -i)
    sign2 = choice([-1, 1])
    alpha2 = 0.5 * 6
    delta2 = 0
    for i in range(1, m + 1):
        delta2 += (1 if random() < probability else 0) * pow(2, -i)

    mutationInd = Individual(0, 0)

    try:
        mutationInd.x1 = ind.x1 + sign1 * alpha1 * delta1
        mutationInd.x2 = ind.x2 + sign2 * alpha2 * delta2
    except ValueError:
        mutationInd = mutation(ind, m)

    return mutationInd


def selection(population, n):

    population.sort(key=fitness)

    red = []

    return [population[i] for i in range(n)]


def check_population(population):

    eps = 0.00001
    for i in population:
        for j in population:
            if abs(fitness(i) - fitness(j)) > eps:
                return False
    return True


def genetic_algorithm(population, n):
    offsprings = []

    for ind in population:
        ind_two = population[randint(0, n - 1)]
        try:
            offsprings.append(mutation(recombination(ind, ind_two), n))
        except ValueError:
            print("individual " + "(" + str(ind.x1) + ", " + str(ind.x2) + ")" + " are ignored")

    population.extend(offsprings)
    population = selection(population, n)

    if check_population(population):
        return population[0]
    else:
        return genetic_algorithm(population, n)


n = 20
population = []

for i in range(n):
    x1 = uniform(-3, 3)
    x2 = uniform(-2, 2)
    population.append(Individual(x1, x2))

result = genetic_algorithm(population, n)

print("f(" + str(result.x1) + ", " + str(result.x2) + ") = " + str(fitness(result)))
