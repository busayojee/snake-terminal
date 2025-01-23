import curses
import random
from .snake import Snake

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)       
        self.stdscr.nodelay(True)
        self.base_time = 200
        self.stdscr.timeout(self.base_time)  
        self.sr, self.sc = self.stdscr.getmaxyx()
        start_x = self.sr // 2
        start_y = self.sc // 2
        
        self.snake = Snake(start_x, start_y, self.sr, self.sc)
        self.food = self._place_food()
        self.score = 0
        self.speed_level = 1
    
    def _place_food(self):
        while True:
            fx = random.randint(0, self.sr - 1)
            fy = random.randint(0, self.sc - 1)
            if (fx, fy) not in self.snake.positions:
                return (fx, fy)
    def _update_speed(self):
        if self.score % 5 == 0 and self.score > 0:
            self.speed_level += 1
            new_delay = max(self.base_time - (self.speed_level * 20), 50)
            self.stdscr.timeout(new_delay)
    def _exit(self):
        self.stdscr.clear()
        msg = "Game Over! Press any key to exit."
        self.stdscr.addstr(self.sr // 2, self.sc // 2 - len(msg) // 2, msg)
        self.stdscr.refresh()
        self.stdscr.nodelay(False) 
        self.stdscr.getch()
    def run(self):
        """
        The main game loop.
        """
        while True:
            # Get user input
            try:
                key = self.stdscr.getch()
            except:
                key = -1     
            if key == curses.KEY_UP:
                self.snake.change_direction('UP')
            elif key == curses.KEY_DOWN:
                self.snake.change_direction('DOWN')
            elif key == curses.KEY_LEFT:
                self.snake.change_direction('LEFT')
            elif key == curses.KEY_RIGHT:
                self.snake.change_direction('RIGHT')
            elif key == ord('q'):
                # Press 'q' to quit
                break
            
            # Move the snake
            try:
                self.snake.move()
            except ValueError:
                break
            
            # Check if snake ate food
            if (self.snake.head.x, self.snake.head.y) == self.food:
                # Grow the snake
                try:
                    self.snake.grow()
                except ValueError:
                    break
                self.score +=1
                self._update_speed()
                self.food = self._place_food()
            # draw stuffs 
            self.stdscr.clear()
            self.stdscr.addch(self.food[0], self.food[1], curses.ACS_PI)
            node = self.snake.head
            while node:
                self.stdscr.addch(node.x, node.y, '#')
                node = node.next
            status = f"Score: {self.score}"
            self.stdscr.addstr(0, 0, status[:self.sc-1]) 
            self.stdscr.refresh()

        self._exit()
