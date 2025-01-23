class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

class Snake:
    def __init__(self, first_x, first_y, x_max, y_max):
        node = Node(first_x, first_y)
        self.head = node
        self.tail = node
        self.direction = 'RIGHT'
        self.positions = {(first_x, first_y)}
        self.x_max = x_max
        self.y_max = y_max
    
    def _wrap(self, x, y):
        # Wrap row
        if x < 0:
            x = self.x_max - 1
        elif x >= self.x_max:
            x = 0
        # Wrap column
        if y < 0:
            y = self.y_max - 1
        elif y >= self.y_max:
            y = 0
        return x, y
    
    def move(self):
        x, y = self.head.x, self.head.y
        if self.direction == 'UP':
            x-=1
        if self.direction == 'DOWN':
            x+=1
        if self.direction == 'RIGHT':
            y+=1
        if self.direction == 'LEFT':
            y-=1   
        
        x, y = self._wrap(x, y)
        x_tail, y_tail = self.tail.x, self.tail.y
        self.positions.remove((x_tail, y_tail))
        if self.tail == self.head:  # Snake has only one node
            self.head = None
            self.tail = None
        else:
            if self.tail.prev:
                self.tail = self.tail.prev 
                self.tail.next = None
            else:
                self.tail = None
        
        self.check_collision(x,y)


        new_head = Node(x,y)
        new_head.next = self.head
        if self.head:
            self.head.prev = new_head
        self.head = new_head
        if not self.tail:
            self.tail = self.head
        self.positions.add((x,y))

    def grow(self):
        x, y = self.head.x, self.head.y
        if self.direction == 'UP':
            x -= 1
        elif self.direction == 'DOWN':
            x += 1
        elif self.direction == 'LEFT':
            y -= 1
        elif self.direction == 'RIGHT':
            y += 1
        # Note that my tail is my head
        new_head = Node(x, y)
        new_head.next = self.head
        if self.head:
            self.head.prev = new_head
        self.head = new_head
        self.positions.add((x,y))

    def change_direction(self, new_direction):
        opposites = {'UP':'DOWN', 'DOWN': 'UP','LEFT': 'RIGHT','RIGHT': 'LEFT'}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction
    
    def check_collision(self, x,y):
        if(x,y) in self.positions:
            raise ValueError("Collision game over")
        return False
