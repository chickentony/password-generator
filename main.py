import sys
import logging.config

from PySide6.QtWidgets import QApplication
import yaml

from src.password_generator import PasswordGenerator

if __name__ == '__main__':
    with open("logging.conf.yml") as config_file_path:
        logging.config.dictConfig(yaml.safe_load(config_file_path))

    app = QApplication()
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
