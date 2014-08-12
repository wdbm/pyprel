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
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

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
