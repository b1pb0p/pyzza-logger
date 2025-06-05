

def load_stylesheet(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Warning: QSS file '{path}' not found.")
        return ""
