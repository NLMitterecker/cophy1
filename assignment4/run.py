from classes.FTCS import FTCS
from classes.FTCSConfig import FTCSConfig

ftcs_config = FTCSConfig(0.0001, 61, 1, 1, 1, 300, 6, 51)
ftcs = FTCS(ftcs_config)
ftcs.calculate()
ftcs.draw_plot()






