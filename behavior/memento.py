class TextMemento:
    def __init__(self, content):
        self._state = content

    def get_state(self):
        return self._state

class TextEditor:
    def __init__(self):
        self._content = ""

    def type(self, text):
        self._content += text

    def save(self):
        return TextMemento(self._content)

    def restore(self, memento):
        self._content = memento.get_state()

    def show(self):
        print(f"[Editor] {self._content}")

class HistoryManager:
    def __init__(self):
        self._history = []

    def save_state(self, memento):
        self._history.append(memento)

    def undo(self):
        if self._history:
            return self._history.pop()
        return None

editor = TextEditor()
history = HistoryManager()

editor.type("Hello")
history.save_state(editor.save())

editor.type(" World")
history.save_state(editor.save())

editor.type("!!!")
editor.show()  # Hello World!!!

memento = history.undo()
if memento:
    editor.restore(memento)
    editor.show()  # Hello World

memento = history.undo()
if memento:
    editor.restore(memento)
    editor.show()  # Hello
