#from Coin import Coin
#we don't know the name of the classes in advance, so we can't use this
#btw, why the from Coin part? why not just import coin?

#"Direct use of __import__() is rare, except in cases where you want to import a module whose name is only known at runtime."
#https://docs.python.org/2/library/functions.html#__import__
#perfect!

#__import__(name[, globals[, locals[, fromlist[, level]]]])

#https://www.python.org/dev/peps/pep-0008

#Coin = __import__("Coin", globals(), locals(), ["Coin"], -1).Coin

#https://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
#from os import walk
#for filenames in walk(path):

from os import listdir
from os.path import isfile, join

plugin = dict()

path = "C:\Users\hcps-tenembasj\Documents\Dynamic Class Loading"
for file in listdir(path):
    print file
    #neither __file__ nor sys.argv[0] work so hardcoding it 4naw
    if isfile(join(path,file)) and file.endswith(".py") and file != "DynamicClassLoading.py": #is not will not work
        print "  importing"
        #file[:-3] lol face
        plugin[file[:-3]] = __import__(file[:-3], globals(), locals(), [file[:-3]], -1).Coin

coin = plugin["Coin"](1)
print coin.value
