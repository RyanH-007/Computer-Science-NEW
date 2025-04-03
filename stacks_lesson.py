'''class stack():
    max = 12
    items = ["" for index in range(max)]

    stack_pointer = -1

    
    def push(self,item):
        if self.stack_pointer < max: 
            self.stack_pointer = self.stack_pointer +1
            return item
        else:
            print("Stack OVERFLOW. The stack is a maximum capcity")
    
    def peek(self):
        if self.stack_pointer != -1:
            return self.tiems[self.stack_pointer]
        else:
            print("Stack UNDERFLOW. There is no data values in this stack.")

items = ["England", "USA", "Ireland"]

s = stack()

for index in range(0, len(items)):
    s.push(items[index])

print(s.pop())

print(s.peek())
'''

'''
procedural code snippets to simulate a stack
* check pre-conditions before push, pop or peek operations
'''


stack_pointer = -1

stack = []

a = input("Please enter a number")
print(a)

def push(item):
#My attempt

    item = a
    stack_pointer = stack_pointer + 1
    stack[stack_pointer] = item 


    pass

#end def

def pop():

    pass

#end def

def peek():

    pass

#end def

def get_item():

    valid = False
    while not valid:

        try:
            item = int(input("Enter Number > "))
            valid = True
        except ValueError:
            print("Not an integer")
        #end except

    #end while

    return item

#end def

# main
exit = False
while not exit:

    op = input("[p]ush, p[o]p, p[e]eek or e[x]it > ").lower()
    if op not in "poex":
        print("Invalid Op")
    elif op == "x":
        exit = True
    elif op == "p":
        item = get_item()
        result = push(item)
    elif op == "o":
        result = pop
    elif op == "e":
        result = peek
    #end if

#end while

print("End")

print(a)

print("Hello world")
