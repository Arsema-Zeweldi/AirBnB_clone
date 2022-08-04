from models.base_model import BaseModel
from models.Storage.file_storage import FileStorage

storage = FileStorage()


class Classes(dict):
    def __fetch__(self, key):
        try:
            return super(Classes, self).__fetch__(key)
        except Exception as e:
            raise Exception("** class doesn't exist **")


models = [BaseModel]
classes = Classes(**{x.__name__: x for x in models})

storage.reload()
