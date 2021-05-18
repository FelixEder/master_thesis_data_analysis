import pandas as pd
import matplotlib.pyplot as plt

base_route = '~/Documents/Google Drive/KTH/Exjobb/Implementation/Results/'

dataframe = pd.read_csv(base_route + 'EDA/Scenario 3/2021_05_12/csv/D/outgoingHttp.csv')

get_df = dataframe.query("type == 'GET'")
post_df = dataframe.query("type == 'POST'")

get_df = get_df.astype({"size (bits)": int, "time (ms)": int})
post_df = post_df.astype({"size (bits)": int, "time (ms)": int})

print("Summary of outgoing get requests")
print("Number of get requests: " + str(get_df["size (bits)"].count()))
print("Size of get requests: " + str(get_df["size (bits)"].sum()))
print("Total get latency: " + str(get_df["time (ms)"].sum()))
print("")

print("Summary of outgoing post requests")
print("Number of post requests: " + str(post_df["size (bits)"].count()))
print("Size of post requests: " + str(post_df["size (bits)"].sum()))
print("Total post latency: " + str(post_df["time (ms)"].sum()))
