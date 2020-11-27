import sys
import re
import random

##############################################
## FUNCTION: PRINT GRIDS HORIZONTALLY
##############################################

def printH(): #function printing out the boards side by size horizontally
    print('Primary Grid:\t\t\tTracking Grid:')
    primGrid[0][0] = '\\'
    trackGrid[0][0] = '\\'
    for i in range(0,height+1):
        print(' '.join(str(spot) for spot in primGrid[i])),'\t',
        print(' '.join(str(spot) for spot in trackGrid[i]))
    return


##############################################
## FUNCTION: PRINT GRIDS VERTICALLY
##############################################

def printV(): #functions printing out the boards vertically stacked
    print("\nPrimary Grid:")
    primGrid[0][0] = '\\'
    for row in primGrid:
        print(' '.join(str(spot) for spot in row))
    print ('\n')

    print("\nTracking Grid:")
    trackGrid[0][0] = '\\'
    for row in trackGrid:
        print (' '.join(str(spot) for spot in row))
    print ('\n')
    return

##############################################
## FUNCTION: PLACE SHIPS ON PRIMARY GRID
##############################################

def place(n, placing, primShips): 
    #STRUCTURE OF USER INPUT VARIABLE placing:
    #placing        =      'carrier     a1      a5'
    #placing[0]     ~>     'carrier'
    #placing[1]     ~>                 'a1'
    #placing[2]     ~>                         'a5'
    #placing[1][0]  ~>                 'a'
    #placing[1][1]  ~>                  '1'
    #placing[2][0]  ~>                         'a'
    #placing[2][1]  ~>                          '5'
    
    ind = (alphabet.lower()).find(placing[1][0]) + 1    #index of letter in alphabet of first coordinate
    ind2 = (alphabet.lower()).find(placing[2][0]) + 1   #index of letter in alphabet of second coordinate

    #captures remaining characters after letter coordinate and converts to int
    sep = '[a-zA-Z]'
    num1 = int((re.split(sep,placing[1],1))[1])
    num2 = int((re.split(sep,placing[2],1))[1])

    firstCord = (ind,num1)
    secondCord = (ind2,num2)

    #if ship is aligned vertically
    ### MUST CHECK COORDINATES ARE 2 UNITS APART
    if (firstCord[0] == secondCord[0]):
        if (firstCord[1] < secondCord[1]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        #STUCTURE OF PRIMSHIPS: primShips [ship type]                  [coordinate set]      [coordinate]
        #                       primShips ['carrier'/'battleship'/ETC] [('A',1),('A',2),ETC] ['A' or 1]
        if ((placing[0] == 'carrier') or (placing[0] == 'battleship')
            or (placing[0] == 'cruiser') or (placing[0] == 'submarine')):

            primShips[n][1] = (primShips[n][0][0],primShips[n][0][1]+1)
    
            if ((placing[0] == 'carrier') or (placing[0] == 'battleship')):
                primShips[n][2] = (primShips[n][0][0],primShips[n][0][1]+2)

                if (placing[0] == 'carrier'):
                    primShips[n][3] = (primShips[n][0][0],primShips[n][0][1]+3)
                    
    #if ship is aligned horizontally
    ### MUST CHECK COORDINATES ARE 2 UNITS APART
    elif (firstCord[1] == secondCord[1]):
        if (firstCord[0] < secondCord[0]):
            primShips[n][0] = firstCord
            primShips[n][-1] = secondCord
        else:
            primShips[n][0] = secondCord
            primShips[n][-1] = firstCord

        #STUCTURE OF PRIMSHIPS: primShips [ship type]                  [coordinate set]      [coordinate]
        #                       primShips ['carrier'/'battleship'/ETC] [('A',1),('A',2),ETC] ['A' or 1]
        if ((placing[0] == 'carrier') or (placing[0] == 'battleship')
            or (placing[0] == 'cruiser') or (placing[0] == 'submarine')):

            primShips[n][1] = (primShips[n][0][0]+1,primShips[n][0][1])

            if ((placing[0] == 'carrier') or (placing[0] == 'battleship')):
                primShips[n][2] = (primShips[n][0][0]+2,primShips[n][0][1])

                if (placing[0] == 'carrier'):
                    primShips[n][3] = (primShips[n][0][0]+3,primShips[n][0][1])
            
    #error: ship not aligned straight         
    else:
        print("Error: ship must be placed vertically or horizontally.")

###################################################
## FUNCTION: Begin taking user input to place ships
###################################################

def primPlacement(primShips):

    ##<<< SHIP PLACEMENT >>>
    ## NOTE:    Must still check if ships placed are of correct length.
    ##          Must still print which ships have yet to be placed after placement of a ship.
    ##          Must still check if ships are placed within bounds and not over each other.
    ## << PRIMARY GRID >>

    donePlacingShips = False #SET TO TRUE WHILE TESTING TO SKIP PRIM GRID PLACEMENT
    print ('\nYour fleet: 1 Carrier. 1 Battleship. 1 Cruiser. 1 Submarine. 1 Destroyer.')
    while (donePlacingShips == False):

        print('Enter the ship you would like to place, followed by the coordinates to place it (i.e. "Carrier A1 A5")')
        placing = (input('> ')).lower()
        placing = placing.split(' ')
        if placing[0] == 'carrier':
            place(0, placing, primShips)
        elif placing[0] == 'battleship':
            place(1,placing, primShips)
        elif placing[0] == 'cruiser':
            place(2,placing, primShips)
        elif placing[0] == 'submarine':
            place(3,placing, primShips)
        elif placing[0] == 'destroyer':
            place(4,placing, primShips)
        else:
            print('Try again.')

        #check primShips[n] for unplaced ships (those containing the point (0,0))
        donePlacingShips = True
        index = 0
        placed = []
        for ship in primShips:
            if (0,0) not in ship:
                placed.append(index)
            else:
                donePlacingShips = False 
            index += 1

        #Print ship coordinates in primShips onto primGrid
        for (x,y) in primShips[0]:
            #prints correctly when x and y are in opposite arrangements as expected
            primGrid[y][x] = 'C'
        for (x,y) in primShips[1]:
            primGrid[y][x] = 'B'
        for (x,y) in primShips[2]:
            primGrid[y][x] = 'C'
        for (x,y) in primShips[3]:
            primGrid[y][x] = 'S'
        for (x,y) in primShips[4]:
            primGrid[y][x] = 'D'

        printH()

        if 0 not in placed: print ("1 Carrier. "),
        if 1 not in placed: print ("1 Battleship. "),
        if 2 not in placed: print ("1 Cruiser. "),
        if 3 not in placed: print ("1 Submarine. "),
        if 4 not in placed: print ("1 Destroyer. "),
        print ('\n')

##############################################
## FUNCTION: GENERATE TRACKING GRID SHIPS
##############################################
def genShip(n):
    alphaCord = random.randrange(1,length+1)
    numCord = random.randrange(1,height+1)

    flip = random.randrange(0,2) #50/50 chance to determing if ship is vertical or horizontal

    if flip == 0:
        
        for i in range(0,lengths[n]):
            trackShips[n][i] = (alphaCord+i,numCord)

        overlap = False
 
        for (x,y) in trackShips[n]:
            for m in range(0,5):
                    if (x,y) in trackShips[m]:
                        if (n != m): overlap = True

        if ((alphaCord+lengths[n]-1) in xrange) and (overlap == False):
            for (x,y) in trackShips[n]:
                trackGrid[y][x] = labels[n]
        else: genShip(n)

    else:
        for i in range(0,lengths[n]):
            trackShips[n][i] = (alphaCord,numCord+i)

        overlap = False
 
        for (x,y) in trackShips[n]:
            for m in range(0,5):
                    if (x,y) in trackShips[m]:
                        if (n != m): overlap = True

        if ((numCord+lengths[n]-1) in yrange) and (overlap == False):
            for (x,y) in trackShips[n]:
                trackGrid[y][x] = labels[n]
        else: genShip(n)

################################################
################ END OF FUNCTIONS ##############
################################################
    
if len(sys.argv) != 3:
    print('battleship.py: Two arguments must be given (int m, int n)' , file=sys.stderr)
    sys.exit()
try: 
    for arg in sys.argv[1:]:
        number = int(arg)
        if number < 9:
            print ('Argument', number, 'is less than 9')
        else:
            pass
except:
    print ('The first argument contains an integer less than 9')
    
try: 
    for arg in sys.argv[2:]:
        number = int(arg)
        if number < 9:
            print ('Argument 2', number, 'is less than 9')
        else:
            pass
except:
    print ('The first argument contains an integer less than 9')


print("Welcome to Battleship!")
length = int(sys.argv[1])
height = int(sys.argv[2])
trackSymbol = '-'
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
trackGrid = [[trackSymbol for x in range(length+1)] for y in range(height+1)]

#labeling tracking grid's axis
for i in range(1,length+1):
    trackGrid[0][i] = alphabet[i-1]
for i in range(1,height+1):
    trackGrid[i][0] = i

lengths = [5,4,3,3,2]                   #lengths of ships
labels  = ['C','B','C','S','D']         #labels for ships
xrange = range(1,length+1)              #ranges for ships to be placed
yrange = range(1,height+1)

printH()

primShips = [[(0,0),(0,0),(0,0),(0,0),(0,0)],       #Carrier        primShips[0][0...4]
            [(0,0),(0,0),(0,0),(0,0)],              #Battleship     primShips[1][0...3]
            [(0,0),(0,0),(0,0)],                    #Cruiser        primships[2][0...2]
            [(0,0),(0,0),(0,0)],                    #Submarine      primShips[3][0...2]
            [(0,0),(0,0)]]                          #Destroyer      primShips[4][0...1]

#placing primary grid ships from player input
#primPlacement(primShips)

print ('All ships placed! Placing enemy ships...\n')
### DONE PLACING PRIMARY GRID SHIPS.
### STARTING TRACKING GRID SHIP PLACEMENT

trackShips = [[(0,0),(0,0),(0,0),(0,0),(0,0)],      #Carrier        trackShips[0][0...4]
             [(0,0),(0,0),(0,0),(0,0)],             #Battleship     trackShips[1][0...3]
             [(0,0),(0,0),(0,0)],                   #Cruiser        trackShips[2][0...2]
             [(0,0),(0,0),(0,0)],                   #Submarine      trackShips[3][0...2]
             [(0,0),(0,0)]]                         #Destroyer      trackShips[4][0...1]
#randomly place tracking grid ships
for n in range(0,5):
    genShip(n)

printH()


#ships are placed now
#take user input for trying to hit ship
#   if user guess correct, mark X on tracking grid, mark (X,X) on trackShips
#randomly guess on primary grid
#   if machine guess correct, mark X on primary grid, mark (X,X) on primShips
#if all coordinates in trackShips == (X,X), player wins
#if all coordinates in primShips == (X,X), machine wins

def getGuess():
    print('Enter enemy coordinates to attack (i.e. "D6")')
    guess = (input('> ')).lower()

    alph = (alphabet.lower()).find(guess[0]) + 1    #index of letter in alphabet of first coordinate
    
    #captures remaining characters after letter coordinate and converts to int
    sep = '[a-zA-Z]'
    num = int((re.split(sep,guess,1))[1])
    
    guessCord = (alph,num)

    if (alph not in yrange) or (num not in xrange):
        print ('Invalid guess. Try again.')
        guessCord = getGuess()
        
  
    return guessCord

def round(trackShips, primShips):
    guessCord = getGuess()

    hitFlag = False
    for n in range(0,5):
        for trackCord in trackShips[n]:
            if (guessCord == trackCord):
                trackCord = (-1,-1)
                trackGrid[guessCord[1]][guessCord[0]] = 'X'
                hitFlag = True

    if (hitFlag == True):
        print ('Hit!')
    else:
        print ('Miss!')

    printH()

round(trackShips, primShips)




























    
