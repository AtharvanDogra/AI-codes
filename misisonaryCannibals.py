import operator
class State:
    def __init__(self,missionaries, cannibals, boatPosition) :
        self.value = (missionaries, cannibals, boatPosition)
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boatPosition = boatPosition
        self.parent = None  
        self.heuristic = (missionaries + cannibals)/boat_cap
    
    def __eq__(self, other):                    #__eq__ and __hash__ are added for comparison for equality of objects 
        if not isinstance(other, State):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.value == other.value  #and self.parent == other.parent       #checks equality only on basis of value and not parent

    def __hash__(self):                                                         #added for immutable
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.value, self.parent))

    def isValid(self):
        if any(x<0 for x in self.value):
            return False
        if self.missionaries>3 or self.cannibals>3:
            return False
        if self in open or self in visited:
            return False 
        if  self.boatPosition > 1 :
            return False
        if self.has_more_Cannibals():
            return False
        else:
            return True

    def has_more_Cannibals(self):
        return (( self.missionaries>0 and self.cannibals > self.missionaries) or #more cannibles on wrong side
                ( self.missionaries<3 and self.missionaries > self.cannibals) or  #more cannibles on right side
                ( self.missionaries==0 and self.cannibals== 3))


boat_cap=2
goal_State = State(0,0,1)
initial_State = State(3,3,0)
open = []
visited = []
FirstLayerPassed=False

  
def apply_heuristic():      # (missionary+cannibals)/boatCapacity
    open.sort(key = operator.attrgetter('heuristic'))      #CHECK REVERSE       #Attrgetter function gets attribute for key here
    return open.pop(0)

def isGoal(state):
    return state.value == goal_State.value

def generateState(state,rider,boat_cap):
    count = state.missionaries + state.cannibals - rider

    for i in range(0,count+1) :         #check count or count+1
        for j in range(i,count+1):

            if i+j == count:
                childState = State(i,j,1)       #(1,3)
                if childState.isValid():
                    childState.parent = state 
                    open.append(childState)     #object is passed into open list

                childState1 = State(j,i,1)      #(3,1)
                if childState1.isValid():
                    childState1.parent = state 
                    open.append(childState1)     #object is passed into open list

    if state not in visited :
        visited.append(state)

def solve(state,boat_cap):

    global FirstLayerPassed

    if isGoal(state):
        visited.append(state)
        return True

    for rider in range(1,boat_cap+1):
        if not ( FirstLayerPassed and rider == boat_cap):
            generateState(state,rider,boat_cap)
        
    FirstLayerPassed =True
    solve(apply_heuristic(),boat_cap)           #heuristic sorting on open list and popping the best element

def printPath(state):
    path =[]
    while state.parent !=None:
        path.append(state.value)
        state = state.parent

    path.append(state.value)
    path.sort(reverse =True)

    print(path)


solve(initial_State,2)

print([x.value for x in visited])
