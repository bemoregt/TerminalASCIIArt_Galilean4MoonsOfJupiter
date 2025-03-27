#!/usr/bin/env python3
"""
Jupiter's Galilean Moons Visualizer
This script shows real-time positions of Jupiter's four Galilean moons
(Io, Europa, Ganymede, and Callisto) relative to Jupiter using ASCII art.
by WonwooPark, email: bemore.one@gmail.com

Dependencies:
- ephem: pip install ephem
- time: standard library
- os: standard library
Usage:
python jupiter_moons.py
Press Ctrl+C to exit
"""
import ephem
import time
import os
from datetime import datetime

def clear_screen():
   """Clear the terminal screen."""
   try:
       os.system('cls' if os.name == 'nt' else 'clear')
   except:
       # 화면을 지우는 대신 여러 줄 출력
       print("\n" * 5)

def calculate_moon_positions():
   """Calculate the positions of Jupiter's moons."""
   # Create Jupiter object
   jupiter = ephem.Jupiter()
   # Set current time
   jupiter.compute(datetime.utcnow())
   
   # Calculate positions of all moons
   positions = []
   for moon in [ephem.Io(), ephem.Europa(), ephem.Ganymede(), ephem.Callisto()]:
       moon.compute(datetime.utcnow())
       # Get X position relative to Jupiter (in Jupiter radii)
       positions.append(moon.x)
       
   return positions

def create_visualization(positions):
   """Create ASCII visualization of Jupiter and its moons."""
   # Constants for visualization
   JUPITER = '[====JUPITER====]'
   SCALE = 0.2  # 스케일 팩터
   WIDTH = 150  # 디스플레이 너비
   
   # Create empty display
   display = [' ' * WIDTH]
   
   # Add Jupiter in the center
   jupiter_pos = WIDTH // 2 - len(JUPITER) // 2
   display[0] = display[0][:jupiter_pos] + JUPITER + display[0][jupiter_pos + len(JUPITER):]
   
   # Add moons with specific symbols
   moon_names = ['Io', 'Europa', 'Ganymede', 'Callisto']
   moon_symbols = ['*', '*', '*', '*']  # 각 위성별 심볼
   
   for pos, name, symbol in zip(positions, moon_names, moon_symbols):
       # Scale position and add to center
       scaled_pos = int(pos * SCALE * 10)  # Convert Jupiter radii to character positions
       moon_pos = jupiter_pos + len(JUPITER) // 2 + scaled_pos
       
       # Ensure moon position is within bounds
       if 0 <= moon_pos < WIDTH:
           display[0] = display[0][:moon_pos] + symbol + display[0][moon_pos + 1:]
   
   # Add moon names above the visualization
   name_line = ' ' * WIDTH
   for pos, name in zip(positions, moon_names):
       scaled_pos = int(pos * SCALE * 10)
       name_pos = jupiter_pos + len(JUPITER) // 2 + scaled_pos - len(name) // 2
       if 0 <= name_pos < WIDTH - len(name):
           name_line = name_line[:name_pos] + name + name_line[name_pos + len(name):]
   
   return name_line + '\n' + display[0]

def main():
   """Main function to run the visualization."""
   try:
       while True:
           clear_screen()
           positions = calculate_moon_positions()
           # 디버깅 정보 출력
           print(f"Raw positions: {positions}")
           visualization = create_visualization(positions)
           print("\nJupiter's Galilean Moons - Real-time Visualization")
           print("(Press Ctrl+C to exit)\n")
           print(visualization)
           time.sleep(1)  # Update every second
           
   except KeyboardInterrupt:
       print("\nExiting...")
   except Exception as e:
       print(f"\nAn error occurred: {e}")
       print("Make sure you have ephem installed (pip install ephem)")

if __name__ == "__main__":
   main()