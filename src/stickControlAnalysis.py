import pandas as pd
import matplotlib.pyplot as plt

base_route = '~/Documents/Google Drive/KTH/Exjobb/Implementation/Results/'

stickControls = pd.read_csv(base_route + 'Monolith/Scenario 3/2021-05-09/csv/iavSystem/stickControlPerson1.csv')

print("Number of stick controls: " + str(stickControls["time (ms)"].count()))
print("Max time (ms): " + str(stickControls["time (ms)"].max()))
print("Min time (ms): " + str(stickControls["time (ms)"].min()))
print("Sum time (ms): " + str(stickControls["time (ms)"].sum()))
print("Mean time (ms): " + str(stickControls["time (ms)"].mean()))
print("Median time (ms): " + str(stickControls["time (ms)"].median()))

plt.plot(stickControls["time (ms)"])
plt.ylim(bottom=0)
plt.title('Monolithic solution: Stick control process')
plt.ylabel('Time (ms)')
plt.xlabel('Controls')
plt.show()