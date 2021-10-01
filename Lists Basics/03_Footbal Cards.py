input_players = input()
list_of_players = input_players.split(" ")
team = 0
card_counter_A = int(0)
card_counter_B = int(0)
last_team = 0


for i in range (0, len(list_of_players)):
    team = list_of_players[i]
    if last_team == team:
        continue
    else: last_team = team

    if list_of_players[i] in list_of_players[:i:]:
        continue

    if "A" in team:
        card_counter_A += 1
    elif "B" in team:
        card_counter_B += 1

    team_A = 11 - card_counter_A
    team_B = 11 - card_counter_B

    if team_A < 7 or team_B < 7:
        print(f"Team A - {team_A}; Team B - {team_B}")
        print("Game was terminated")
        exit()
print(f"Team A - {team_A}; Team B - {team_B}")