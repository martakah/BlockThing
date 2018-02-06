# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:08:02 2018

@author: Masaya
"""

class BlockNode:
    def __init__(self, multicastIP = '0.0.0.0', multicastPort = 8888, name = "Jon", key = 1110110):
        self.ip = multicastIP
        self.port = multicastPort
        self.name = name
        self.key = key
        
        #Represent Things list as hash table for scaling
        self.devices = {}
        self.keyValue = {}