import random

#random Library choose randonm city

def randomSolution(tsp):
    cities=list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity= cities [random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
        
    return solution

def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i-1]] [solution[i]]
    return routeLength

def getNeighbours (solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            neighbour =solution.copy() 
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours 

def getBestNeighbour (tsp, neighbours): 
    bestRouteLength =routeLength(tsp, neighbours[0])
    bestNeighbour= neighbours[0] 
    for neighbour in neighbours:
        currentRouteLength =routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength= currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

def hillClimbing(tsp):
    currentSolution= randomSolution(tsp)
    print("currentSolution is ")
    print(currentSolution)
    currentRouteLength =routeLength(tsp, currentSolution) 
    print("currentRouteLength is ")
    print(currentRouteLength)
    neighbours =getNeighbours (currentSolution)
    print("Below are neighbours list ")
    nighbours=getneighbour(tsp,currrentSolution)
    for i in nighbours:
        print(f"{i} cost= {routeLength(tsp, i)}")

    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour (tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:

            currentRouteLength =bestNeighbour
            currentRouteLength=bestNeighbourRouteLength
            neighbours =getNeighbours(currentSolution)
            bestNeighbour,bestNeighbourRouteLength=getBestNeighbour(tsp,neighbours)
    
    print("BEST SOLUTION AND BEST ROUTE LENGTH IS ")
    return currentSolution, currentRouteLength

def main():

    tsp =[

        [0, 400, 500, 300], 
        [400, 0, 300,500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]
    print(hillClimbing(tsp))

if __name__=="__main__":
    main()
