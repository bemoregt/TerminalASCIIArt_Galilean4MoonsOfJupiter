# Jupiter's Galilean Moons ASCII Visualizer

Real-time ASCII art visualization of Jupiter's four Galilean moons (Io, Europa, Ganymede, and Callisto) relative to Jupiter in your terminal.

![Jupiter's Galilean Moons](https://upload.wikimedia.org/wikipedia/commons/e/e4/Galilean_satellites_-_Hubble_Space_Telescope_-_20070308_%28thumbnail%29.jpg)

## Description

This Python script calculates and displays the real-time positions of Jupiter's four Galilean moons discovered by Galileo Galilei in 1610:
- Io
- Europa
- Ganymede
- Callisto

The visualization shows Jupiter as `[====JUPITER====]` in the center of your terminal, with each moon (*) displayed at its accurate scaled position relative to Jupiter based on astronomical calculations.

## Features

- Real-time calculation of moon positions using astronomical formulas
- Terminal-based ASCII visualization
- Automatic updates every second
- Cross-platform support (Windows, macOS, Linux)
- Simple user interface

## Requirements

- Python 3.x
- PyEphem library (`pip install ephem`)

## Installation

1. Clone this repository:
```
git clone https://github.com/bemoregt/TerminalASCIIArt_Galilean4MoonsOfJupiter.git
```

2. Install required dependencies:
```
pip install ephem
```

## Usage

Run the script with Python:
```
python jupiter_moons.py
```

The visualization will update every second. Press `Ctrl+C` to exit.

## How It Works

The script uses the PyEphem library to:
1. Calculate the positions of Jupiter and its moons based on the current time
2. Convert astronomical coordinates to relative positions in Jupiter radii
3. Scale these positions to fit in the terminal display
4. Render the positions using ASCII characters

## Example Output

```
                  Callisto                   Ganymede     Io  Europa
                             [====JUPITER====]   *     *    *
```

## Author

Wonwoo Park (bemore.one@gmail.com)

## License

MIT License
