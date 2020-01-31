# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:21:26 2020

@author: Luca
"""
import os
import time

def display_array(ar):
    "clear the screen, display the contents of an array, wait for 1 sec"
    os.system('clear')
    
    rows = len(ar)    # grab the rows
    
    if rows == 0:
        raise ValueError("Array contains no data")
        
    cols = len(ar[0])  # grab the columns - indices start at 0!
    
    for i in range(rows):
        for j in range(cols):
            print(ar[i][j],end=' ')  # no carriage return, space separated
        print()
        
    time.sleep(1)
        
##############################################################################

ar = [[1,2,3],
      [4,5,6],
      [7,8,9]]

display_array(ar)

##############################################################################

board = [[' ','*',' '],
         ['*',' ','*'],
         [' ','*',' ']]

display_array(board)