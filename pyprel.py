################################################################################
#                                                                              #
# pyprel                                                                       #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program provides elegant printing utilities in Python.                  #
#                                                                              #
# copyright (C) 2014 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

version = "2014-11-17T2008Z"

import subprocess
import pyfiglet as pyfiglet

def centerString(
    text = None
    ):
    textList = text.splitlines()
    terminalWidth = int(
        subprocess.Popen(
            ['tput', 'cols'],
            stdout = subprocess.PIPE
        ).communicate()[0].decode('utf-8').strip('\n')
    )
    newText = ""
    for line in textList:
        widthOfText = len(line)
        paddingTotal = terminalWidth - widthOfText
        paddingLeft = int(paddingTotal/2)
        paddingRight = paddingTotal - paddingLeft
        newText = newText + paddingLeft * " " + line + paddingRight * " " + "\n"
    return(newText)

def printCenter(
    text = None
    ):
    print(centerString(text = text))

def printDictionary(
    dictionary = None,
    indentation = ''
    ):
    for key, value in dictionary.iteritems():
        if isinstance(value, dict):
            print("{indentation}{key}:".format(
            indentation = indentation,
            key = key
        ))
            printDictionary(
                dictionary = value,
                indentation = indentation + '   '
            )
        else:
            print(indentation + "{key}: {value}".format(
                key = key,
                value = value
            ))

def printLine(
    character = '-'
    ):
    terminalWidth = int(
        subprocess.Popen(
            ['tput', 'cols'],
            stdout = subprocess.PIPE
        ).communicate()[0].decode('utf-8').strip('\n')
    )
    line = ""
    for column in range(0, terminalWidth):
        line += character
    print(line)

def renderBanner(
    text = None,
    font = "slant"
    ):
    return(pyfiglet.Figlet(font = font).renderText(text))
