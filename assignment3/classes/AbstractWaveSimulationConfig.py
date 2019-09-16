from abc import ABC, abstractmethod

class AbstractWaveSimulationConfig(ABC):

    @abstractmethod
    def string_size(self):
        pass

    @abstractmethod
    def step_size(self):
        pass

    @abstractmethod
    def segment_length(self):
        pass

    @abstractmethod
    def initial_position(self):
        pass

    # TODO c?
    @abstractmethod
    def c(self):
        pass

    # TODO k?
    @abstractmethod
    def k(self):
        pass
