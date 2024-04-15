# That is a really intresting problem, it reminded me a board game 'Robo Rally'.
import sys

# Creating an object robot to keep all the data for each robot in one place
class Robot:
  def __init__(self, initialX, initialY, direction, moves):
    self.initialX = initialX
    self.initialY = initialY
    self.direction = direction
    self.moves = moves

# the main process running in this function. Expecting the input in line with spaces in between from the user or 
# it is possible to pass the coordinates directly into the function. Returns list of coordinates where robots stop
def mainProcess(allInput = None):
    marsSurface, robotsAndMoves = handlingTheInput(allInput)
    
    endCoordRobots = movingRobots(marsSurface, robotsAndMoves)
    print(endCoordRobots)
    return endCoordRobots


# Expecting the input in line with spaces in between from the user or 
# it is possible to pass the coordinates directly into the function 
# returns array with the data
def handlingTheInput(allInput = None):
    if allInput == None:
        allInput = input('Please, provide: Mars size, coordinates of each robot and their moves. ')
    
    allInput = allInput.split()

    # the size of Mars
    maxX = castStringToInt(allInput[0])
    maxY = castStringToInt(allInput[1])
    
    marsSurface = (maxX, maxY)
    robotsAndMoves = splitRobotsAndMoves(allInput[2:])
    return marsSurface, robotsAndMoves

# input a list of strings, that contains info about each robot, the output the list of objets Robot with all the info per robot
def splitRobotsAndMoves(robotsAndMovesInStrings):
    # extract each piece of data per robot. It takes 4 position in array
    # i: 0 - init robot's coordinate X, 1 - init robot's coordnate Y, 2 - init direction of arobot, 3 - all moves it has to do
    robotsAndMoves = []
    count = 0
    while count < len(robotsAndMovesInStrings):
        initialX = 0
        initialY = 0
        initialDirection = ''
        robotMoves = ''
        for i in range(4):
            if i == 0:
                initialX = castStringToInt(robotsAndMovesInStrings[count])
            elif i == 1:
                initialY = castStringToInt(robotsAndMovesInStrings[count])
            elif i == 2:
                initialDirection = robotsAndMovesInStrings[count]
            else:
                robotMoves = robotsAndMovesInStrings[count]
            count += 1
        robotsAndMoves.append(Robot(initialX, initialY, initialDirection, robotMoves))

    return robotsAndMoves

# going to use it if convertin String to int went wrong
def exit():
    sys.exit('Thank you for being with us :)')

# moving each robot on the field. The function takes coordinates and robot moves
# returns the list of robot's positions
def movingRobots(marsSurface, robotsAndMoves):
    # the output of the problem
    endCoordRobots = []
    # dictionary with positions of robot's fall from the field
    coordRobotsFallOverEdge = dict()
    # processing each robot
    for robot in robotsAndMoves:
        endCoordRobots.append(movingRobotOnMars(marsSurface, coordRobotsFallOverEdge, robot))
        
    return endCoordRobots

def movingRobotOnMars(marsSurface, coordRobotsFallOverEdge, robot):
    # going through each robot's move
    currX = robot.initialX
    currY = robot.initialY
    currDirection = robot.direction
    lastCoordinate = ''

    for move in robot.moves:
        # turn the robot
        if move in ['L', 'R']:
            currDirection = turnRobot(currDirection, move)
        # move forward
        elif move == 'F':
            tmpX = currX
            tmpY = currY
            
            # check if this position is good to go, no one felt from the same place before. if it is, ignore the move
            if isSomeFallBefore(tmpX, tmpY, currDirection, coordRobotsFallOverEdge): 
                continue

            if currDirection == 'N':
                tmpY = tmpY + 1
            elif currDirection == 'S':
                tmpY = tmpY - 1
            elif currDirection == 'W':
                tmpX = tmpX - 1
            else:
                tmpX = tmpX + 1

            # check if this move leads us out of the field
            if (tmpX in range(marsSurface[0] + 1)) and (tmpY in range(marsSurface[1] + 1)):
                currX = tmpX
                currY = tmpY
            else:
                # it means the robot felt from the field. We have to save last coordinates 
                # and add this position in last seen dictionary
                lastCoordinate = str(currX) + ' ' + str(currY) + ' ' + currDirection + ' LOST'

                if currX in coordRobotsFallOverEdge:
                    coordRobotsFallOverEdge.get(currX).append(str(currY) + currDirection)
                else:
                    coordRobotsFallOverEdge[currX] = [str(currY) + currDirection]
                break
                    
    if len(lastCoordinate) == 0: 
        lastCoordinate = str(currX) + ' ' + str(currY) + ' ' + currDirection
    return lastCoordinate 
    

# Find a robot orientation oo the field
# input current facing and where to turn, output new facing
def turnRobot(currDirection, turn):
    parts = ['N', 'E', 'S', 'W']
    index = parts.index(currDirection)
    if turn == 'L':
        index = index - 1
    else:
        index = index + 1
    if index < 0:
        return parts[3]
    elif index > 3:
        return parts[0]
    else:
        return parts[index]

# check if a robot felt from this position before and return True if so
def isSomeFallBefore(coordX, coordY, direction, coordRobotsFallOverEdge):
    if coordX in coordRobotsFallOverEdge:
        if (str(coordY) + direction) in coordRobotsFallOverEdge.get(coordX):
            return True
    return False


# helper function with error handling during transformation string to int
def castStringToInt(stringToCast):
    try:
        goodInt = int(stringToCast)
    except ValueError:
        print('For coordinates we accept only numbers.')
        exit()
    except:
        print('Something went wrong, try to run the script again.')
        exit()
    return goodInt

# mainProcess('5 3 3 2 N FRRFLLFFRRFLL')
