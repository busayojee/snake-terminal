import curses
from game import Game


def main(stdscr):
    game = Game(stdscr)
    game.run()

if __name__ == '__main__':
    curses.wrapper(main)


# def main(stdscr):
#     curses.curs_set(0)  
#     stdscr.nodelay(1)   
#     stdscr.timeout(150) 
#     sh, sw = stdscr.getmaxyx()
#     game_window = curses.newwin(sh, sw, 0, 0)
#     game_window.keypad(1)
#     snake = Snake(0, 0, sh, sw)
#     food = (random.randint(1, sh - 2), random.randint(1, sw - 2))
#     game_window.addch(food[0], food[1], curses.ACS_PI) 
    
#     # Game loop
#     while True:
#         # Handle user input
#         key = game_window.getch()
#         if key == curses.KEY_UP:
#             snake.change_direction('UP')
#         elif key == curses.KEY_DOWN:
#             snake.change_direction('DOWN')
#         elif key == curses.KEY_LEFT:
#             snake.change_direction('LEFT')
#         elif key == curses.KEY_RIGHT:
#             snake.change_direction('RIGHT')
#         elif key == ord('q'): 
#             break
        
#         try:
#             snake.move()
#         except ValueError:  
#             break
        
#         if (snake.head.x, snake.head.y) == food:
#             snake.grow()
#             food = (random.randint(1, sh - 2), random.randint(1, sw - 2))
#             game_window.addch(food[0], food[1], curses.ACS_PI)
    
#         game_window.clear()
#         game_window.addch(food[0], food[1], curses.ACS_PI)
#         node = snake.head
#         while node:
#             game_window.addch(node.x, node.y, '#')
#             node = node.next
        
#         game_window.refresh()
#         time.sleep(0.1) 


# curses.wrapper(main)