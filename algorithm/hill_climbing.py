from random_allocation import RandomAllocation


class HillClimbing:
    DEFAULT_N_ITERATIONS = 10000

    def __init__(self, problem_input, n_iterations=DEFAULT_N_ITERATIONS):
        self.people = problem_input.people
        self.teams = problem_input.teams
        self.n_iterations = n_iterations
        self.solution = None

    def search(self):
        self.solution = None
        for it in range(0, HillClimbing.DEFAULT_N_ITERATIONS):
            allocations = self.generate_initial_allocation()
            while True:
                new_allocations = self.improve_allocation(allocations)
                if new_allocations is None:
                    self.update_best_solution(allocations)
                    break
                else:
                    allocation = new_allocations
        return self.solution

    def improve_allocation(self, allocation):


    def generate_initial_allocation(self):
        return RandomAllocation(self.people, self.teams).generate()

    def update_best_solution(self, allocations):
        if self.solution is None or self.calc_cost(self.solution) > self.calc_cost(allocations):
            self.solution = allocations

    def calc_cost(self, allocations):


