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

primShips = [[(0,0),(0,0),(0,0),(0,0),(0,0)],   #Carrier        primShips[0][0...4]
          [(0,0),(0,0),(0,0),(0,0)],            #Battleship     primShips[1][0...3]
          [(0,0),(0,0),(0,0)],                  #Cruiser        primships[2][0...2]
          [(0,0),(0,0),(0,0)],                  #Submarine      primShips[3][0...2]
          [(0,0),(0,0)]                         #Destroyer      primShips[4][0...1]
    ]

print('Enter the ship you would like to place, followed by the coordinates to place it (i.e. "Carrier A1 A5")')
placing = (raw_input('> ')).lower()
placing = placing.split(' ')

#placing = 'carrier a1 a5'
#placing[1][0] = a
#placing[1][1] = 1
#placing[2][0] = a
#placing[2][1] = 5

if placing[0] == 'carrier':
    ind = (alphabet.lower()).find(placing[1][0]) + 1    #index of letter in alphabet of first coordinate
    ind2 = (alphabet.lower()).find(placing[2][0]) + 1   #index of letter in alphabet of second coordinate

    firstCord = (ind,int(placing[1][1]))
    secondCord = (ind2,int(placing[2][1]))

    #if ship is aligned vertically
    ### MUST CHECK COORDINATES ARE 4 UNITS APART
    if (firstCord[0] == secondCord[0]):
        if (firstCord[1] < secondCord[1]):
            primShips[0][0] = firstCord
            primShips[0][-1] = secondCord
        else:
            primShips[0][0] = secondCord
            primShips[0][-1] = firstCord

        primShips[0][1] = (primShips[0][0][0],primShips[0][0][1]+1)
        primShips[0][2] = (primShips[0][0][0],primShips[0][0][1]+2)
        primShips[0][3] = (primShips[0][0][0],primShips[0][0][1]+3)
            
    #if ship is aligned horizontally
    ### MUST CHECK COORDINATES ARE 4 UNITS APART
    elif (firstCord[1] == secondCord[1]):
        if (firstCord[0] < secondCord[0]):
            primShips[0][0] = firstCord
            primShips[0][-1] = secondCord
        else:
            primShips[0][0] = secondCord
            primShips[0][-1] = firstCord

        primShips[0][1] = (primShips[0][0][0]+1,primShips[0][0][1])
        primShips[0][2] = (primShips[0][0][0]+2,primShips[0][0][1])
        primShips[0][3] = (primShips[0][0][0]+3,primShips[0][0][1])
            
    #error: ship not aligned straight         
    else:
        print("Error: ship must be placed vertically or horizontally.")
    

    print primShips[0]

##    printH()
    
elif placing[0] == 'battleship':
    n = 1
    ind = (alphabet.lower()).find(placing[1][0]) + 1    #index of letter in alphabet of first coordinate
    ind2 = (alphabet.lower()).find(placing[2][0]) + 1   #index of letter in alphabet of second coordinate

    firstCord = (ind,int(placing[1][1]))
    secondCord = (ind2,int(placing[2][1]))

    #if ship is aligned vertically
    ### MUST CHECK COORDINATES ARE 3 UNITS APART
    if (firstCord[0] == secondCord[0]):
        if (firstCord[1] < secondCord[1]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        primShips[n][1] = (primShips[n][0][0],primShips[n][0][1]+1)
        primShips[n][2] = (primShips[n][0][0],primShips[n][0][1]+2)
            
    #if ship is aligned horizontally
    ### MUST CHECK COORDINATES ARE 3 UNITS APART
    elif (firstCord[1] == secondCord[1]):
        if (firstCord[0] < secondCord[0]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        primShips[n][1] = (primShips[n][0][0]+1,primShips[n][0][1])
        primShips[n][2] = (primShips[n][0][0]+2,primShips[n][0][1])
            
    #error: ship not aligned straight         
    else:
        print("Error: ship must be placed vertically or horizontally.")
    

    print primShips[n]

        
elif placing[0] == 'cruiser':
    n = 2
    ind = (alphabet.lower()).find(placing[1][0]) + 1    #index of letter in alphabet of first coordinate
    ind2 = (alphabet.lower()).find(placing[2][0]) + 1   #index of letter in alphabet of second coordinate

    firstCord = (ind,int(placing[1][1]))
    secondCord = (ind2,int(placing[2][1]))

    #if ship is aligned vertically
    ### MUST CHECK COORDINATES ARE 2 UNITS APART
    if (firstCord[0] == secondCord[0]):
        if (firstCord[1] < secondCord[1]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        primShips[n][1] = (primShips[n][0][0],primShips[n][0][1]+1)
        primShips[n][2] = (primShips[n][0][0],primShips[n][0][1]+2)
            
    #if ship is aligned horizontally
    ### MUST CHECK COORDINATES ARE 2 UNITS APART
    elif (firstCord[1] == secondCord[1]):
        if (firstCord[0] < secondCord[0]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        primShips[n][1] = (primShips[n][0][0]+1,primShips[n][0][1])
            
    #error: ship not aligned straight         
    else:
        print("Error: ship must be placed vertically or horizontally.")
    

    print primShips[n]
    
elif placing[0] == 'submarine':
    n = 3
    ind = (alphabet.lower()).find(placing[1][0]) + 1    #index of letter in alphabet of first coordinate
    ind2 = (alphabet.lower()).find(placing[2][0]) + 1   #index of letter in alphabet of second coordinate

    firstCord = (ind,int(placing[1][1]))
    secondCord = (ind2,int(placing[2][1]))

    #if ship is aligned vertically
    ### MUST CHECK COORDINATES ARE 2 UNITS APART
    if (firstCord[0] == secondCord[0]):
        if (firstCord[1] < secondCord[1]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        primShips[n][1] = (primShips[n][0][0],primShips[n][0][1]+1)
        primShips[n][2] = (primShips[n][0][0],primShips[n][0][1]+2)
            
    #if ship is aligned horizontally
    ### MUST CHECK COORDINATES ARE 2 UNITS APART
    elif (firstCord[1] == secondCord[1]):
        if (firstCord[0] < secondCord[0]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        primShips[n][1] = (primShips[n][0][0]+1,primShips[n][0][1])
            
    #error: ship not aligned straight         
    else:
        print("Error: ship must be placed vertically or horizontally.")
    

    print primShips[n]
    
elif placing[0] == 'destroyer':
    n = 4
    ind = (alphabet.lower()).find(placing[1][0]) + 1    #index of letter in alphabet of first coordinate
    ind2 = (alphabet.lower()).find(placing[2][0]) + 1   #index of letter in alphabet of second coordinate

    firstCord = (ind,int(placing[1][1]))
    secondCord = (ind2,int(placing[2][1]))

    #if ship is aligned vertically
    ### MUST CHECK COORDINATES ARE 1 UNITS APART
    if (firstCord[0] == secondCord[0]):
        if (firstCord[1] < secondCord[1]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        primShips[n][1] = (primShips[n][0][0],primShips[n][0][1]+1)
        primShips[n][2] = (primShips[n][0][0],primShips[n][0][1]+2)
            
    #if ship is aligned horizontally
    ### MUST CHECK COORDINATES ARE 1 UNITS APART
    elif (firstCord[1] == secondCord[1]):
        if (firstCord[0] < secondCord[0]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord
            
    #error: ship not aligned straight         
    else:
        print("Error: ship must be placed vertically or horizontally.")
    

    print primShips[n]
    
##for li in primShips:
##    print li




