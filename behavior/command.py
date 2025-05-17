# Command interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class AddTextCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.append_text(self.text)

    def undo(self):
        self.editor.delete_last(len(self.text))


class DeleteTextCommand(Command):
    def __init__(self, editor, count):
        self.editor = editor
        self.count = count
        self.deleted = ""

    def execute(self):
        self.deleted = self.editor.get_last(self.count)
        self.editor.delete_last(self.count)

    def undo(self):
        self.editor.append_text(self.deleted)

class TextEditor:
    def __init__(self):
        self.content = ""

    def append_text(self, text):
        self.content += text

    def delete_last(self, count):
        self.content = self.content[:-count]

    def get_last(self, count):
        return self.content[-count:]

    def show(self):
        print(f"[Editor] {self.content}")

class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            cmd = self.undo_stack.pop()
            cmd.undo()
            self.redo_stack.append(cmd)

    def redo(self):
        if self.redo_stack:
            cmd = self.redo_stack.pop()
            cmd.execute()
            self.undo_stack.append(cmd)

editor = TextEditor()
manager = CommandManager()

# Simulate user actions
manager.execute(AddTextCommand(editor, "Hello "))
manager.execute(AddTextCommand(editor, "World!"))
editor.show()  # Hello World!

manager.undo()
editor.show()  # Hello

manager.redo()
editor.show()  # Hello World!

