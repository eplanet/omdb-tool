# omdb-tool
Interactive command-line omdb api tool using Python

## Required packages
The package python3 is the only one needed. You might want to use virtualenv as well, while it is not necessary.

## Usage
```bash
pip3 install .
omdb-tool -a API_KEY
```

The tool asks for a search chain which should consist in the movie name. Then is retrieve some results that it displays, leaving the choice to interactively select a result to get it printed in a standard formatted way :
```
  Movie Title (Year - Director) Actor1, Actor2, ...
```

Example for Jurassic Park :
```
  Jurassic Park (1993 - Steven Spielberg) Sam Neill, Laura Dern, Jeff Goldblum, Richard Attenborough
```

# License
omdb-tool is licensed under the GPL version 3.0. See LICENSE for more details
