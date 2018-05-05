from random_allocation import RandomAllocation

class HillClimbing:

    DEFAULT_N_ITERATIONS = 10000

    def __init__(self, problem_input, n_iterations=DEFAULT_N_ITERATIONS):
        self.people = problem_input.people
        self.teams = problem_input.teams
        self.n_iterations = n_iterations


    def search(self):
        allocation = self.generate_initial_allocation()


    def generate_initial_allocation(self):
        RandomAllocation(self.people, self.teams).generate()




