# Concrete product classes for Windows UI elements
class WindowsButton:
    def render(self):
        return "🪟 Rendering a Windows button"

class WindowsCheckbox:
    def render(self):
        return "🪟 Rendering a Windows checkbox"

# Concrete product classes for Mac UI elements
class MacButton:
    def render(self):
        return "🍎 Rendering a Mac button"

class MacCheckbox:
    def render(self):
        return "🍎 Rendering a Mac checkbox"

# Factory function that returns a pair of Windows UI components
def create_windows_ui():
    return WindowsButton(), WindowsCheckbox()

# Factory function that returns a pair of Mac UI components
def create_mac_ui():
    return MacButton(), MacCheckbox()

# Function that renders the provided UI components
def render_ui(button, checkbox):
    print(button.render())
    print(checkbox.render())

# Operating system name used to select the UI theme
os_name = "windows"  # Try "windows" or "mac"

# Dictionary mapping OS names to their corresponding factories
factories = {
    "windows": create_windows_ui,
    "mac": create_mac_ui
}

# Create UI components based on the selected OS
button, checkbox = factories[os_name]()

# Render the selected UI components
render_ui(button, checkbox)
