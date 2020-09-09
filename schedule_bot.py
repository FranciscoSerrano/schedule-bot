# Import Dependancies
import pandas as pd
import os
import plotly.express as px
import plotly

# Load in the data
file_to_load = os.path.join("All Shifts-Table 1.csv")
raw_schedule = pd.read_csv(file_to_load)
raw_schedule_df = pd.DataFrame(raw_schedule)

# Drop the coloumns that arent needed.
raw_schedule_df = raw_schedule_df[["Team Manager", "Name", "Local SHIFT_DATE", "Local Full SHIFT_START_TIME", "Local Full SHIFT_END_TIME"]]

# Adds two new columns 'Start_Shift' and 'End Shift'
# This creates a start and end of a shift as a datetime object for charting.  
raw_schedule_df['Start_Shift'] = pd.to_datetime(raw_schedule_df['Local SHIFT_DATE'] + ' ' + raw_schedule_df['Local Full SHIFT_START_TIME'])
raw_schedule_df['End_Shift'] = pd.to_datetime(raw_schedule_df['Local SHIFT_DATE'] + ' ' + raw_schedule_df['Local Full SHIFT_END_TIME'])

# Asks Team Manager for input to get their name as it appears in the CSV file
print("\nHey there, I'm a bot that can generate an interactive schedule chart for you!\n")
manager_name = input("Please enter your name exactly as it appears in the Spreadsheet: ")

# Creates a new data frame with only the team members from a specific manager.
manager_team_df = raw_schedule_df.loc[raw_schedule_df['Team Manager'] == manager_name]
manager_team_df.reset_index()

# Creates the schecule chart using the Manager Team dataframe
schedule = px.timeline(manager_team_df, x_start="Start_Shift", x_end="End_Shift", y="Name", title = "Team Schedule")
schedule.update_yaxes(autorange="reversed") # otherwise inverse order
schedule.update_layout(
            title_font_size = 42,
            font_size = 18
            )


#Save Schedule as HTML for interactive Chart
plotly.offline.plot(schedule, filename='team_schedule.html')