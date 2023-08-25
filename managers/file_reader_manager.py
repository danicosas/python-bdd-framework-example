from managers.config_reader import ConfigReader

class FileReaderManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config_reader = ConfigReader('config.properties')
            # Agregar aquí otros tipos de lectores de archivos según sea necesario
        return cls._instance

    def get_config_reader(self):
        return self.config_reader
