#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# pyprel_examples_database                                                     #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is pyprel database examples.                                    #
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

usage:
    program [options]

options:
    -h, --help       display help message
    --version        display version and exit
    --database=FILE  database            [default: database.db]
    --table=NAME     database table name [default: users]
"""

name    = "pyprel_examples_database"
version = "2017-02-16T1356Z"

import docopt
import os
import uuid

import dataset
import pyprel

def main(options):

    filename_database = options["--database"]
    name_table        = options["--table"]

    print("\npyprel database examples\n")

    if os.path.exists(filename_database):
        print("create database {database}".format(
            database = filename_database
        ))
        create_database(filename = "database.db")

    print("access database {filename}".format(
        filename = filename_database
    ))
    database = dataset.connect(
        "sqlite:///{filename_database}".format(
            filename_database = filename_database
        )
    )
    table = database[name_table]

    print("add data to database")
    table.insert(dict(
        name     = "Legolas Greenleaf",
        age      = 2000,
        country  = "Mirkwood",
        uuid4    = str(uuid.uuid4())
    ))
    table.insert(dict(
        name     = "Cody Rapol",
        age      = 30,
        country  = "USA",
        activity = "DDR",
        uuid4    = str(uuid.uuid4())
    ))

    print(
"""
database tables:\n{tables}
\ntable {table} columns:\n{columns}
\ntable {table} row one:\n{row}
""".format(
            tables  = database.tables,
            table   = name_table,
            columns = database[name_table].columns,
            row     = [entry for entry in table.find(id = "1")]
        )
    )

    print("table {table} printout:\n".format(
        table = name_table
    ))

    print(
        pyprel.Table(
            contents = pyprel.table_dataset_database_table(
                table = database[name_table]
            )
        )
    )

def create_database(
    filename = None
    ):
    os.system(
        "sqlite3 " + \
        filename   + \
        " \"create table aTable(field1 int); drop table aTable;\""
    )

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
