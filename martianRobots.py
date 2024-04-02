import sys

# the main process running in this function
def mainProcess(coordMoves = None):
    userData = handlingTheInput(coordMoves)
    try:
        # mars size
        coordX = int(userData[0])
        coordY = int(userData[1])
    except ValueError:
        print('For coordinates we accept only numbers.')
        exit()
    except:
        print('Something went wrong, try to run the script again.')
        exit()

    listOfStops = movingRobots(coordX, coordY, userData[2:])
    print(listOfStops)
    return listOfStops


# Expecting the input in line with spaces in between from the user or 
# it is possible to pass the coordinates directly into the function 
# returns array with the data
def handlingTheInput(coordMoves = None):
    if coordMoves == None:
        coordMoves = input('Please, provide: Mars size, coordinates of each robot and their moves. ')
    
    return coordMoves.split()

# going to use it if convertin String to int went wrong
def exit():
    sys.exit('Thank you for being with us :)')

# moving each robot on the field. The function takes coordinates and robot moves
# returns the list of robot's positions
def movingRobots(coordX, coordY, robotData):
    # the output of the problem
    listOfStop = []
    # dictionary with positions of robot's fall from the field
    coordOfRobFall = dict()
    
    # extract each piece of data per robot. It takes 4 position in array
    # 0 - robot's coordinate X, 1 - robot's coordnate Y, 2 - which direction robot faced, 3 - all moves it has to do
    count = 0
    while count < len(robotData):
        robotCoordX = 0
        robotCoordY = 0
        robotFaced = ''
        robotSteps = ''
        for i in range(4):
            try:
                if i == 0:
                    robotCoordX = int(robotData[count])
                elif i == 1:
                    robotCoordY = int(robotData[count])
                elif i == 2:
                    robotFaced = robotData[count]
                else:
                    robotSteps = robotData[count]
            except ValueError:
                print('For coordinates we accept only numbers.')
                exit()
            except:
                print('Something went wrong, try to run the script again.')
                exit()
            count += 1
    
        # processing each robot
        movingRobOnField(coordX, coordY, listOfStop, coordOfRobFall, robotCoordX, robotCoordY, robotFaced, robotSteps)
    return listOfStop

def movingRobOnField(coordX, coordY, listOfStop, coordOfRobFall, robotCoordX, robotCoordY, robotFaced, robotSteps):
    # going through each robot's move
    currX = robotCoordX
    currY = robotCoordY
    currFaced = robotFaced
    
    for move in robotSteps:
        # turn the robot
        if move in ['L', 'R']:
            currFaced = turnRobot(currFaced, move)
        # move forward
        elif move == 'F':
            tmpX = currX
            tmpY = currY
            
            # check if this position is good to go, no one falls here before
            if isSomeFallBefore(tmpX, tmpY, currFaced, coordOfRobFall): 
                continue

            if currFaced == 'N':
                tmpY = tmpY + 1
            elif currFaced == 'S':
                tmpY = tmpY - 1
            elif currFaced == 'W':
                tmpX = tmpX - 1
            else:
                tmpX = tmpX + 1

            # check if this move leads out of the field
            if (tmpX in range(coordX + 1)) and (tmpY in range(coordY + 1)):
                currX = tmpX
                currY = tmpY
            else:
                # it means the robot felt from the field. We have to save last coordinates 
                # and add this position in last seen dictionary
                listOfStop.append(str(currX) + ' ' + str(currY) + ' ' + currFaced + ' LOST')

                if currX in coordOfRobFall:
                    coordOfRobFall.get(currX).append(str(currY) + currFaced)
                else:
                    coordOfRobFall[currX] = [str(currY) + currFaced]
                return
                    
    listOfStop.append(str(currX) + ' ' + str(currY) + ' ' + currFaced)
    return



# Find a robot orientation oo the field
# input current facing and where to turn, output new facing
def turnRobot(currFacing, turn):
    parts = ['N', 'E', 'S', 'W']
    index = parts.index(currFacing)
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
def isSomeFallBefore(x, y, faced, coordOfRobFall):
    if x in coordOfRobFall:
        if (str(y) + faced) in coordOfRobFall.get(x):
            return True
    return False

# mainProcess('5 3 3 2 N FRRFLLFFRRFLL')