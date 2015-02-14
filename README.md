# pyprel

Python print elegant

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

# prerequisites

## pyfiglet

    sudo pip install pyfiglet
