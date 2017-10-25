# -*- coding: utf-8 -*-

#from Coin import Coin
# we don't know the name of the classes in advance, so we can't use this
# instead,
#Coin = __import__("Coin", globals(), locals(), ["Coin"], -1).Coin

import os

plugin = {}

for fileName in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    print fileName
    if fileName.endswith('.py') and fileName != __file__:
        p = fileName[:fileName.index('.')]
        print '└─importing ' + p
        exec('plugin[p] = __import__(p, globals(), locals(), [p], -1).'+p)
print '\nDone importing!\n'

coin = plugin['Coin'](1)
print coin.value
