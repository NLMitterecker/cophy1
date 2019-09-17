from classes.WaveSimulation import WaveSimulation
from classes.WaveSimulationConfig import WaveSimulationConfig



sim_conf = WaveSimulationConfig(1000, 0.3, 0.1, 1, 4, 1000)
sim = WaveSimulation(sim_conf)
sim.draw()

