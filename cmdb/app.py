import json
from cmdb.types import get_instance

jsonstr = """
{
    "1":"cmdb.types.Int",
    "2":"200",
    "option":{
        "max":100,
        "min":1
    }
}
"""

obj = json.loads(jsonstr)

type = obj["1"]
option = obj["option"]
print(get_instance(type,**option).stringfy(obj["2"]))
