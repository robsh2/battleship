import sys

def printH(): #function printing out the boards side by size horizontally
    print('Primary Grid:\t\t\tTracking Grid:')
    for i in range(0,length+1):
        print(' '.join(str(spot) for spot in primGrid[i])),'\t',
        print(' '.join(str(spot) for spot in trackGrid[i]))
    return

def printV(): #functions printing out the boards vertically stacked
    print("\nPrimary Grid:")
    for row in primGrid:
        print(' '.join(str(spot) for spot in row))

    print("\nTracking Grid:")
    for row in trackGrid:
        print (' '.join(str(spot) for spot in row))
    return

##if (len(sys.argv) != 2): ## DOESNT WORK
##    print('battleship.py: Two arguments must be given (int m, int n)')
##    sys.exit() 

print("Welcome to Battleship!")
length = int(sys.argv[1])
height = int(sys.argv[2])
alphabet  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

##<<INSERT CHECK: TWO INT ARGS EACH GREATER THAN 9>>

##<<initializing the primary grid>>
primGrid = [['.' for x in range(length+1)] for y in range(height+1)]

#labeling Primary grid's axis
for i in range(1,length+1):
    primGrid[0][i] = alphabet[i-1]
for i in range(1,height+1):
    primGrid[i][0] = i

##<<initializing the computer's board
trackGrid = [['?' for x in range(length+1)] for y in range(height+1)]

#labeling tracking grid's axis
for i in range(1,length+1):
    trackGrid[0][i] = alphabet[i-1]
for i in range(1,height+1):
    trackGrid[i][0] = i

x = ''
y = ''

ships = {'Carrier':5,
          'Battleship':4,
          'Cruiser':3,
          'Submarine':3,
          'Destroyer':2}

printH()

##<<< SHIP PLACEMENT >>>
## << PRIMARY GRID >>

print("Carrier: %d" % ships['Carrier'])
print("Battleship: %d" % ships['Battleship'])
print("Cruiser: %d" % ships['Cruiser'])
print("Submarine: %d" % ships['Submarine'])
print("Destroyer: %d" % ships['Destroyer'])

primShips = [[(0,0),(0,0),(0,0),(0,0),(0,0)],  #Carrier
          [(0,0),(0,0),(0,0),(0,0)],        #Battleship
          [(0,0),(0,0),(0,0)],              #Cruiser
          [(0,0),(0,0),(0,0)],              #Submarine
          [(0,0),(0,0)]                     #Destroyer
    ]

print('Enter the ship you would like to place, followed by the coordinates to place it (i.e. "Carrier A1 A5")')
placing = (raw_input('> ')).lower()
placing = placing.split(' ')

if placing[0] == 'carrier':
    #print placing[1][0],placing[1][1] #start coordinates: "a, 1" 
    #print placing[2][0],placing[2][1] #end coordinates: "a, 5"

    ind = (alphabet.lower()).find(placing[1][0]) + 1    #letter of start coordinate
    ind2 = (alphabet.lower()).find(placing[2][0]) + 1   #letter of end coordinate

    #print ind,ind2

    primGrid[int(placing[1][1])][ind] = 'C'      #start coordinate
    primGrid[int(placing[2][1])][ind2] = 'C'     #end coordinate

    printH()
    
elif placing[0] == 'battleship':
    print placing[1][0],placing[1][1] # start coordinates
    print placing[2][0],placing[2][1] # end coordinates

    
elif placing[0] == 'cruiser':
    print placing[1][0],placing[1][1]
    print placing[2][0],placing[2][1]
elif placing[0] == 'submarine':
    print placing[1][0],placing[1][1]
    print placing[2][0],placing[2][1]
elif placing[0] == 'destroyer':
    print placing[1][0],placing[1][1]
    print placing[2][0],placing[2][1]


    
##print("Enter ship you would like to place:")
##placing = (raw_input('> ')).lower()
##
##if placing == 'carrier':
##    print('Placing Carrier. Enter starting letter coordinate:')
##    startLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    startNC = raw_input('> ')
##
##    startC = (startLC,startNC)
##    primShips[0][0] = startC
##
##    print('Enter ending letter coordinate:')
##    endLC = raw_input('> ')
##    print('Enter ending number coordinate:')
##    endNC = raw_input('> ')
##
##    endC = (endLC,endNC)
##    primShips[0][4] = endC
##    
##elif placing == 'battleship':
##    print('Placing Battleship. Enter starting letter coordinate:')
##    startLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    startNC = raw_input('> ')
##
##    startC = (startLC,startNC)
##    primShips[1][0] = startC
##
##    print('Enter ending letter coordinate:')
##    endLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    endNC = raw_input('> ')
##
##    endC = (endLC,endNC)
##    primShips[1][3] = endC
##    
##elif placing == 'cruiser':
##    print('Placing Cruiser. Enter starting letter coordinate:')
##    startLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    startNC = raw_input('> ')
##
##    startC = (startLC,startNC)
##    primShips[2][0] = startC
##
##    print('Enter ending letter coordinate:')
##    endLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    endNC = raw_input('> ')
##
##    endC = (endLC,endNC)
##    primShips[2][2] = endC
##    
##elif placing == 'submarine':
##    print('Placing Submarine. Enter starting letter coordinate:')
##    startLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    startNC = raw_input('> ')
##
##    startC = (startLC,startNC)
##    primShips[3][0] = startC
##
##    print('Enter ending letter coordinate:')
##    endLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    endNC = raw_input('> ')
##
##    endC = (endLC,endNC)
##    primShips[3][2] = endC
##    
##elif placing == 'destroyer':
##    print('Placing Destroyer. Enter starting letter coordinate:')
##    startLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    startNC = raw_input('> ')
##
##    startC = (startLC,startNC)
##    primShips[4][0] = startC
##
##    print('Enter ending letter coordinate:')
##    endLC = raw_input('> ')
##    print('Enter starting number coordinate:')
##    endNC = raw_input('> ')
##
##    endC = (endLC,endNC)
##    primShips[4][1] = endC
##else:
##    print('Try again.')

##for li in primShips:
##    print li
