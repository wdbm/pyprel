#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# examples_tables                                                              #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is pyprel tables examples.                                      #
#                                                                              #
# copyright (C) 2016 William Breaden Madden                                    #
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
"""

name    = "examples_tables"
version = "2018-09-06T1743Z"

import numpy
import pyprel

def main():

    pyprel.print_line()

    print("\nconvert Markdown table to pyprel table\n")

    table_Markdown = """
|**variable 1**|**variable 2**|
|--------------|--------------|
|1             |0.23545       |
|2             |0.63523       |
|3             |0.55231       |
|4             |0.89563       |
|5             |0.55345       |
"""

    table_contents = pyprel.table_Markdown_to_table_pyprel(
        table = table_Markdown
    )

    print(
        pyprel.Table(
            contents = table_contents,
        )
    )

    pyprel.print_line()

    print("\ncompose and print table\n")
    
    table_contents = [
        [
            "number",
            "letter"
        ],
        [
            1,
            "a"
        ],
        [
            2,
            "b"
        ]
    ]
    print(
        pyprel.Table(
            contents = table_contents
        )
    )

    pyprel.print_line()

    print("\ncompose and print a table using list comprehensions and zip\n")

    data_x = numpy.linspace(0, numpy.pi, 10)
    data_y = [numpy.sin(x) for x in data_x]

    print(pyprel.Table(
        contents = [["x", "y"]] + [[x, y] for x, y in zip(data_x, data_y)]
    ))

    pyprel.print_line()

    print("\ncompose aligned printouts of data using tables\n")

    table_contents = [
        ["msg:"      , "1536155474294"],
        ["signature:", "0C118313F6D19"],
        ["data:"     , "1536155474294"]
    ]
    print(pyprel.Table(
        contents              = table_contents,
        column_delimiter      = "",
        row_delimiter         = "",
        table_width_requested = 40
    ))

    table_contents = [
        ["msg:"      , "15361554742941536155474294153615547429415361554742941536155474294"],
        ["signature:", "0C118313F6D190C118313F6D190C118313F6D190C118313F6D190C118313F6D19"],
        ["data:"     , "15361554742941536155474294153615547429415361554742941536155474294"]
    ]
    print(pyprel.Table(
        contents              = table_contents,
        column_delimiter      = "",
        row_delimiter         = "",
        table_width_requested = 40
    ))

    pyprel.print_line()

if __name__ == "__main__":
    main()
