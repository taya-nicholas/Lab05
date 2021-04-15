from genetic_algorithm import Genetic
import time
import random
meta_loop = 0
meta_t1 = time.time()
data = []
data_x = []
data_y = []
data_pop = []
data_elite = []
data_mutation = []

while meta_loop < 100:
    start = time.time()

    population_size = random.randint(30, 200)  # 84
    elite_amount = int(population_size/random.randint(1, 25))  # 7
    mutation_chance = random.randint(2, 40)  # 8
    max_time = random.uniform(3, 60)  # 5

    print(f"\npopulation size: {population_size}, elite amount: {elite_amount}, mutation chance: {mutation_chance}")

    gen = Genetic(population_size)

    while gen.top_gene[0] < 28:
        gen.check_fitness(gen.population)
        gen.cal_prob()
        while len(gen.new_children) < population_size:
            gen.splice(mutation_chance)
        gen.summary()
        gen.new_generation(elite_amount)
        gen.loops += 1
        if gen.loops % 100 == 0 or gen.loops == 1:
            print(f"Top fitness: {gen.top_gene[0]}, for chromosome: {gen.top_gene[1]}, loops: {gen.loops}")
        test_time = time.time()
        if (test_time - start) > max_time:
            break

    end = time.time()
    print(f"Found status: {gen.found} Population size: {population_size}, elite amount: {elite_amount}, mutation chance: {mutation_chance}")
    print(f"Top fitness: {gen.top_gene[0]}, for chromosome: {gen.top_gene[1]}")
    print(f"Finished after {gen.loops} number of loops")
    print(f"Time taken: {end - start}")
    meta_loop += 1
    if gen.found:
        meta_t2 = time.time()
        print(f"total time: {meta_t2 - meta_t1}")
        data.append(f"Found with parameters: {population_size}, {elite_amount}, {mutation_chance}, with max {max_time} per cycle,  total time: {meta_t2 - meta_t1}\n")
        data_x.append(meta_t2 - meta_t1)
        data_y.append(f"{max_time}")
        data_pop.append(f"{population_size}")
        data_elite.append(f"{elite_amount}")
        data_mutation.append(f"{mutation_chance}")
        meta_t1 = time.time()
        gen.show_board()
        #break

print(data)
with open('genetic_data.txt', 'w') as file_object:
    file_object.write('\n'.join(data))

with open('genetic_data_x.txt', 'w') as file_object:
    for item in data_x:
        file_object.write("\n" + str(item))

with open('genetic_data_y.txt', 'w') as file_object:
    for item in data_y:
        file_object.write("\n" + str(item))

with open('genetic_data_pop.txt', 'w') as file_object:
    for item in data_pop:
        file_object.write("\n" + str(item))

with open('genetic_data_elite.txt', 'w') as file_object:
    for item in data_elite:
        file_object.write("\n" + str(item))

with open('genetic_data_mutation.txt', 'w') as file_object:
    for item in data_mutation:
        file_object.write("\n" + str(item))
