# Note that the queries were based on the codecademy platform on the website.
# The results were different if worked using on my PC because the database did 
# not contain many errors while the codecademy website version did.

# In this part of the project, I took my findings from the SQL queries and 
# visualize them using Python and Matplotlib, in the forms of:
  # 1) Bar Graph: Features Games
  # 2) Pie Chart: Stream Viewers' Locations
  # 3) Line Graph: Time Series Analysis


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "WoT", 
"Hearth", "Agar.io"]

viewers =  [193533, 85608, 54438, 38004, 35310, 29467, 28115, 15932, 14399, 
11480]

# Plotting
ax = plt.subplot()
plt.bar(range(len(games)), viewers, color="slateblue")
plt.title("Featured Games Viewers")
plt.legend(["Twitch"])
plt.xlabel("Games")
plt.ylabel("Viewers")

# Setting ticks and tick labels
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation=30)

plt.show()

# This is used to clear the current figure, our bar graph, before creating our 
# next figure, the pie chart.
plt.clf() 


# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "CA", "DE", "N/A", "GB", "TR", "AU", "SE", "NL", "DK", "GR", 
"Others"]

countries = [85606, 13034, 10835, 7641, 6964, 4412, 3911, 3533, 3213, 2909, 
2885, 48590]

# For the chart, codecademy suggested using the following colors:
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 
'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

# This will separate the US from the pie. The 0.1 specifies the fraction of the 
# radius.
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) 

# Plotting
plt.pie(countries, explode=explode, colors=colors, shadow=True, startangle=345, 
    autopct='%1.0f%%', pctdistance=1.15)
plt.title("League of Legends Viewers' Whereabouts")

# The bbox_to_anchor argument will help us move the Legend box to a place for 
# easier view.
plt.legend(labels, loc="right", bbox_to_anchor=(1.3, 0.5)) 

plt.show()

plt.clf()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [7025, 4693, 5961, 4236, 3567, 1597, 236, 338, 935, 1214, 1940, 
7349, 11766, 9740, 7521, 9065, 10134, 11929, 12215, 15206, 19656, 18425, 13984, 
11646]

# Plotting
ax = plt.subplot()
plt.plot(hour, viewers_hour, marker='o')
plt.title("Time Series")
plt.legend(["2015-01-01"], loc='lower right', bbox_to_anchor=(1.0, 0.025))
plt.xlabel("Hour")
plt.ylabel("Viewers")

# Setting the tick marks and background color
ax.set_xticks(hour)
ax.set_facecolor('lightgray')

# Lets account for a 15% error in the viewers_hour data.
y_upper = [i * 1.15 for i in viewers_hour] # Sets the top of the shaded error
y_lower = [i * 0.85 for i in viewers_hour] # Sets the bottom of the shaded area

plt.fill_between(hour, y_lower, y_upper, alpha=0.2) # this is the shaded error

plt.show()



