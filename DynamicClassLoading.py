# -*- coding: utf-8 -*-

#from Coin import Coin
# we don't know the name of the classes in advance, so we can't use this

import os, importlib

plugin = {}

for fileName in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    print fileName
    if fileName.endswith('.py') and fileName != os.path.basename(__file__):
        p = fileName.rsplit('.')[0]
        print '└─importing ' + p
        plugin[p] = getattr(importlib.import_module(p), p)
print '\nDone importing!\n'

coin = plugin['Coin'](1)
print coin.value
