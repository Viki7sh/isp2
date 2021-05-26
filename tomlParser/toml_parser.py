import pytomlpp
from Utilities.Utilities import convert, deconvert


class Toml:

    def load(file="testtoml.toml"):
        with open(file, 'r+') as fr:
            packed = pytomlpp.load(fr)
        return deconvert(packed)

    def loads(src):
        packed = pytomlpp.loads(src)
        return deconvert(packed)
