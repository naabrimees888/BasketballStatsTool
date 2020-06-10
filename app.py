import constants

if __name__ == '__main__':

    def start_baseball_stats():
        print("\nWELCOME TO BASEBALL TEAM STATS TOOL\n\n-----MENU ITEMS-----\n")
        while True:
            try:
                selection = int(input("Your choises:\n1. Display Team Stats\n2. Quit\nMake your selection > "))
                if selection == 1:
                    for index, team in enumerate(constants.TEAMS, 1):
                        print(f'{index}. {team}')
                    select_team = int(input("Make your selectoion > "))
                    if select_team == 1:
                        print("Nr 1")
                    elif select_team == 2:
                        print("nr2")
                    elif select_team == 3:
                        print("nr 3")
                else:
                    print("Tool closed")
                    exit()
            except ValueError:
                print("Sorry, it is not a number. Please try again!")

    start_baseball_stats()