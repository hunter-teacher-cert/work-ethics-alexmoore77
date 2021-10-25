#AM Annotated plane_seating.Python
#alexmoore77
#Ethical Airlines Solution:  Let families sit together.
"""
Note:  I spent over ten hours on this project.  It helped me to improve my Python skills significantly and begin to understand many key/value pairings in particular

Key Ethical Addition:  Allow families to sit together.  
1) Create an original set of families with names and values.
2) Traverse the dictionary and use concatenation to create individual family members with the naming convention lastName-memberNumber
3)  Traverse the plane horizontally and then vertically.
4)  Splice the name string to retrieve the last name, and pass this as an added argument to the function.
5)  Check the argument name against any existing plane names.  If there is a match and an adjacent seat is open, assign that customer there.  
6)  If there is no match, place the customer randomly.

Implementation:  
1) I created some original functions.
2) I slightly or signifantly modified existing functions.
3) I debugged like nobody's business, hence all of the print statements.  

Next Steps:  
I plan to continue to work on my Python chess game.  As Python seems to be becoming the language of choice for AP CSP, it is certainly a good language to know.  Thanks.


"""

#AM- This module adds psuedorandom numbers
import random

def family_print(economy_sold):
  for k in economy_sold.keys():
    print(k+" bought "+str(economy_sold[k])+" tickets.")
  #  print (v, economy_sold[v])
  #print(economy_sold)


def create_plane(rows,cols):
#AM - """Allows you to start and end long comments like /* */ in C++

    """
    returns a new plane of size rowsxcols
    A plane is represented by a list of lists. 
    This routine marks the empty window seats as "win" and other empties as "avail"
    """
#AM - =[] assigns to an empty list
    plane = []
#AM - Iterate through the rows, and append to the empty plane list a new row consisting of ["win"]["avail"]["win"] where ["avail"] appears equal to the number of cols arguments
#AM - range() returns a sequence of numbers.  By default if only one argument it goes from 0 to rows-1 in increments of 1
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    """
Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many
    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2
    Returns: the total number of seats sold
    """
    sold = 0
    #AM-using for loop with dictionary and key/value pairs, returns sum of number of tickets sold
    for v in economy_sold.values():
        sold = sold + v
    return sold

#AM - this version is only for economy plus seating
def get_avail_seats(plane,economy_sold):
    """
    Parameters: plane : a list of lists representing plane
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned
    Returns: the number of unsold seats
    Notes: this loops over the plane and counts the number of seats that are "avail" or "win" 
           and removes the number of economy_sold seats
    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

#AM - this new function is only for economy  seating.  It is identical to the economy_plus version except that it does not subtract from the total number the number of economy because they are what matter here

def get_avail_seats_while_seating_economy(plane):
    """

    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    return avail


#AM - Returns total seats on the plane
def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

#AM - toString()
#AM - not using the special boolean test of list comrpehension - just using it as a standard for loop - so why not use another for loop?  ["%14s"%x is for formatting, adding 14 spaces before each x I believe] 
def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s

