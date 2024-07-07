#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getRegistrationStatus' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. INTEGER k
#

def getRegistrationStatus(passwords, k):
    return evaluatePasswords(passwords, k)

def evaluatePasswords(ACCEPT, REJECT, passwords, k):
    for index in range(len(passwords)):
        if(passwords[index] != ACCEPT and passwords[index] != REJECT):
            password = passwords[index]
            repeated_passwords = 0
            rejectOrAcceptAllWithPassword(passwords, k, password, repeated_passwords)
            

def rejectOrAcceptAllWithPassword(passwords, k, password, repeated_passwords):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"
    for i in range(len(passwords)):
                    if password == passwords[i] and k > repeated_passwords:
                        passwords[i] = ACCEPT
                        repeated_passwords += 1

                    elif password == passwords[i]:
                        passwords[i] = REJECT
                        repeated_passwords += 1

    return passwords

if __name__ == '__main__':
    result = getRegistrationStatus(["Maria", "Maria", "Maria","Maria", "Maria", "Maria", "Juan", "Jose", "Jose", "Jose","Juan", "Jose", "Jose", "Jose", "Juan", "Juan", "Juan", "Juan"], 2)
    #Output: ACCEPT, ACCEPT, REJECT, REJECT, REJECT, REJECT,ACCEPT,ACCEPT,ACCEPT,REJECT