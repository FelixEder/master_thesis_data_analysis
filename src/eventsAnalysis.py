import pandas as pd
import matplotlib.pyplot as plt

base_route = '~/Documents/Google Drive/KTH/Exjobb/Implementation/Results/'

eventsDf = pd.read_csv(base_route + 'EDA/Scenario 3/2021_05_12/csv/E/events.csv')

print("Number of events emitted: " + str(eventsDf["description"].count()))