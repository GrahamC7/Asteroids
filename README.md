# Asteroids Game

A classic Asteroids game implementation built with Python and Pygame. Navigate your spaceship through an asteroid field, shooting asteroids to survive as long as possible.

## Features

- **Classic Gameplay**: Control a triangular spaceship in space
- **Asteroid Physics**: Asteroids split into smaller pieces when shot
- **Smooth Controls**: Responsive keyboard controls for movement and shooting
- **Collision Detection**: Real-time collision detection between player, asteroids, and shots
- **Dynamic Asteroid Field**: Continuously spawning asteroids to keep the challenge going

## Controls

- **W** - Move forward (thrust)
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right
- **SPACE** - Shoot

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Asteroids
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.6+
- Pygame 2.6.1

## Game Mechanics

- **Player Ship**: Triangular spaceship that can rotate and thrust in any direction
- **Asteroids**: Come in multiple sizes (small, medium, large) and split when destroyed
- **Shooting**: Limited by a cooldown period to prevent spam
- **Collision**: Game ends when the player collides with an asteroid
- **Screen Wrapping**: Objects wrap around screen edges for seamless gameplay

## Project Structure

```
asteroid.py         # Asteroid class and splitting logic
asteroidfield.py    # Manages asteroid spawning
circleshape.py      # Base class for circular game objects
constants.py        # Game configuration and constants
main.py            # Main game loop and initialization
player.py          # Player ship class and controls
shot.py            # Projectile class
requirements.txt   # Python dependencies
```

## Game Constants

The game is highly configurable through `constants.py`:

- **Screen**: 1280x720 resolution
- **Player**: 20px radius, 300°/sec turn speed, 200px/sec movement speed
- **Asteroids**: 20-60px radius range, spawn every 0.8 seconds
- **Shots**: 5px radius, 500px/sec speed, 0.3 second cooldown

## Development

This project demonstrates:
- Object-oriented programming in Python
- Game development with Pygame
- Sprite management and collision detection
- Real-time input handling
- Vector mathematics for 2D movement

## Future Enhancements

Possible improvements could include:
- Score system
- Multiple lives
- Power-ups
- Sound effects
- High score persistence
- Different asteroid types
- Particle effects

## License

This project is open source and available under the MIT License.