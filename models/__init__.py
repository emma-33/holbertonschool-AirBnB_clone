#!/usr/bin/python3
"""Initialization file to create a unique FileStorage instance"""


from models.engine.file_storage import FileStorage

file_storage = FileStorage()
file_storage.reload()
