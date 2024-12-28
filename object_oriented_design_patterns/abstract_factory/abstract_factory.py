from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self): ...

    @abstractmethod
    def create_checkbox(self): ...


class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()
    

class Button(ABC):
    @abstractmethod
    def paint(self): ...


class WinButton(Button):
    def paint(self):
        return "Windows button"

class WinCheckbox(Button):
    def paint(self):
        return "Windows checkbox"


class MacButton(Button):
    def paint(self):
        return "Mac button"
    
class MacCheckbox(Button):
    def paint(self):
        return "Mac checkbox"

class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
    
    def create_ui(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()
        return button.paint(), checkbox.paint()