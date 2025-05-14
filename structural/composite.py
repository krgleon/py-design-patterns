from typing import List

# Component interface: declares the common interface for both leaves and composites
class FileSystemItem:
    def get_size(self) -> int:
        # Ensures all file system elements (files, folders) expose a uniform interface
        raise NotImplementedError("Must be implemented by subclasses")

# Leaf class: represents a file (cannot contain children)
class File(FileSystemItem):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size  # Each file has a fixed size

    def get_size(self) -> int:
        # Leaf just returns its own size
        return self.size

# Composite class: represents a folder that can contain files or other folders
class Folder(FileSystemItem):
    def __init__(self, name: str):
        self.name = name
        self.contents: List[FileSystemItem] = []  # Holds both Files and Folders

    def add(self, item: FileSystemItem):
        # Adds a file or folder to the contents
        self.contents.append(item)

    def get_size(self) -> int:
        # Calculates the total size by delegating to child items
        # This allows recursive processing of nested structures
        return sum(item.get_size() for item in self.contents)

# --- Client code using Composite pattern ---

# Create individual file items (leaves)
file1 = File("resume.pdf", 120)
file2 = File("photo.jpg", 300)

# Create a folder and add files (composite node)
docs = Folder("Documents")
docs.add(file1)
docs.add(file2)

# Create another folder that includes the previous folder and a new file
archive = Folder("Archive")
archive.add(docs)  # Nested composite
archive.add(File("backup.zip", 800))  # Leaf

# The client uses get_size() without knowing if it's a file or folder
# Composite allows treating single items and groups uniformly
print("Total size of archive:", archive.get_size())  # Output: 1220
