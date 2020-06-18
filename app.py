import constants
import copy
import random

if __name__ == '__main__':

    teams = copy.deepcopy(constants.TEAMS)
    players = copy.deepcopy(constants.PLAYERS)
    experienced = []
    unexpierenced = []
    panthers = []
    warriors = []
    bandits = []
    panthers_names =[]
    warriors_names = []
    bandits_names = []
    num_players_team = len(players) / len(teams)

    def clean_data():
        for player in players:
            player['height'] = int(player['height'][:2])
            if player['experience'] == 'YES':
                player['experience'] = True
                experienced.append(player)
            else:
                player['experience'] = False
                unexpierenced.append(player)
    clean_data()

    def balance_teams(team):
        while len(experienced) != 0 and len(team) < 3:
            team.append(experienced.pop(random.randrange(len(experienced))))
            while len(unexpierenced) != 0 and len(team) < 6:
                team.append(unexpierenced.pop(random.randrange(len(unexpierenced))))

    balance_teams(panthers)
    balance_teams(warriors)
    balance_teams(bandits)

    def start_basketball_stats():

        print("\nWELCOME TO BASEBALL TEAM STATS TOOL\n\n------MENU ITEMS------\n")
        while True:
            try:
                selection = int(input("Your choises:\n1. Display Team Stats\n2. Quit\n\nMake your selection > "))
                if selection == 1:
                    for index, item in enumerate(teams, 1):
                        print(f'{index}. {item}')

                    select_team = int(input("\nSelect team > "))
                    if select_team == 1:
                        team_name = "Panthers"
                        for player in panthers:
                            panthers_names.append(player['name'])
                        print("\nTeam: ", team_name, "Stats")
                        print("--------------------")
                        print("Total players: ", len(panthers), "\n")
                        print("Players on Team:")
                        print(", ".join(panthers_names),"\n")
                    elif select_team == 2:
                        team_name = "Warriors"
                        for player in warriors:
                            warriors_names.append(player['name'])
                        print("\nTeam: ", team_name, "Stats")
                        print("--------------------")
                        print("Total players: ",len(warriors),"\n")
                        print("Players on Team:")
                        print(", ".join(warriors_names),"\n")
                    elif select_team == 3:
                        team_name = "Bandits"
                        for player in bandits:
                            bandits_names.append(player['name'])
                        print("\nTeam: ", team_name, "Stats")
                        print("--------------------")
                        print("Total players: ", len(bandits), "\n")
                        print("Players on Team:")
                        print("\n",", ".join(bandits_names),"\n")
                elif selection > 2:
                    print("Entered number is too big! Try again!")
                else:
                    print("\nThank you for using this tool!")
                    exit()
            except ValueError:
                print("Sorry, select number from selection. Please try again!\n")

    start_basketball_stats()
