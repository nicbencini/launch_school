import unittest
from todo_class import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))
    
    def test_to_list(self):

        test_list = [Todo("Buy milk"),
                     Todo("Clean room"),
                     Todo("Go to the gym")
                     ]
        
        self.assertEqual(test_list, self.todos.to_list())

    def test_first(self):

        self.assertEqual(self.todo1, self.todos.first())
    
    def test_last(self):

        self.assertEqual(self.todo3, self.todos.last())
    
    def test_all_done(self):
        self.assertFalse(self.todos.all_done())
    
    def test_add_invalid(self):

        with self.assertRaises(TypeError):
            self.todos.add('Test')
        
        with self.assertRaises(TypeError):
            self.todos.add(1)
        
    def test_todo_at(self):

        with self.assertRaises(IndexError):
            self.todos.todo_at(4)
        
        self.assertEqual(self.todo2, self.todos.todo_at(1))
    
    def mark_done_at(self):

        with self.assertRaises(IndexError):
            self.todos.mark_done_at(4)
        
        self.todos.mark_done_at(1)

        self.assertFalse(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertFalse(self.todo3.done)
    
    def test_mark_undone_at(self):

        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(4)
        
        self.todos.mark_undone_at(1)

        self.assertFalse(self.todo1.done)
        self.assertFalse(self.todo2.done)
        self.assertFalse(self.todo3.done)
    
    def test_mark_all_done(self):

        self.todos.mark_all_done()

        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)
    
    def test_remove_at(self):

        with self.assertRaises(IndexError):
            self.todos.remove_at(4)
        
        self.todos.remove_at(1)
        self.assertEqual([self.todo1, self.todo3], self.todos.to_list())
    
    def test_str(self):
        string = (
        "---- Today's Todos -----\n"
        "[ ] Buy Milk\n"
        "[ ] Clean Room\n"
        "[ ] Go To The Gym"
        )
        self.assertEqual(string, str(self.todos))
    
    def test_str_done_todo(self):

        string = (
        "---- Today's Todos -----\n"
        "[ ] Buy Milk\n"
        "[X] Clean Room\n"
        "[ ] Go To The Gym"
        )

        self.todos.mark_done_at(1)
        self.assertEqual(string, str(self.todos))
    
    def test_str_all_done_todos(self):

        string = (
        "---- Today's Todos -----\n"
        "[X] Buy Milk\n"
        "[X] Clean Room\n"
        "[X] Go To The Gym"
        )

        self.todos.mark_all_done()
        self.assertEqual(string, str(self.todos))
    
    def test_each(self):

        string = (
        "---- Today's Todos -----\n"
        "[X] Buy Milk\n"
        "[X] Clean Room\n"
        "[X] Go To The Gym"
        )

        result = self.todos.each(lambda todo: todo.mark_done())

        self.assertEqual(string, str(self.todos))
    
    def test_select(self):

        string = (
        "---- Today's Todos -----\n"
        "[ ] Buy Milk"
        )

        selected_list = self.todos.select(lambda todo: 'Milk' in str(todo))

        self.assertEqual(string, str(selected_list))


        

        



if __name__ == "__main__":
    unittest.main()