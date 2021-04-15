from genetic_algorithm import Genetic
import time
import random


class GeneticControl:

    def __init__(self):
        self.population_size = random.randint(30, 200)  # 84
        self.elite_amount = int(self.population_size / random.randint(1, 25))  # 7
        self.mutation_chance = random.randint(2, 40)  # 8
        self.max_time = random.uniform(3, 10)  # 5
        self.start = time.time()
        self.end = time.time()

        print(
            f"\npopulation size: {self.population_size}, elite amount: {self.elite_amount}, mutation chance: {self.mutation_chance}, max time: {self.max_time}")

    def new_generation(self):
        self.gen = Genetic(self.population_size)
        self.start_test = time.time()
        self.end_test = time.time()

    def control_until_max_time(self):
        while (self.end_test - self.start_test) < self.max_time:
            self.gen.check_fitness(self.gen.population)
            self.gen.cal_prob()
            while len(self.gen.new_children) < self.population_size:
                self.gen.splice(self.mutation_chance)
            self.gen.new_generation(self.elite_amount)
            self.gen.loops += 1
            if self.gen.loops % 100 == 0 or self.gen.loops == 1:
                print(
                    f"Top fitness: {self.gen.top_gene[0]}, for chromosome: {self.gen.top_gene[1]}, loops: {self.gen.loops}")
            self.end_test = time.time()
            if self.gen.top_gene[0] == 28:
                break

    def evaluate(self):
        print(f"\nGeneration end: Found final state = {self.gen.found}")
        print(f"Time taken: {self.end - self.start}")
        print(
            f"population size: {self.population_size}, elite amount: {self.elite_amount}, mutation chance: {self.mutation_chance}, max time: {self.max_time}\n")

    def record(self, taken, maxi, pop, el, mu):
        taken.append(self.end - self.start)
        maxi.append(self.max_time)
        pop.append(self.population_size)
        el.append(self.elite_amount)
        mu.append(self.mutation_chance)

    def write_record(self, taken, maxi, pop, el, mu):
        with open('genetic_data_taken.txt', 'w') as file_object:
            for item in taken:
                file_object.write("\n" + str(item))

        with open('genetic_data_max_time.txt', 'w') as file_object:
            for item in maxi:
                file_object.write("\n" + str(item))

        with open('genetic_data_pop.txt', 'w') as file_object:
            for item in pop:
                file_object.write("\n" + str(item))

        with open('genetic_data_elite.txt', 'w') as file_object:
            for item in el:
                file_object.write("\n" + str(item))

        with open('genetic_data_mutation.txt', 'w') as file_object:
            for item in mu:
                file_object.write("\n" + str(item))


data_time_taken = []
data_max_time = []
data_pop = []
data_elite = []
data_mutation = []

# Control parameters 1
gc = GeneticControl()

loop = 0
# Population 1
while loop < 1000:
    gc.new_generation()
    # While the control parameters 1 don't return true, run loop. Loop restarts at each max_time period. After restart, a new generation is used.
    gc.control_until_max_time()
    gc.end = time.time()
    gc.evaluate()
    if gc.gen.found:
        gc.record(data_time_taken, data_max_time, data_pop, data_elite, data_mutation)
        gc = GeneticControl()
        print("New control")
    loop += 1
    print(loop)
    # New generation after each restart, using same control parameters

gc.write_record(data_time_taken, data_max_time, data_pop, data_elite, data_mutation)

