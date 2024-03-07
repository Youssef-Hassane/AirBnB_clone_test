#!/usr/bin/python3
import json


class FileStorage:
    """ FileStorage class """


    # Private Class Attributes
    __file_path = "file.json"
    __objects = {}
    
    # Public Instance Methods
    def all(self):
        """
        Public instance methods that returns the dictionary __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Public instance methods that sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """
        Public instance method that deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """

