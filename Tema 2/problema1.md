# Token Ring Simulation

This project is a **Token Ring** simulation using **Pygame**. The simulation represents a network where a token circulates between nodes to facilitate message passing. The user can control the direction of the token flow and visualize the movement in real-time.

## Features
- **Graphical Representation**: Nodes are displayed in a circular topology with connecting edges.
- **Token Passing**: A token moves between nodes in a chosen direction.
- **Randomized IP Assignment**: Each node is assigned a unique IP address.
- **Logging System**: The token's journey is logged in a `result.txt` file.
- **Interactive Controls**: Users can change the direction or trigger token transmission using the keyboard.

## Requirements
To run the project, install the necessary dependencies:

```bash
pip install pygame
```

## How to Run
Run the script using Python:

```bash
python problema1.py
```

## Controls
- **Press `1`** → Set token movement to clockwise.
- **Press `2`** → Set token movement to counterclockwise.
- **Press `SPACE`** → Start token transmission between two randomly chosen nodes.
- **Press `X`** or close the window → Exit the simulation.

## File Structure
```
|-- problema1.py     # Main Python script
|-- result.txt        # Log file storing token movements
|-- README.md         # Documentation
```

## How It Works
1. The program initializes 10 nodes and assigns them random IP addresses.
2. Nodes are arranged in a circular layout.
3. When triggered, a token moves from a randomly chosen source to a destination.
4. The token moves step-by-step until it reaches the destination.
5. The journey is logged in `result.txt`.
6. The user can change the direction and restart the process at any time.

## Example Output (Logged in `result.txt`)
```
source: C3, destination: C7
C3: moving token
C4: moving token
C5: moving token
C6: moving token
C7: reached destination
```