#AM- Use this when an economy seat is purchased.  name becomes the key for the dictionary economy_sold
#AM - If no more seats, return plane, but how does the programmer know that no passenger was added?  Shouldn't it return false or null?
def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])

    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane

    #AM - WAIT - So the customer buying an economy plus is given a window seat 70% of the time.  This does not make sense because if they indicate their preference we can increase the chance they will be happy!!

    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    #AM unclear what the random object is.  is random set to be a copy of plane?
    """"
    if random.randrange(100) > 30:
     # make a list of all the rows using a list comprehension
      #AM:  Looked up list comprehension - Here order is a new list that consists of all rows (I think)
    """ 
    

      # randomzie it
      #AM: shuffling order of order list - why?
      #AM:  WAIT - We can let the customer select their preference - front, back, middle, or none - first come, first served
      #random.shuffle(order)

      # go through the randomized list to see if there's an available seat
      # and if there is, assign it and return the new plane

        
        #first, check for a matching last name
    
    for col in range(len(plane[0])):
            if plane[0][col].split("_")[0] == name.split("_")[0] and plane[col][1]=="avail":
                [1][col] = name
                print("[1][col]"+name)
                return plane

            elif plane[1][col].split("_")[0] == name.split("_")[0] and plane[2][col]=="avail":
                plane[2][col] = name
                print("plane[col][2]="+name)
                return plane

            elif plane[2][col].split("_")[0] == name.split("_")[0] and plane[4][col]=="avail":
                plane[3][col] = name
                print("plane[col][3]="+name)
                return plane
            
            elif plane[3][col].split("_")[0] == name.split("_")[0] and plane[4][col]=="win":
                plane[4][col] = name
                print("[col][4]="+name)
                return plane
            else: 
                print ("_________col:"+str(col)+"key in name:"+name.split("_")[0]+"spot:"+plane[4][col].split("_")[0])
    print (">>I'm on line 163 out of first algorithm!")

        #if no match, place the person where you can   
    for col in range(len(plane[0])):
            if plane[0][col]=="win":
                plane[0][col] = name
                return plane
            elif plane[1][col]=="avail": 
                plane[1][col] = name
                return plane
            elif plane[2][col]=="avail":
                plane[2][col] = name
                return plane
            elif plane[3][col]=="avail":      
                plane[3][col] = name
                return plane
            elif plane[4][col]=="win":      
                plane[4][col] = name
                return plane
    print (">>I'm on line 183 out of second algorithm!")

""""

   #AM:  WAIT - We can take the customer's preferences into account if no match is found and go with second choice, third choice, etc. instead of random - first come, first served
    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


# THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
 #AM:  WAIT - We can use the same algorithm as we did for assigning the Economy Plus seats, but just run the Economy Plus algorithm first.
""" 
def seat_economy(plane,economy_sold,name):

  """  
  This is mostly the same as the purchase_economy_plus routine but 
  just does the random assignment. 
  We use this when we're ready to assign the economy seats after most 
  of the economy plus seats are sold
 
  """
    
    
    
  rows = len(plane)
  cols = len(plane[0])

# add code to seat all the economy_sold people
#added by AM ----------------------------------------
#AM:  IMPORTANT - for assigning the economy seats, we are no longer going to subtract the number of economy seats when checking how many seats are left.
# total unassigned seats
  seats = get_avail_seats_while_seating_economy(plane)

# exit if we have no more seats
  if seats < 1:
        print("We have no more seats:"+ str(seats)+" to be exact!")
        return plane

    #AM - WAIT - So the customer buying an economy plus is given a window seat 70% of the time.  This does not make sense because if they indicate their preference we can increase the chance they will be happy!!

    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    #AM unclear what the random object is.  is random set to be a copy of plane?
  if random.randrange(100) > 0:
        # make a list of all the rows using a list comprehension
        #AM:  Looked up list comprehension - Here order is a new list that consists of all rows (I think)
        order = [x for x in range(rows)]

        # randomzie it
        #AM: shuffling order of order list - why?
        #AM:  WAIT - We can let the customer select their preference - front, back, middle, or none - first come, first served
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                
                
                print ("seat_economy:plane[row][0]==win....and here's what the plane looks like now:")
                print(get_plane_string(plane))
                print ("<Hit enter.>")
                delay=input()
                
                
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name

                print ("seat_economy:plane[row][len(plane[0])-1]==win, total....and here's what the plane looks like now:")
                print(get_plane_string(plane))
                print ("<Hit enter.>")
                delay=input()
                return  plane

   #AM:  WAIT - We can take the customer's preferences into account if no match is found and go with second choice, third choice, etc. instead of random - first come, first served
    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
  found_seat = False
  while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True

  print ("plane[r_row][r_col]==win or avail....and here's what the plane looks like now:")
  print(get_plane_string(plane))
  print ("<Hit enter.>")
  delay=input()


  #END added by AM  ----------------------------------------


    
    
  return plane


