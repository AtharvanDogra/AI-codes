import copy

puzzle = [[2  ,None,3],
          [1  ,8   ,4],
          [7  ,6   ,5]]

target = [[1  ,2  , 3],
          [8  ,None,4],
          [7  ,6   ,5]]

found = False
printTarget = False
#blank = [(x,y) for x,list in enumerate(state) for y,item in enumerate(list) if item==None].pop()   

def up(state):
    global printTarget
    if found and not printTarget:
        printTarget= True
        for x in target:
            for y in x:
                if y==None:
                    print(" ",end=" | ")
                else:
                    print(y,end=" | ")
            print()
            print("-----------")
        print()

    newstate = copy.deepcopy(state)       
    blank = [(x,y) for x,list in enumerate(state) for y,item in enumerate(list) if item==None].pop()

    if 0 <blank[0] <len(state) and not found: #boolstateblank[0]-1]blank[1]])

        
        newstate[blank[0]][blank[1]], newstate[blank[0]-1][blank[1]] = newstate[blank[0]-1][blank[1]],newstate[blank[0]][blank[1]]
        return newstate 
    elif found:
        return newstate
  

def down(state):
    global printTarget
    if found and not printTarget:
        printTarget= True
        for x in target:
            for y in x:
                if y==None:
                    print(" ",end=" | ")
                else:
                    print(y,end=" | ")
            print()
            print("-----------")
        print()

    stateNew= copy.deepcopy(state)     
    blank = [(x,y) for x,list in enumerate(state) for y,item in enumerate(list) if item==None].pop()
   
    #try:
    if 0 <=blank[0] <len(state)-1 and not found:#boolstateblank[0]+1]blank[1]]):

        
        stateNew[blank[0]][blank[1]],stateNew[blank[0]+1][blank[1]] = stateNew[blank[0]+1][blank[1]],stateNew[blank[0]][blank[1]]
        return stateNew
    elif found:
        return stateNew
    #except :
    #    return None

def left(state):
    global printTarget
    if found and not printTarget:
        printTarget= True
        for x in target:
            for y in x:
                if y==None:
                    print(" ",end=" | ")
                else:
                    print(y,end=" | ")
            print()
            print("-----------")
        print()

    blank = [(x,y) for x,list in enumerate(state) for y,item in enumerate(list) if item==None].pop()    
    stateNew = copy.deepcopy(state)                        
    #try:
    if 0 <blank[1] <len(state) and not found:#boolstateblank[0]]blank[1]-1]):
        
        stateNew = copy.deepcopy(state)
        stateNew[blank[0]][blank[1]],stateNew[blank[0]][blank[1]-1] = stateNew[blank[0]][blank[1]-1],stateNew[blank[0]][blank[1]]
        return stateNew
    elif found:
        return stateNew
    #except :
    #   return None

def right(state):
    global printTarget
    if found and not printTarget:
        printTarget= True
        for x in target:
            for y in x:
                if y==None:
                    print(" ",end=" | ")
                else:
                    print(y,end=" | ")
            print()
            print("-----------")
        print()

    stateNew = copy.deepcopy(state)    
    blank = [(x,y) for x,list in enumerate(state) for y,item in enumerate(list) if item==None].pop()
    #try:
    if 0 <=blank[1] <len(state)-1 and not found:#boolstateblank[0]]blank[1]+1]):          
        
        
        stateNew[blank[0]][blank[1]],stateNew[blank[0]][blank[1]+1] = stateNew[blank[0]][blank[1]+1],stateNew[blank[0]][blank[1]]
        return stateNew
    elif found:
        return stateNew
    #except :
    #   return None
                
def dls(state,limit,dir) ->bool:
    
    global found
    if found:
        return True
    if state == target:      
        found = True
        return True

    if limit <=0:
        return False
    
    if state == None:
       return False
    
    if dir!='down' and dls(up(state),limit-1,'up') and found :      #move up
        for x in up(state):
            for y in x:
                if y==None:
                    print(" ",end=" | ")
                else:
                    print(y,end=" | ")
            print()
            print("------------")        
        print()
    if dir!='up' and dls(down(state),limit-1,'down') and found :    #move down
        for x in down(state):
            for y in x:
                if y==None:
                    print(" ",end=" | ")
                else:
                    print(y,end=" | ")
            print()
            print("-----------")
        print()
        
    if dir!='right' and dls(left(state),limit-1,'left') and found : #move left
        for x in left(state):
            for y in x:
                if y==None:
                    print(" ",end=" | ")
                else:
                    print(y,end=" | ")
            print()
            print("-----------")
        print()
    if dir!='left' and dls(right(state),limit-1,'right') and found :    #move right
     
        for x in right(state):
            for y in x:
                if y==None:
                    print(" ",end=" | ")
                else:
                    print(y,end=" | ")
            print()
            print("-----------")
        print()
dls(puzzle,3,'down')   