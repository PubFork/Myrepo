import ipaddress
import importlib

classes_cache = {}
instance_cache = {}

def get_class(type:str):
    cls  = classes_cache.get(type)
    module,fn = type.rsplit(".",maxsplit=1)
    mod = importlib.import_module(module)
    cls = getattr(mod,fn)
    classes_cache[type] = cls

    if issubclass(cls,BaseType):
        return cls
    raise TypeError("wrong type")

def get_instance(type,**option):
    key = ",".join("{}={}".format(k,v) for k,v in sorted(option.items()))
    key = "{}|{}".format(type,key)
    obj = instance_cache.get(key)
    if obj:
        return obj

    obj = get_class(type)(**option)
    instance_cache[key] = obj
    return obj


class BaseType:
    def __init__(self,**option):
        self.option = option

    def __getattr__(self, item):
        return self.option.get(item)

    def stringfy(self,value):
        raise NotImplementedError

    def desstringfy(self,value):
        raise NotImplementedError

class Int(BaseType):
    def stringfy(self, value):
        value = int(value)
        max = self.max
        if max and value>max:
            raise ValueError("too big")
        min = self.min
        if min and value<min:
            raise ValueError("too small")
        return str(ipaddress.ip_address(value))

    def desstringfy(self, value):
        pass

class IP(BaseType):
    def stringfy(self, value):
        val = str(ipaddress.ip_address(value))
        if not val and val.startswith(self.prefix):
            raise ValueError()
        return val

    def desstringfy(self, value):
        pass
