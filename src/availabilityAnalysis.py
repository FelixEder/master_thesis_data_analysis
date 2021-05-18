import pandas as pd
import matplotlib.pyplot as plt

base_route = '~/Documents/Google Drive/KTH/Exjobb/Implementation/Results/'

availabilityDf = pd.read_csv(base_route + 'EDA/Scenario 3/2021_05_12/csv/D/requestFailedLogger.csv')

print("Number of times system was down: " + str(availabilityDf["time (ms)"].count()))
print("Total time that system was unavailable: " + str(availabilityDf["time (ms)"].sum()))