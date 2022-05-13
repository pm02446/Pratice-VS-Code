# Global Scope, a variable that is accesed by everyone
x = 300

# Local Scope is variable only avalibae within a funcion 
def localScope ():
    x = 200
# you a Global and Local variable have the same name, they are treated differently

# the "global" keyword allows a global variable to be created within a function
# you can also change a global varibale with the keyword "global"

x = 300

def myfunc ():
    global x
    x = 200
myfunc()
print(x)