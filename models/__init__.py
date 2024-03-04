#!/usr/bin/python3
"""Initialization file to create a unique FileStorage instance"""
from models.engine.file_storage import FileStorage

file_path ="file.json"
storage = FileStorage(file_path)
storage.reload()
