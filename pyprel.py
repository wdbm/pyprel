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

version = "2015-03-03T1703Z"

import subprocess
import textwrap
import pyfiglet

def terminalWidth():
    return(
        int(
            subprocess.Popen(
                ["tput", "cols"],
                stdout = subprocess.PIPE
            ).communicate()[0].decode("utf-8").strip("\n")
        )
    )

def centerString(
    text = None
    ):
    textList = text.splitlines()
    _terminalWidth = terminalWidth()
    newText = ""
    for line in textList:
        widthOfText = len(line)
        paddingTotal = _terminalWidth - widthOfText
        paddingLeft = int(paddingTotal/2)
        paddingRight = paddingTotal - paddingLeft
        newText = newText + paddingLeft * " " + line + paddingRight * " " + "\n"
    return(newText)

def printCenter(
    text = None
    ):
    print(centerString(text = text))

def dictionaryString(
    dictionary  = None,
    indentation = ""
    ):
    string = ""
    for key, value in dictionary.iteritems():
        if isinstance(value, dict):
            string += "\n{indentation}{key}:".format(
                indentation = indentation,
                key         = key
            )
            string += dictionaryString(
                dictionary  = value,
                indentation = indentation + "  "
            )
        else:
            string += "\n" + indentation + "{key}: {value}".format(
                key   = key,
                value = value
            )
    return(string)

def printDictionary(
    dictionary  = None,
    indentation = ""
    ):
    print(dictionaryString(
        dictionary  = dictionary,
        indentation = ""
    ))

def lineString(
    character = "-"
    ):
    _terminalWidth = terminalWidth()
    line = ""
    for column in range(0, _terminalWidth):
        line += character
    return(line)

def printLine(
    character = "-"
    ):
    print(lineString(
        character = character
    ))

def renderBanner(
    text = None,
    font = "slant"
    ):
    return(pyfiglet.Figlet(font = font).renderText(text))

def renderSegmentDisplay(
    text = None
    ):
    segments = (
        {
            ' _ ': '02356789',
            '   ': '14'
        },
        {
            '| |': '0',
            '  |': '17',
            ' _|': '23',
            '|_|': '489',
            '|_ ': '56'
        },
        {
            '|_|': '068',
            '  |':'147',
            '|_ ': '2',
            ' _|':'359'
        }
    )
    segmentDisplayRender = ""
    for row in range(3):
        for character in text:
            for leds, digits in segments[row].items():
                if character in digits:
                    segmentDisplayRender = segmentDisplayRender + leds
        segmentDisplayRender = segmentDisplayRender + "\n"
    return(segmentDisplayRender)

class Table:

    def __init__(
        self,
        contents                 = None,
        columnWidth              = None,
        tableWidthRequested      = None,
        hardWrapping             = False,
        columnDelimiter          = "|",
        rowDelimiter             = "-"
        ):
        self.contents            = contents
        self.columnWidth         = columnWidth
        self.tableWidthRequested = tableWidthRequested
        self.columnDelimiter     = columnDelimiter
        self.hardWrapping        = hardWrapping
        self.numberOfColumns = len(contents[0])
        # Resolve the table dimensions.
        # If a column width is specified, that is given precidence. If a table
        # width is requested, a reasonable column width is derived from it. If
        # no column width is specified and no table width is requested, the
        # requested table width is set to the terminal width.
        if self.columnWidth is None:
            if self.tableWidthRequested is None:
                self.tableWidthRequested = terminalWidth()
            self.columnWidth = (
                self.tableWidthRequested -\
                (self.numberOfColumns + 1) * len(self.columnDelimiter)
            ) / self.numberOfColumns
        # line gets too long for one concatenation
        self.rowDelimiter = self.columnDelimiter
        self.rowDelimiter +=\
            rowDelimiter * (
                self.columnWidth * max([len(i) for i in self.contents]) +\
                (self.numberOfColumns - 1) * len(self.columnDelimiter)
            )
        self.rowDelimiter +=\
            self.columnDelimiter + "\n"

    def wrapSoft(self):
        # Wrap text regarding word boundaries.
        tableString = self.rowDelimiter
        # Restructure the table contents to get soft wrapped content for each
        # cell.
        contentsWrapped = [
            [
                textwrap.wrap(column, self.columnWidth) for column in row
            ] for row in self.contents
        ]
        for row in contentsWrapped:
            for n in range(max([len(i) for i in row])):
                tableString += self.columnDelimiter
                for column in row:
                    if n < len(column):
                        tableString += column[n].ljust(self.columnWidth)
                    else:
                        tableString += " " * self.columnWidth
                    tableString += self.columnDelimiter
                tableString += "\n"
            tableString += self.rowDelimiter
        return(tableString)

    def wrapHard(self):
        # Wrap text disregarding word boundaries.
        tableString = self.rowDelimiter
        for row in self.contents:
            maxWrap = (max([len(i) for i in row]) // self.columnWidth) + 1
            for r in range(maxWrap):
                tableString += self.columnDelimiter
                for column in row:
                    start = r * self.columnWidth
                    end = (r + 1) * self.columnWidth 
                    tableString +=\
                        column[start:end].ljust(self.columnWidth) +\
                        self.columnDelimiter
                tableString += "\n"
            tableString += self.rowDelimiter
        return(tableString)

    def __str__(self):
        if self.hardWrapping is True:
            return self.wrapHard()
        else:
            return self.wrapSoft()
