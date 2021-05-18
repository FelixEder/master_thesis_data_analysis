import pandas as pd
import matplotlib.pyplot as plt

base_route = '~/Documents/Google Drive/KTH/Exjobb/Implementation/Results/'

iavControls = pd.read_csv(base_route + 'Monolith/Scenario 1/2021_05_12-13/csv/C/iavControlPerPerson.csv')

print("Number of Iav creations: " + str(iavControls["time (ms)"].count()))
print("Max time (ms): " + str(iavControls["time (ms)"].max()))
print("Min time (ms): " + str(iavControls["time (ms)"].min()))
print("Sum time (ms): " + str(iavControls["time (ms)"].sum()))
print("Mean time (ms): " + str(iavControls["time (ms)"].mean()))
print("Median time (ms): " + str(iavControls["time (ms)"].median()))

plt.plot(iavControls["time (ms)"])
plt.ylim(bottom=0)
plt.title('Monolithic solution: IAV creation process')
plt.ylabel('Time (ms)')
plt.xlabel('People')
plt.show()