#!/usr/bin/env python

import pyprel as pyprel

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

    pyprel.printLine()
    pyprel.printDictionary(dictionary = information)
    pyprel.printLine()
    print(pyprel.dictionaryString(dictionary = information))
    pyprel.printLine()

    print("\nexample: printout of existing logo")
    raw_input("Press Enter to continue.")

    text = (
    "   ____      _            _____ _                \n"
    "  / ___|___ | | ___  _ __|  ___| | _____      __ \n"
    " | |   / _ \| |/ _ \| '__| |_  | |/ _ \ \ /\ / / \n"
    " | |__| (_) | | (_) | |  |  _| | | (_) \ V  V /  \n"
    "  \____\___/|_|\___/|_|  |_|   |_|\___/ \_/\_/   "
    )

    pyprel.printCenter(text = text)

    print("\nexample: rendering and printout of logo")
    raw_input("Press Enter to continue.")

    name = "aria"
    logo = pyprel.renderBanner(
        text = name.upper()
    )
    pyprel.printLine()
    print(pyprel.centerString(text = logo))
    pyprel.printLine()

    print("\nexample: rendering and printout segment display")
    raw_input("Press Enter to continue.")

    print(pyprel.renderSegmentDisplay(text = "0123456789"))

if __name__ == '__main__':
    main()
