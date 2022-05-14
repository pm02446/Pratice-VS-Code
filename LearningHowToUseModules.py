import randomModule

#module_name.function_name is the syntax
randomModule.greeting("Pedro")

a = randomModule.person1["car"]

# you can re-name a module with an alias with "as"
# import module as k

#dir() list all the function and variable names in a module
x = dir(randomModule)
#print(x)

# to only import certain things form modules
# When importing using the from keyword, 
# do not use the module name when referring to elements in the module.
# from module import what_I_want
# what_I_want() not module.what_I_want()