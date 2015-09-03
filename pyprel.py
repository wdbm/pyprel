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
# copyright (C) 2014 2015 William Breaden Madden                               #
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

version = "2015-09-03T1620Z"

import subprocess
import textwrap

def smuggle(
    moduleName = None,
    URL        = None
    ):
    if moduleName is None:
        moduleName = URL
    try:
        module = __import__(moduleName)
        return(module)
    except:
        try:
            moduleString = urllib.urlopen(URL).read()
            module = imp.new_module("module")
            exec moduleString in module.__dict__
            return(module)
        except: 
            raise(
                Exception(
                    "module {moduleName} import error".format(
                        moduleName = moduleName
                    )
                )
            )
            sys.exit()

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
    pyfiglet = smuggle(moduleName = "pyfiglet")
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

def clamp(x): 
    return(max(0, min(x, 255)))

def RGB_to_HEX(RGB_tuple):
    # This function returns a HEX string given an RGB tuple.
    r = RGB_tuple[0]
    g = RGB_tuple[1]
    b = RGB_tuple[2]
    return "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))

def HEX_to_RGB(HEX_string):
    # This function returns an RGB tuple given a HEX string.
    HEX = HEX_string.lstrip('#')
    HEX_length = len(HEX)
    return tuple(
        int(HEX[i:i + HEX_length // 3], 16) for i in range(
            0,
            HEX_length,
            HEX_length // 3
        )
    )

def mean_color(colorsInHEX):
    # This function returns a HEX string that represents the mean color of a
    # list of colors represented by HEX strings.
    colorsInRGB = []
    for colorInHEX in colorsInHEX:
        colorsInRGB.append(HEX_to_RGB(colorInHEX))
    sum_r = 0
    sum_g = 0
    sum_b = 0
    for colorInRGB in colorsInRGB:
        sum_r += colorInRGB[0]
        sum_g += colorInRGB[1]
        sum_b += colorInRGB[2]
    mean_r = sum_r / len(colorsInRGB)
    mean_g = sum_g / len(colorsInRGB)
    mean_b = sum_b / len(colorsInRGB)
    return RGB_to_HEX((mean_r, mean_g, mean_b))

def extend_palette(
    colors = None, # list of HEX string colors
    minimumNumberOfColorsNeeded = 15
    ):
    while len(colors) < minimumNumberOfColorsNeeded:
        for index in range(1, len(colors), 2):
            colors.insert(index, mean_color([colors[index - 1], colors[index]]))
    return colors

def save_image_of_palette(
    colors   = None, # list of HEX string colors
    filename = "palette.png"
    ):
    import numpy
    import Image
    scale_x = 200
    scale_y = 124
    data = numpy.zeros((1, len(colors), 3), dtype = numpy.uint8)
    index = -1
    for color in colors:
        index += 1
        color_RGB = HEX_to_RGB(color)
        data[0, index] = [color_RGB[0], color_RGB[1], color_RGB[2]]
    data = numpy.repeat(data, scale_x, axis=0)
    data = numpy.repeat(data, scale_y, axis=1)
    image = Image.fromarray(data)
    image.save(filename)

# Define color palettes.
# primary colors for white background
palette1 = [
    "#fc0000",
    "#ffae3a",
    "#00ac00",
    "#6665ec",
    "#a9a9a9",
]
# ATLAS clarity
palette2 = [
    "#FEFEFE",
    "#AACCFF",
    "#649800",
    "#9A33CC",
    "#EE2200",
]
# ATLAS primary colors
palette3 = [
    "#005CFF",
    "#FFBF00",
    "#14B814",
    "#FF0000",
    "#00FFFF",
]
# grayscale
palette4 = [
    "#E8E9EC",
    "#A7AEB6",
    "#6A747F",
    "#383D43",
    "#2A2C30",
]
# dusk
palette5 = [
    "#F1E1BD",
    "#EEBA85",
    "#E18D76",
    "#9C837E",
    "#5B7887",
]
# sunset
palette6 = [
    "#ED4964",
    "#F69092",
    "#CC3075",
    "#5B217B",
    "#441D54",
]
# burnt
palette7 = [
    "#000000",
    "#472718",
    "#EB5656",
    "#ECA558",
    "#F2D773",
]
# high contrast
palette8 = [
    "#140E11",
    "#873387",
    "#41C6D7",
    "#ECD03E",
    "#FEEAC6",
]
palettes = []
palettes.append(palette1)
palettes.append(palette2)
palettes.append(palette3)
palettes.append(palette4)
palettes.append(palette5)
palettes.append(palette6)
palettes.append(palette7)
palettes.append(palette8)

def save_images_of_palettes():
    for index, palette in enumerate(palettes):
        save_image_of_palette(
            colors = palette,
            filename = "palette_{index}.png".format(index = index + 1)
        )
