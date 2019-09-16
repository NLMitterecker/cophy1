from .AbstractWaveSimulationConfig import AbstractWaveSimulationConfig

class WaveSimulationConfig(AbstractWaveSimulationConfig):

    # TODO what is c, k??
    # TODO Refactor *args, **kwargs?
    def __init__(self, string_size, step_size, segment_length, initial_position, c, k):

        self.string_size = string_size
        self.step_size = step_size
        self.segment_length = segment_length
        self.initial_position = initial_position
        self.c = c
        self.k = k

    def string_size(self):
        return self.string_size

    def step_size(self):
        return self.step_size

    def segment_length(self):
        return self.segment_length

    def initial_position(self):
        return self.initial_position

    # TODO c?
    def c(self):
        return self.c

    # TODO k?
    def k(self):
        return self.k