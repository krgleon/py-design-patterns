# This is the legacy class (cannot be changed; could come from a third-party library)
class LegacyPrinter:
    # Method with an outdated or incompatible name
    def print_document(self, content: str):
        print(f"[Legacy] Printing document: {content}")

# Adapter class that provides the expected modern interface
class PrinterAdapter:
    def __init__(self, legacy_printer: LegacyPrinter):
        # Store the legacy printer instance internally
        self._legacy_printer = legacy_printer

    def print(self, content: str):
        # Translate the modern 'print()' call to the legacy method
        self._legacy_printer.print_document(content)

# Client function that expects any object with a `.print()` method
def generate_report(printer):
    # Calls the modern method, unaware of what's behind it
    printer.print("Quarterly Report: Revenue up 25%")

# Instantiate the legacy printer (not compatible with the client)
legacy = LegacyPrinter()

# Wrap it in an adapter so it matches the expected interface
adapter = PrinterAdapter(legacy)

# Now we can use the legacy printer through the adapter
generate_report(adapter)
