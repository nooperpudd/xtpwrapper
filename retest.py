import  re
import pprint
regex = re.compile(r"\{(.*\n?)\}",re.X)

file = "xtp/include/xoms_api_struct_temp.h"

with open(file, encoding="utf-8") as f:
    # print(f.read())
    data = re.finditer(regex, f.read())

    print(list(data))


    # print(len(data))
    # pprint.pprint(data)
    for item in data:
        print("item:",item)
        # print(data)
    # print(data)