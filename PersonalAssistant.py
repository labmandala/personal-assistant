class PersonalAssistant:
  
  def __init__(self):
    self.contacts = {'Ann': 'Marketing Coordinator', 'Chelsea': 'Software Developer', 'Nichole': 'Sales Representative', 'Max': 'Technical Writer'}
    self.todos = []
    
  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
        # Get the todo_item index in list
        index = self.todos.index(todo_item)
        # pop the index for todo_item in todos list
        self.todos.pop(index)
    else:
        print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_birthday(self, name):
    if name == "Ann":
      return "Birthday is 04/15/92!"
    elif name == "Chelsea":
      return "Birthday is 07/12/98!"
    elif name == "Nichole":
      return "Birthday is 02/31/85!"
    else:
      return "Can't find birthday for this person..."
    # print statements replaced with return statements

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name!"
