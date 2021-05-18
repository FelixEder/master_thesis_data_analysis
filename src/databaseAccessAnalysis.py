import pandas as pd
import matplotlib.pyplot as plt

base_route = '~/Documents/Google Drive/KTH/Exjobb/Implementation/Results/'

database = pd.read_csv(base_route + 'EDA/Scenario 3/2021_05_12/csv/B/database.csv')


write_df = database.query("type == 'WRITE'")
read_df = database.query("type == 'READ'")

#write_df = write_df.astype({"time (ms)": int})

print("Summary of database writes")
print("Number of writes:" + str(write_df["type"].count()))
#print("Max time: " + str(write_df["time (ms)"].max()))
#print("Min time: " + str(write_df["time (ms)"].min()))
#print("Sum time: " + str(write_df["time (ms)"].sum()))
#print("Mean time: " + str(write_df["time (ms)"].mean()))
#print("Median time: " + str(write_df["time (ms)"].median()))


print("Summary of database reads")
print("Number of reads: " + str(read_df["type"].count()))