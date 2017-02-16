#!/usr/bin/env python

import pyprel

def main():

    print("\nexample: printout of dictionary")
    raw_input("Press Enter to continue.")

    information = {
        "sample information": {
            "ID": 169888,
            "name": "ttH",
            "number of events": 124883,
            "cross section": 0.055519,
            "k factor": 1.0201,
            "generator": "pythia8",
            "variables": {
                "trk_n": 147,
                "zappo_n": 9001
            }
        }
    }

    pyprel.print_line()
    pyprel.print_dictionary(dictionary = information)
    pyprel.print_line()
    print(pyprel.dictionary_string(dictionary = information))
    pyprel.print_line()

    print("\nexample: printout of existing logo")
    raw_input("Press Enter to continue.")

    text = (
    "   ____      _            _____ _                \n"
    "  / ___|___ | | ___  _ __|  ___| | _____      __ \n"
    " | |   / _ \| |/ _ \| '__| |_  | |/ _ \ \ /\ / / \n"
    " | |__| (_) | | (_) | |  |  _| | | (_) \ V  V /  \n"
    "  \____\___/|_|\___/|_|  |_|   |_|\___/ \_/\_/   "
    )

    pyprel.print_center(text = text)

    print("\nexample: rendering and printout of logo")
    raw_input("Press Enter to continue.")

    name = "aria"
    logo = pyprel.render_banner(
        text = name.upper()
    )
    pyprel.print_line()
    print(pyprel.center_string(text = logo))
    pyprel.print_line()

    print("\nexample: rendering and printout segment display")
    raw_input("Press Enter to continue.")

    print(pyprel.render_segment_display(text = "0123456789"))

    print("\nexample: printout of tables")
    raw_input("Press Enter to continue.")

    table_contents = [
        ["heading 1", "heading 2"],
        ["some text", "some more text"],
        ["lots and lots and lots and lots and lots of text", "some more text"]
    ]
    print(
        pyprel.Table(
            contents = table_contents,
            column_width = 25
        )
    )
    print(
        pyprel.Table(
            contents = table_contents,
            table_width_requested = 30
        )
    )
    print(
        pyprel.Table(
            contents = table_contents,
            table_width_requested = 30,
            hard_wrapping = True
        )
    )
    print(
        pyprel.Table(
            contents = table_contents
        )
    )
    pyprel.print_center(
        text = pyprel.Table(
            contents = table_contents,
            table_width_requested = 30
        ).__str__()
    )
    print(
        pyprel.Table(
            contents = table_contents,
            column_width = 25,
            column_delimiter = "||"
        )
    )
    print(
        pyprel.Table(
            contents = table_contents,
            column_width = 25,
            row_delimiter = "~"
        )
    )
    table_contents = [
        [
            "heading 1",
            "heading 2",
            "heading 3"
        ],
        [
            "some text",
            "some more text",
            "even more text"
        ],
        [
            "lots and lots and lots and lots and lots of text",
            "some more text",
            "some more text"
        ]
    ]
    print(
        pyprel.Table(
            contents = table_contents
        )
    )
    table_contents = [
        [
            "heading 1",
            "heading 2",
            "heading 3",
            "heading 4"
        ],
        [
            "some text",
            "some more text",
            "even more text",
            "yeah more text"
        ],
        [
            "lots and lots and lots and lots and lots of text",
            "some more text",
            "some more text",
            "some more text"
        ]
    ]
    print(
        pyprel.Table(
            contents = table_contents
        )
    )

if __name__ == '__main__':
    main()
