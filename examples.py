#!/usr/bin/env python

import pyprel as pyprel

def main():

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

    text = (
    "   ____      _            _____ _                \n"
    "  / ___|___ | | ___  _ __|  ___| | _____      __ \n"
    " | |   / _ \| |/ _ \| '__| |_  | |/ _ \ \ /\ / / \n"
    " | |__| (_) | | (_) | |  |  _| | | (_) \ V  V /  \n"
    "  \____\___/|_|\___/|_|  |_|   |_|\___/ \_/\_/   "
    )

    pyprel.printCenter(text = text)

if __name__ == '__main__':
    main()
