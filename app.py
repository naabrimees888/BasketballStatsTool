import constants
import copy

if __name__ == '__main__':

    teams = copy.deepcopy(constants.TEAMS)
    players = copy.deepcopy(constants.PLAYERS)
    experienced = []
    unexpierenced = []
    panthers = []
    warriors = []
    bandits = []
    num_players_team = len(players) / len(teams)

    def clean_data():
        for player in players:
            player['height'] == int(player['height'] [:2])
            if player['experience'] == 'YES':
                player['experience'] == True
                experienced.append(player)
            else:
                unexpierenced.append(player)
    clean_data()


    def balance_teams(team):
        team_size = 0;
        while team_size < num_players_team:
                team.append(players.pop())
                team_size += 1

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
                    #while True:

                    select_team = int(input("\nSelect team > "))

                    if select_team == 1:
                            print("Team: ", teams[0], "stats")
                            print("----------------------")
                            print("Total players: ", len(panthers), "\n")
                            print("Players in team:")
                            for panther in panthers:
                                print(panther['name'], " ")
                    elif select_team == 2:
                        print("nr2")

                    elif select_team == 3:
                        print("nr 3")
                    else:
                        break
                else:
                    print("Tool closed. Thank you for watching!")
                exit()
            except ValueError:
                print("Sorry, select number from selection. Please try again!")
    start_basketball_stats()
