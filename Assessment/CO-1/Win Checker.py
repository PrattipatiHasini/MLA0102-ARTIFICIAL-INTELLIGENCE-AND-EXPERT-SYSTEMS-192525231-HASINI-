board = [
['X','X','X','X'],
['O','O','X','O'],
['X','O','O','X'],
['O','X','O','X']
]

winner=False

for row in board:
    for i in range(len(row)-3):
        if row[i]==row[i+1]==row[i+2]==row[i+3]:
            winner=True

if winner:
    print("Player Wins")
else:
    print("No Winner")
