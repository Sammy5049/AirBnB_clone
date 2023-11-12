#!/usr/bin/python3

"""Magic method for all models dir"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
