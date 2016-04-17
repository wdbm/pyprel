# pyprel

Python print elegant

# setup

```Bash
sudo pip install pyprel
```

# introduction

This module provides Python rendering functionality. It can render a dictionary such that it is displayed with indentations for illustration of hierarchy:

```
sample information:
  name: ttH
  generator: pythia8
  cross section: 0.055519
  variables:
    zappo_n: 9001
    trk_n: 147
  number of events: 124883
  k factor: 1.0201
  ID: 169888
```

It can render and display logos:

```
                  ____      _            _____ _                                
                 / ___|___ | | ___  _ __|  ___| | _____      __                 
                | |   / _ \| |/ _ \| '__| |_  | |/ _ \ \ /\ / /                 
                | |__| (_) | | (_) | |  |  _| | | (_) \ V  V /                  
                 \____\___/|_|\___/|_|  |_|   |_|\___/ \_/\_/               
```

It can center blocks of text for terminal output (such as in a way shown for the logo above). It can render segment displays:

```
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
```

It can render and display tables of various specified widths and column widths with various text wrapping features and delimiters:

```
|---------------------------------------------------|
|heading 1                |heading 2                |
|---------------------------------------------------|
|some text                |some more text           |
|---------------------------------------------------|
|lots and lots and lots   |some more text           |
|and lots and lots of text|                         |
|---------------------------------------------------|
```

```
                         |---------------------------|                          
                         |heading 1    |heading 2    |                          
                         |---------------------------|                          
                         |some text    |some more    |                          
                         |             |text         |                          
                         |---------------------------|                          
                         |lots and lots|some more    |                          
                         |and lots and |text         |                          
                         |lots and lots|             |                          
                         |of text      |             |                          
                         |---------------------------|                         
```

```
||----------------------------------------------------||
||heading 1                ||heading 2                ||
||----------------------------------------------------||
||some text                ||some more text           ||
||----------------------------------------------------||
||lots and lots and lots   ||some more text           ||
||and lots and lots of text||                         ||
||----------------------------------------------------||
```

```
|-----------------------------------------------------------------------------|
|heading 1                |heading 2                |heading 3                |
|-----------------------------------------------------------------------------|
|some text                |some more text           |even more text           |
|-----------------------------------------------------------------------------|
|lots and lots and lots   |some more text           |some more text           |
|and lots and lots of text|                         |                         |
|-----------------------------------------------------------------------------|
```

```
|---------------------------------------------------------------------------|
|heading 1         |heading 2         |heading 3         |heading 4         |
|---------------------------------------------------------------------------|
|some text         |some more text    |even more text    |yeah more text    |
|---------------------------------------------------------------------------|
|lots and lots and |some more text    |some more text    |some more text    |
|lots and lots and |                  |                  |                  |
|lots of text      |                  |                  |                  |
|---------------------------------------------------------------------------|
```

It can provide color palettes, extend them and save images of them. Color palettes available can be viewed by saving images of them:

```Python
pyprel.save_images_of_palettes()
```

A palette can be loaded using its name:

```Python
pyprel.access_palette(name = "palette1")
```

A palette of colors can be extended to a required number of colors:

```Python
colors_1_extended = extend_palette(
    colors                          = colors_1,
    minimum_number_of_colors_needed = 15
)
```

# references

- C. A. Brewer, M. Harrower ColorBrewer.org: An Online Tool for Selecting Colour Schemes for Maps, The Cartographic Journal, 40 (1), 27--37 (01 June 2003)

# palettes

![](images/palette_1.png)
![](images/palette_2.png)
![](images/palette_3.png)
![](images/palette_4.png)
![](images/palette_5.png)
![](images/palette_6.png)
![](images/palette_7.png)
![](images/palette_8.png)
![](images/palette_9.png)
![](images/palette_10.png)
![](images/palette_11.png)
![](images/palette_12.png)
![](images/palette_13.png)
![](images/palette_14.png)
![](images/palette_15.png)
![](images/palette_16.png)
![](images/palette_17.png)
![](images/palette_18.png)
![](images/palette_19.png)
![](images/palette_20.png)
![](images/palette_21.png)
![](images/palette_22.png)
