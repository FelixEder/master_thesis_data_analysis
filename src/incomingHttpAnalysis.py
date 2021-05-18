import pandas as pd
import matplotlib.pyplot as plt

base_route = '~/Documents/Google Drive/KTH/Exjobb/Implementation/Results/'

dataframe = pd.read_csv(base_route + 'EDA/Scenario 3/2021_05_12/csv/B/incomingHttp.csv')

get_df = dataframe.query("type == 'GET'")
post_df = dataframe.query("type == 'POST'")

get_df = get_df.astype({"size (bits)": int})
post_df = post_df.astype({"size (bits)": int})

print("Summary of incoming get requests")
print("Number of get requests: " + str(get_df["size (bits)"].count()))
print("Size of get requests: " + str(get_df["size (bits)"].sum()))
print("")

print("Summary of incoming post requests")
print("Number of post requests: " + str(post_df["size (bits)"].count()))
print("Size of post requests: " + str(post_df["size (bits)"].sum()))