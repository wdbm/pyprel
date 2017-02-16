#!/usr/bin/env python

import pyprel

def main():

    pyprel.print_line()

    print("\nexample: accessing a palette and extending it\n")
    palette_name = "palette1"
    print("access palette {name}".format(name = palette_name))
    palette = pyprel.access_palette(name = palette_name)
    print("palette colors default: {colors}".format(colors = palette))
    minimum_number_of_colors_needed = 3
    print(
        "extend palette to ensure that it has at least {number} colors".format(
            number = minimum_number_of_colors_needed
    ))
    palette.extend_palette(
        minimum_number_of_colors_needed = minimum_number_of_colors_needed
    )
    print("palette colors: {colors}".format(colors = palette))
    minimum_number_of_colors_needed = 20
    print(
        "extend palette to ensure that it has at least {number} colors".format(
            number = minimum_number_of_colors_needed
    ))
    palette.extend_palette(
        minimum_number_of_colors_needed = minimum_number_of_colors_needed
    )
    print("palette colors: {colors}".format(colors = palette))

    pyprel.print_line()

if __name__ == '__main__':
    main()
