import os

class FileExplorer:

    def __init__(self):
        self.current_dir = os.getcwd()
        self.python_files = []

    def explore_dir(self, path=None):
        if not path:
            path = self.current_dir
        for item in os.listdir(path):
            if item.startswith('.'):
                continue
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                self.explore_dir(item_path)
            elif os.path.isfile(item_path) and item_path.endswith('.py'):
                self.python_files.append(item_path)

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def get_python_files(self):
        self.explore_dir()
        return [(path, self.read_file(path)) for path in self.python_files]
