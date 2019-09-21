#!/usr/bin/env python3

from classes.WaveSimulation import WaveSimulation
from classes.WaveSimulationConfig import WaveSimulationConfig

simulation_config = WaveSimulationConfig(1000, 1000, 0.25, 1)
wave_simulation = WaveSimulation(simulation_config)
wave_simulation.simulate(10000)
wave_simulation.animate()

if not __name__ == "__main__":
    pass





