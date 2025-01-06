
class Todo:

    COMPLETE_MARK = 'X'
    NOT_COMPLETE_MARK = ' '

    def __init__(self, title):
        self._title = title
        self._done = False

    @property
    def task(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, new_value):
        if isinstance(new_value, bool):
            self._done = new_value
        else:
            return NotImplemented
    
    def __str__(self):
        if self._done:
            return f'[{self.COMPLETE_MARK}] {self._title.title()}'
        else:
            return f'[{self.NOT_COMPLETE_MARK}] {self._title.title()}'
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        return str(self) == str(other)
        
class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title
    
    def add(self, new_task):

        if not isinstance(new_task, Todo):
            raise TypeError('Can only add Todo objects')
        
        return self._todos.append(new_task)

def test_todo():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')
    todo4 = Todo('Clean room')

    print(todo1)                  # [ ] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [ ] Clean room

    print(todo2 == todo4)         # True
    print(todo1 == todo2)         # False
    print(todo4.done)             # False

    todo1.done = True
    todo4.done = True
    print(todo4.done)             # True

    print(todo1)                  # [X] Buy milk
    print(todo2)                  # [ ] Clean room
    print(todo3)                  # [ ] Go to gym
    print(todo4)                  # [X] Clean room

    print(todo2 == todo4)         # False

    todo4.done = False
    print(todo4.done)             # False
    print(todo4)                  # [ ] Clean room

#test_todo()

empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

def step_1():
    print('--------------------------------- Step 1')
    todo_list = setup()

    # setup() uses `todo_list.add` to add 3 todos

    try:
        todo_list.add(1)
    except TypeError:
        print('TypeError detected')    # TypeError detected

    for todo in todo_list._todos:
        print(todo)

step_1()