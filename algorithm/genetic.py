from algorithm import RandomAllocation
from model import Allocations
from copy import copy
import itertools
import random
import heapq
import pdb

class Genetic:

    DEFAULT_N_ITERATIONS = 300
    DEDAULT_GENERATION_SIZE = 50
    DEDAULT_ELITE_SIZE = 8
    DEFAULT_MUTATION_ODDS = 0.1

    def __init__(self, problem_input, extra_settings=None):
        extra_settings = extra_settings or {}
        self.people = problem_input.people
        self.teams = problem_input.teams
        self.problem_input = problem_input
        self.n_iterations = extra_settings.get("n_iterations", Genetic.DEFAULT_N_ITERATIONS)
        self.generation_size = extra_settings.get("generation_size", Genetic.DEDAULT_GENERATION_SIZE)
        self.elite_size = extra_settings.get("elite_size", Genetic.DEDAULT_ELITE_SIZE)
        self.mutation_odds = extra_settings.get("mutation_odds", Genetic.DEFAULT_MUTATION_ODDS)

    def search(self):
        # init_population
        population = self.generate_initial_population()
        # evaluate population (already done inside??)
        for generation_index in range(self.n_iterations):
            # select best to keep in new gen
            new_population = self.select_elite(population)
            for couple_index in range((self.generation_size - self.elite_size)//2):
                # select couple based on fitness
                parent_a, parent_b = self.select_proportionate(population)
                child_a, child_b = self.generate_children(parent_a, parent_b)
                if random.random() < self.mutation_odds:
                    child_a = self.mutate(child_a)
                new_population += [child_a, child_b]
            population = new_population
        return max(population, key=self.fitness)

    def generate_initial_population(self):
        population = []
        allocator = RandomAllocation(self.people, self.teams)
        for member_index in range(self.generation_size):
            population.append(Allocations(self.problem_input, allocator.generate()))
        return population

    def select_elite(self, population):
        return heapq.nlargest(self.elite_size, population, key=self.fitness)

    def select_proportionate(self, population):
        # TODO change below code to O(log n)
        fitnesses = [self.fitness(p) for p in population]
        rand_range = sum(fitnesses)
        pick_a = random.uniform(0, rand_range)
        pick_b = random.uniform(0, rand_range)
        current_sum = fitnesses[0]
        index_a = 0
        index_b = 0
        index = 0
        while current_sum < pick_a or current_sum < pick_b:
            if current_sum < pick_a:
                index_a += 1
            if current_sum < pick_b:
                index_b += 1
            index += 1
            current_sum += fitnesses[index]
        return population[index_a], population[index_b]

    def fitness(self, allocation):
        return 0.01 + 1.0/allocation.cost()

    def generate_children(self, parent_a, parent_b):
        new_a = copy(parent_a)
        new_b = copy(parent_b)
        # cross over a and b
        trade_person = random.sample(self.people, 1)[0]
        first_team_a = new_a.people_to_team_map[trade_person]
        presence_a = [(trade_person, first_team_a)]
        current_team_b = new_b.people_to_team_map[trade_person]
        presence_b = [(trade_person, current_team_b)]
        trade_people = {trade_person}
        while current_team_b != first_team_a:
          possible_trade_people = list(new_a.team_name_to_allocation[current_team_b].members - trade_people)
          trade_person = random.sample(possible_trade_people,1)[0]
          presence_a.append((trade_person, current_team_b))
          current_team_b = new_b.people_to_team_map[trade_person]
          presence_b.append((trade_person, current_team_b))
          trade_people.add(trade_person)
        # should exchange trade people between teams
        self.remove_members(new_a, presence_a)
        self.add_members(new_a, presence_b)
        self.remove_members(new_b, presence_b)
        self.add_members(new_b, presence_a)
        new_a.calculate_cost()
        new_b.calculate_cost()
        return new_a, new_b

    def mutate(self, allocation):
        new_allocation = copy(allocation)
        for _ in range(random.randint(1,12)):
            # calculate random people to swap
            team1, team2 = random.sample(new_allocation.team_allocations, 2)
            person1 = random.sample(team1.members, 1)[0]
            person2 = random.sample(team2.members, 1)[0]
            self.swap_people(new_allocation, team1, person1, team2, person2)
            new_allocation.calculate_cost()
        return new_allocation

    def swap_people(self, team_allocations, team1, person1, team2, person2):
        team1.members.remove(person1)
        team2.members.remove(person2)
        team1.members.add(person2)
        team2.members.add(person1)

    def remove_members(self, allocation, presence):
        for member, team_name in presence:
            allocation.team_name_to_allocation[team_name].members.remove(member)

    def add_members(self, allocation, presence):
        for member, team_name in presence:
            allocation.team_name_to_allocation[team_name].members.add(member)
