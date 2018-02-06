# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:55:56 2018

@author: Masaya

BlockThing: Creates a data structure representing sensors/actuators (Things) and assigns them to Multicast Groups.
>Multicast Groups are represented as tuple in self.group
>can use socket.bind(thing.group) for address binding
"""

class BlockThing:
    def __init__(self, multicastIP = '0.0.0.0', multicastPort = 8888, name = "Jon", key = 1010):
        portLen = len(str(multicastPort))
        if portLen != 4:
            print("Invalid port length: " + str(portLen) + ". Port must be exactly four (4) digits.")
            return
        else:
            self.name = str(name)
            self.ip = multicastIP
            self.port = multicastPort
            #TO DO: Generate key hashing function based on name
            self.key = key
            #Redundancy as a Tuple
            self.group = (str(self.ip), self.port)
        print("Thing '" + self.name + "' created with multicast group " + 
              str(self.group) + " with key " +str(key) + ".")

##Test Functions
Test1 = BlockThing('0.0.0.0', 4579, "Ocelot")
Test4 = BlockThing('1234.56.192.58', 1234, "Jonathan")
Test5 = BlockThing()