# 🐍 Snake Terminal

A classic Snake game implemented in Python, playable directly in your terminal! Built using the `curses` library and a doubly linked list. Now available on PyPI for easy installation and play.

![Snake Terminal Demo](https://github.com/busayojee/snake-terminal/demo.png)  
*(Replace with an actual demo GIF or screenshot if available)*

---

## Features

- 🕹️ **Terminal-based gameplay**: Play Snake directly in your terminal.
- 🎮 **Smooth controls**: Use arrow keys to control the snake's direction.
- 🍎 **Dynamic growth**: The snake grows longer as it eats food.
- ⏩ **Progressive difficulty**: Game speed increases as your score improves.
- 🛠️ **Easy installation**: Install and play with just one command.

---

## Installation

You can install **Snake Terminal** directly from PyPI using `pip`:

```bash
pip install snake-terminal
```

---

## How to Play

After installation, simply run the game from your terminal:

```bash
snake-terminal
```

### Controls

Arrow keys (↑, ↓, ←, →): Change the snake's direction.

q: Quit the game.

### Objective

Eat the food to grow the snake and increase your score. Avoid colliding with yourself!

---

## Project Structure

The package is structured as follows:

```plaintext
snake-terminal/
├── snaketerm/        # Package source code
│   ├── __init__.py        # Package initialization
│   ├── game.py            # Game logic and loop
│   ├── main.py            # Entry point
│   ├── snake.py           # Snake class and movement logic
├── README.md              # Project documentation
├── setup.py               # Package setup and configuration
└── setup.cfg
```

### Contributing

Contributions are welcome! If you'd like to improve the game.

---

## Acknowledgments

- Inspired by the classic Snake game.
- Built with Python's curses library for terminal-based graphics.

---

Enjoy the game! 🎉

If you have any questions or feedback, feel free to open an issue or reach out.

