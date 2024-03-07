#!/usr/bin/python3


class FileStorage:
    """ FileStorage class """


    # Private class attributes
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        
        return FileStorage.__objects