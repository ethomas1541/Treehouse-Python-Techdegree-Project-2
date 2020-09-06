"""
Treehouse Python Techdegree
Project 2 - Basketball Stats Tool
Elijah Thomas
9/6/2020
"""

from constants import *
from random import choice                                           #Random module is only used for choosing players to sort into teams.
from math import ceil                                               #Math module is only used to tidy up the average height readout, as it makes a lot of ugly .666666666 representations of two-thirds and such.

cleaned_data = []

sorted_teams = {
    "Panthers": [],
    "Bandits": [],
    "Warriors": []
}

def clean_data():
    for player in PLAYERS:
        new_dict = {}                                               # New dictionary where clean data will be stored.
        for item in player:
            if item == "name":                                      # Add name to the dictionary as-is.
                new_dict.update(name = player[item])
            elif item == "guardians":
                guardians_list = player[item].split(" and ")        # Convert guardians string into list of 1 or 2 strings, then add it to the dictionary.
                new_dict.update(guardians = guardians_list)
            elif item == "experience":
                if player[item] == "NO":                            # Convert "YES"/"NO" into boolean and add it to the dictionary.
                    new_dict.update(experience = False)
                else:
                    new_dict.update(experience = True)
            else:                                                   # Convert first two characters of height string to a 2-digit integer and add it to the dictionary.
                new_dict.update(height = int(player[item][:2]))
        cleaned_data.append(new_dict)                               # Add the player's dictionary to the list of cleaned data.

def sort_teams():
    experienced = []                                                # Lists used to seperate players based on experience. These will equal each other because there are 9 experienced and 9 inexperienced players, which is convenient.
    inexperienced = []
    for player in cleaned_data:                                     # Loop to seperate players based on experience using aforementioned lists.
        if player["experience"]:
            experienced.append(player)
        else:
            inexperienced.append(player)
    for team in sorted_teams:                                       # This loop is a bit complicated. For each team, it adds 3 experienced and 3 inexperienced players. Each name is taken off the list when added to a team to avoid "cloning".
        selected_team = sorted_teams[team]
        for x in range(3):
            experienced_player = choice(experienced)
            inexperienced_player = choice(inexperienced)
            selected_team.append(experienced_player)
            selected_team.append(inexperienced_player)
            experienced.remove(experienced_player)
            inexperienced.remove(inexperienced_player)

def handled_input(upper_bound : int):                               # Simple function for filtering user input, pretty self-explanatory.
    while True:
        try:
            response = int(input("\nEnter an option > "))
            if response < 1 or response > upper_bound:
                raise ValueError
            else:
                return response
        except:
            print(f"\nPlease type a whole number between 1 and {upper_bound}.")
        

if __name__ == "__main__":                                                                                                  #Dunder main block containing actual app behavior. clean_data and sort_teams are outside the loop because I don't imagine the data needing to change if the user decides to restart the program.
    clean_data()
    sort_teams()

    while True:
        print(f"BASKETBALL TEAM STATS TOOL\n\n{'-' * 10} MENU {'-' * 10}\n\nOptions:\n\n 1. Display Team Stats\n 2. Quit")

              
        if handled_input(2) == 1:                                                                                           #User decides to quit or use/reuse the tool. Teams are not re-sorted after reusing the program, and cleaned_data is not altered.
            pass
        else:
            quit()

        print("\nWhich team? Options:\n\n 1. Panthers\n 2. Bandits \n 3. Warriors")                                         #User selects team whose stats they want to view.

        selected_team = handled_input(3)

        if selected_team == 1:
            selected_team = "Panthers"
        elif selected_team == 2:
            selected_team = "Bandits"
        else:
            selected_team = "Warriors"

        team_player_names = []                                                                                              #Empty values, each of which must be filled to give a full statistical readout of the team.

        experienced_count = 0

        inexperienced_count = 0

        cumulative_height = 0

        avg_height = 0

        team_guardians = []
        
        for player in sorted_teams[selected_team]:                                                                          #Loop that sorts all needed data into the empty values and prepares them for printing.
            for item in player:
                if item == "name":
                    team_player_names.append(player[item])
                elif item == "experience":
                    if player[item]:
                        experienced_count += 1
                    else:
                        inexperienced_count += 1
                elif item == "height":
                    cumulative_height += player[item]
                else:
                    for guardian in player[item]:
                        team_guardians.append(guardian)

        avg_height = ceil(cumulative_height / len(team_player_names))

        #I HATE using these many print statements, but after typing a ridiculous 327-character long one-liner, I decided to change my style.

        print(f"\nTeam: {selected_team} stats\n--------------------\n")
        print(f"Players on team: {len(team_player_names)}\n")
        print(f"Players:\n\n\t{', '.join(team_player_names)}\n")
        print(f"Experienced Players: {experienced_count}\n")
        print(f"Inexperienced Players: {inexperienced_count}\n")
        print(f"Average Height: {avg_height} inches\n")
        print(f"Guardians of Players:\n\n\t{', '.join(team_guardians)}\n")
        print("-" * 26 + "\n")

# I'm going for the "exceeds expectations" bar on this project.
