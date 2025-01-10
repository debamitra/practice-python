import types

type_objects = {name:obj for name,obj in vars(types).items() if isinstance(obj,type)}

for name,obj in type_objects.items():
    print(f"{name} = {obj}")

built_in_types = [
    int, float, str, list, tuple, dict, set, frozenset, bool, bytes, bytearray,
    memoryview, complex, range, type, object, slice, property, staticmethod, classmethod
]

for t in built_in_types:
    print(f"{t.__name__}: {t}")
