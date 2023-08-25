class ConfigReader:
    def __init__(self, file_path):
        self.config = {}
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    self.config[key.strip()] = value.strip()

    def get_value(self, key):
        return self.config.get(key)
