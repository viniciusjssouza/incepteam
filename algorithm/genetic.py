
class Genetic:

    DEFAULT_N_ITERATIONS = 1000
    DEDAULT_GENERATION_SIZE = 50
    DEDAULT_ELITE_SIZE = 8

    def __init__(self, problem_input, extra_settings=None):
        self.people = problem_input.people
        self.teams = problem_input.teams
        self.n_iterations = extra_settings.n_iterations or DEFAULT_N_ITERATIONS
        self.generation_size = extra_settings.generation_size or DEDAULT_GENERATION_SIZE
        self.elite_size = extra_settings.elite_size or DEDAULT_ELITE_SIZE

    def search(self):
        # init_population
        # evaluate population
        for generation in range(0, self.n_iterations):
            # select best to keep in new gen
            for couple in range(0, (self.generation_size - self.elite_size)//2):
                # select couple based on fitness
                # create children through crossover
                # mutation?
                # evaluate
