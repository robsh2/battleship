import sys

print("Welcome to Battleship!")
##print('Argument List:', str(sys.argv))
##print(int(sys.argv[1]))
##print(int(sys.argv[2]))

length = int(sys.argv[1])
height = int(sys.argv[2])
alphabet  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#<<initializing the player's board>>
print("\nPlayer's Board:")
playerBoard = [['.' for x in range(length+1)] for y in range(height+1)]

for i in range(1,length+1):
    playerBoard[0][i] = alphabet[i-1]
for i in range(1,height+1):
    playerBoard[i][0] = i

for row in playerBoard:
    print ' '.join(str(spot) for spot in row)

##<<initializing the computer's board
print("\nComputer's Board:")
compBoard = [['?' for x in range(length+1)] for y in range(height+1)]

for i in range(1,length+1):
    compBoard[0][i] = alphabet[i-1]
for i in range(1,height+1):
    compBoard[i][0] = i

for row in compBoard:
    print ' '.join(str(spot) for spot in row)
