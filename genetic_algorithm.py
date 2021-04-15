import random
import numpy as np
import time
from chess_board import chess_board


class Genetic:

    def __init__(self, population_size):
        """Initiates population_size number of chromosomes randomly"""
        self.population = []  # the current list of chromosomes
        self.fitness = []  # a list of the fitness evaluations of each chromosome
        self.sorted_f = []  # a list of the indices of the population, sorted from most to least fit
        self.weighted_list = []  # a list of the weights used for roulette selection
        self.new_children = []  # a list of the children genes

        self.best_index = 0
        self.loops = 0
        self.top_gene = [0]
        self.top_gene.append([])
        self.found = False

        for _ in range(population_size):
            c = random.sample(range(63), 8)
            self.population.append(c)

    def check_fitness(self, pop_test):
        for chromosome in pop_test:
            self.fitness.append(board.nonattacking_pairs(chromosome))
        self.fit_index()

    def fit_index(self):
        self.best_index = np.argmax(self.fitness)
        if self.fitness[self.best_index] > self.top_gene[0]:
            self.top_gene[0] = self.fitness[self.best_index]
            self.top_gene[1] = self.population[self.best_index]
        self.sorted_f = np.argsort(self.fitness)
        self.sorted_f = self.sorted_f[::-1]
        if self.top_gene[0] == 28:
            self.found = True
        #self.check_end()

    def show_board(self):
        while False:
            board.show_state(self.top_gene[1])

    def check_end(self):
        if self.fitness[self.best_index] == 28:
            t2 = time.time()
            print("Winning solution:")
            print(f"Top fitness: {self.top_gene[0]}, for chromosome: {self.top_gene[1]}")
            print(f"Found after {self.loops} number of loops")
            print(f"Total time taken: {t2 - t1}")
            while True:
                board.show_state(self.population[self.best_index])

    def cal_prob(self):
        total_fitness_points = sum(self.fitness)
        # populate weighted probability list for roulette_selection
        for fit in self.fitness:
            self.weighted_list.append(fit / total_fitness_points)

    def roulette_selection(self):
        return random.choices(self.population, self.weighted_list)[0]

    def mutation(self, child):
        i = random.randint(0, 7)
        child[i] = random.randint(0, 63)
        return child

    def splice(self, mutation_chance):
        parent1 = self.roulette_selection()
        parent2 = self.roulette_selection()
        while parent1 == parent2:
            parent2 = self.roulette_selection()

        c1 = []
        cut_point = random.randint(0, 7)
        rand_num = random.choice([1, 2])
        if rand_num == 1:
            first = parent1
            second = parent2
        else:
            first = parent2
            second = parent1

        for i in range(8):
            if i < cut_point:
                c1.append(first[i])
            else:
                c1.append(second[i])

        if random.randint(0, mutation_chance) == 0:
            c1 = self.mutation(c1)

        if len(set(c1)) == 8:
            self.new_children.append(c1)

    def new_generation(self, elite_amount):
        elites = []
        for i in range(elite_amount):
            elites.append(self.population[self.sorted_f[i]])
        self.population = self.new_children
        for elite_pop in elites:
            self.population.append(elite_pop)

        self.fitness = []
        self.sorted_f = []
        self.new_children = []
        self.weighted_list = []
        self.best_index = 0

    def summary(self):
        pass
        # print(f"Max fitness: {self.fitness[self.best_index]}, from: {self.population[self.best_index]}, at: {self.best_index}")


t1 = time.time()
board = chess_board()
