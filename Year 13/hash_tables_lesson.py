#Creating a hash table

# Task - Modify the code and use chaining

# Sirs code to use for an example:
'''
hash a value and place the data in a specific position in an array/list
if occupied, rehash to next position and repeat
'''

student_names = [None]*10  ## an array that has 10 spaces set to None

def hash_name(name):

    hash_total = 0
    for char in name:  ## Loop goes through each character in the string name
        hash_total += ord(char)  ## 'ord(char) is a built-in function that returns the ASCII integer value of that character, so each of those totals are added to hash_total
    #end for   ## hash_total now holds the total of ASCII integer values of the name entered

    # mod for position
    hash_position = hash_total % len(student_names)  ## % is modulus operator and is used to ensure that the name fits in the list  

    num_attempts = len(student_names) ## will be used to set a limit on how many times the code can try to find a place,  prevents an infinite loop if full

    placed = False
    while (not placed) and (num_attempts) > 0:
        
        # check if space occupied
        if student_names[hash_position] == None:
            placed = True
        else: 

            print(f"Position {hash_position} already occupied")

            ## handles linear probing, moves to nect space to check, if end of list is reached, wraps around to the start (ensures all positions get checked if needed)
            if hash_position == len(student_names) - 1:
                hash_position = 0
            else:
                hash_position += 1
            #end if
            num_attempts -=1  ## reduces number of remaining attempts

        #end if 

    #end while

    return hash_position, num_attempts

#end def

# main here

def main():

    exit = False
    while not exit:

        name = input("First Name > ").lower().strip()
        if name == "":
            print("Try again")
        else:
            hash_position, rehashes = hash_name(name)
            print(hash_position, rehashes)

            if student_names[hash_position] == None:
                student_names[hash_position] = name
            else:
                if rehashes == 0:
                    print("Could not place, array is full..exiting")
                    exit = True
                else:
                    print(hash_position)
                #end if
        #endif

    #end while

#end def

if __name__ == "__main__":
    main()