#AM-So whenever seats are purchased, the plane and the dictionary are updated.  The plane indicates the location of the seat, and the dictionary indicates the name (key) and number sold
def purchase_economy_block(plane,economy_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary
    """
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_economy_sold(economy_sold)

#AM- Let's say there are 5 seats available and a request for 5 seats sold, so the if evaluates to true.  In that case, the dictionary is updated for that user with that number of seats.  There is no indication of a failure on short seats, however.
    if seats_avail >= number:
        economy_sold[name]=number
    return economy_sold

#AM - OK, so every passenger is either economy plus or economy.  What is the significance of the number?
def fill_plane(plane, economy_sold):
    """
    Params: plane - a list of lists representing a plane
    comments interspersed in the code
    """

    
   

    total_seats = get_total_seats(plane)
    
    print(">>Call: get_total_seats(plane)"+str(total_seats))


    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    u_number=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

#AM The max family size is 3
#70% chance of...?
    max_family_size = 3
    for key in economy_sold.keys():
      loopVar=0
      while (loopVar<economy_sold[key]):
        print("key:"+str(key)+", value: "+str(economy_sold[key])+"loopVar:"+str(loopVar))
        
        plane = purchase_economy_plus(plane,economy_sold,str(key)+"_"+str(loopVar))
        loopVar=loopVar+1
        print(">>Current State:  key="+key+", value="+str(economy_sold[key])+", loopVar="+str(loopVar))
        #plane[0][0]="Demo_2"
        #print("plane[0][0]="+plane[0][0])
        #print("(plane[0][0].split(_))[0]="+(plane[0][0].split("_"))[0])
        """"
        r = random.randrange(100)
        if r > 30:
            plane = purchase_economy_plus(plane,economy_sold,(str(ep_number)+"ep"+key))
            ep_number = ep_number + 1
            #total_seats = get_avail_seats(plane,economy_sold)

            print (">>Call:  plane=purchase_economy_plus(plane, economy_sold, ep_number) total seats:"+ str(total_seats)+"....and here's what the plane looks like now:")
            print(get_plane_string(plane))
            print ("<Hit enter.>")
            delay=input()

        """

        
    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section
    
    """
    for name in economy_sold.keys():
        for i in range(economy_sold[name]):
            print (">>Call:  seat_economy")
            plane = seat_economy(plane,economy_sold,name)
    """

    return plane
    
    
    
def main():
    
 
    
    
    
    
    print ("Ethical Airlines\n")
    print("Created by Alex Moore")
    print("Hunter College - Spring 2021")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print("Welcome to Ethical Airlines!  You'll love the way our algorithm makes you fly.\n")
    print ("                                       ")
    print ("      /                  \\                 ")
    print ("     /                    \\                ")
    print ("    /                      \\               ")
    print ("         ^             ^                 ")
    print ("         v             v                 ")
    print ("                 ^                             ")
    print ("                                       ")
    print ("     ----                   ---               ")
    print ("         \\-----------------/                              ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("<Hit enter.>")
    delay=input()


    print("First, we'd like to welcome our families.  Let's break out our dictionary and see who the families are and how many tickets they bought!\n")

   #AM- Family name key/value pairs - if more time, would be defined locally instead of globally
    economy_sold={
   
    "Bradbury": 2,
    "Pynchon": 3,
    "Shakespeare": 4,
    "Baldwin": 2,
    "Kramer": 3,
    "Bozzano": 5,
    "Rudolph": 6,
    "Allen": 1,
    "Capulet": 4,
    "Salinger": 3,
    "Lynch": 3,
    "Holmes":2,
    "Matute":2,
    "Borges":5,
    "Morrison":1
    }

    print (">>Call: family_print(economy_sold)")
    family_print(economy_sold)
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("                                       ")
    print ("<Hit enter.>")
    delay=input()

    print (">>Call: create_plane(10,5)")
    plane = create_plane(10,5)

    print ("<Hit enter.>")
    delay=input()

    print (">>Call: get_plane_string(plane)")
    print(get_plane_string(plane))
    print ("<Hit enter.>")
    delay=input()

    print (">>Call: fill_plane(plane, economy_sold)")
    plane = fill_plane(plane,economy_sold)
    print ("<Hit enter.>")
    delay=input()

    print(">>Call: get_plane_string(plane)")
    print(get_plane_string(plane))
    print ("<Hit enter.>")
    delay=input()

if __name__=="__main__":
    main()