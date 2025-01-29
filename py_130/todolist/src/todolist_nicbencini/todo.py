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
    
    @property
    def title(self):
        return self._title
    
    @done.setter
    def done(self, new_value):
        if isinstance(new_value, bool):
            self._done = new_value
        else:
            return NotImplemented
    
    def mark_done(self):
        self.done = True
    
    def __str__(self):
        if self._done:
            return f'[{self.COMPLETE_MARK}] {self._title.title()}'
        else:
            return f'[{self.NOT_COMPLETE_MARK}] {self._title.title()}'
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        return str(self) == str(other)