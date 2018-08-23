# encoding=utf-8
import codecs
import linecache
import os
import re
from collections import OrderedDict

XTP_PATH = os.path.join(os.path.dirname(__file__), "xtp")
HEADER_PATH = os.path.join(XTP_PATH, "include")
# USERAPI_DATA_FILE = os.path.join(HEADER_PATH, "xoms_api_struct_temp.h")
USERAPI_STRUCT_FILE = os.path.join(HEADER_PATH, "xquote_api_struct_temp.h")
# GENERATE_FILE = os.path.join(os.path.dirname(__file__), "ctpwrapper/ApiStructure.py")

# typedef signed char        int8_t;
# typedef short              int16_t;
# typedef int                int32_t;
# typedef long long          int64_t;
# typedef unsigned char      uint8_t;
# typedef unsigned short     uint16_t;
# typedef unsigned int       uint32_t;
# typedef unsigned long long uint64_t;

type_define = {
    "int8_t": "ctypes.c_int8",
    "int16_t": "ctypes.c_int16",
    "int32_t": "ctypes.c_int32",
    "int64_t": "ctypes.c_int64",
    "uint8_t": "ctypes.c_uint8",
    "uint16_t": "ctypes.c_uint16",
    "unit32_t": "ctypes.c_uint32",
    "unint64_t": "ctypes.c_uint64"
}

length_define = {
     "XTP_TRADING_DAY_LEN":9,
    "XTP_TICKER_LEN":16,
    "XTP_TICKER_NAME_LEN":64,
    "XTP_LOCAL_ORDER_LEN":11,
    "XTP_ORDER_EXCH_LEN":17,
    "XTP_EXEC_ID_LEN":18,
    "XTP_BRANCH_PBU_LEN":7,
    "XTP_ACCOUNT_NAME_LEN":16
}

# typedef char XTPVersionType[XTP_VERSION_LEN];
# /// 可交易日字符串长度
# #define XTP_TRADING_DAY_LEN 9
# /// 存放证券代码的字符串长度
# #define XTP_TICKER_LEN 16
# /// 存放证券名称的字符串长度
# #define XTP_TICKER_NAME_LEN 64
# /// 本地报单编号的字符串长度
# #define XTP_LOCAL_ORDER_LEN         11
# /// 交易所单号的字符串长度
# #define XTP_ORDER_EXCH_LEN          17
# /// 成交执行编号的字符串长度
# #define XTP_EXEC_ID_LEN             18
# /// 交易所交易员代码字符串长度
# #define XTP_BRANCH_PBU_LEN          7
# /// 用户资金账户的字符串长度
# #define XTP_ACCOUNT_NAME_LEN        16

import ctypes
# ctypes.c_char
class Parse(object):
    """
    解析结构体
    """

    def __init__(self, type_file, struct_file):
        """
        :param type_file:
        :param struct_file:
        """
        self.type_file = type_file
        self.struct_file = struct_file

        self.data_type = OrderedDict()
        self.data_type = self.data_type.update(type_define)
        self.struct = OrderedDict()
        self.struct_doc = dict()  # for struct doc

    def parse_datatype(self):
        """
        处理 UserApiDataType file.
        """
        for line in codecs.open(self.type_file, encoding="utf-8"):
            if line.startswith("typedef"):
                result = re.findall("\w+", line)
                name = result[2]
                type_ = result[1]

                if type_ == "char":
                    self.data_type[name] = {
                        "type": "ctypes.c_char",
                    }
                elif type_ =="enum":
                    self.data_type[name] = {
                        "type":"ctypes.c_int"
                    }
                elif type_ == "uint8_t":
                    self.data_type[name] = {
                        "type":"ctypes.uint8"
                    }
                elif type_ == "double":
                    self.data_type[name] = {
                        "type":"ctypes.c_double"
                    }
                else:
                    self.data_type[name] = {
                        "type": type_,
                    }

    def parse_struct(self):
        """
        解析结构体定义
        """
        self.parse_datatype()

        comple_struct = re.compile(r"\w+")
        struct_start = False
        inner_struct = False
        union_str= None
        for index, line in enumerate(codecs.open(self.struct_file,
                                                 encoding="utf-8")):
            doc_line = index

            if line.startswith("struct") or line.startswith("typedef struct"):
                struct_start = True
                result = re.findall("\w+", line)
                name = result[1]  # assign the name
                self.struct[name] = OrderedDict()
                # stuct doc
                struct_doc = linecache.getline(self.struct_file, doc_line)
                struct_doc = struct_doc.strip().replace("///", "")
                self.struct_doc[name] = struct_doc

            if "}" in line and inner_struct is False: # set end of the file
                struct_start = False

            if struct_start and re.match(r"\w+", line.strip()):

                # if line.strip().startwith("union"):
                result = re.findall("\w+", line)
                field_type = result[0]
                field_name = result[1].replace(";", "")
                struct_dict = self.struct[name]
                struct_dict[field_name] = self.data_type[field_type]
                # doc
                field_doc = linecache.getline(self.struct_file, doc_line)
                field_doc = field_doc.strip().replace("///", "")
                struct_dict[field_name + "_doc"] = field_doc

                if re.findall(r"\[(.+)\]", field_name):
                    length_define_type = re.findall(r"\[(.+)\]", field_name)[0]
                    struct_dict[field_name+"__length"] = length_define[length_define_type]


def generate_struct(struct, struct_doc, py_file):
    for item in struct:

        py_file.write("class {class_name}(Base):\n".format(class_name=item))
        py_file.write('    """{doc}"""\n'.format(doc=struct_doc[item]))
        py_file.write("    _fields_ = [\n")
        struct_dict = struct[item]

        for field in struct_dict:

            if field.endswith("_doc"):
                continue
            field_data = struct_dict[field]
            field_doc = struct[item][field + "_doc"]
            field_length = struct[item].get(field+"__length")
            field_type = field_data["type"]

            if not field_length:
                py_file.write("        ('{field}', {type_}), # {doc}\n".format(field=field,
                                                                           type_=field_type,doc=field_doc))
            else:
                py_file.write("        (''")

            # if field_data["type"] == "double":
            #     py_file.write("        ('{field}', ctypes.c_double),  # {doc}\n".format(field=field, doc=field_doc))
            # elif field_data["type"] == "int":
            #     py_file.write("        ('{field}', ctypes.c_int),  # {doc}\n".format(field=field, doc=field_doc))
            # elif field_data["type"] == "short":
            #     py_file.write("        ('{field}', ctypes.c_short),  # {doc}\n".format(field=field, doc=field_doc))
            # elif field_data["type"] == "str" and "length" not in field_data:
            #     py_file.write("        ('{field}', ctypes.c_char),  # {doc} \n ".format(field=field, doc=field_doc))
            # elif field_data["type"] == "str" and "length" in field_data:
            #     py_file.write("        ('{field}', ctypes.c_char*{len}),  # {doc}\n".format(field=field,
            #                                                                                 len=field_data["length"],
            #                                                                                 doc=field_doc))

        py_file.write("    ]\n")

        struct_fields = []
        for field in struct_dict:

            if field.endswith("_doc"):
                continue

            field_data = struct_dict[field]
            if field_data["type"] == "double":
                struct_fields.append("%s=0.0" % field)
            elif field_data["type"] in ["int", "short"]:
                struct_fields.append("%s=0" % field)
            else:
                struct_fields.append("%s=''" % field)
        py_file.write("    def __init__(self,%s):\n" % ",".join(struct_fields))
        py_file.write("        super({class_name},self).__init__()\n".format(class_name=item.replace("CThostFtdc", "")))

        for field in struct_dict:
            if field.endswith("_doc") or field.endswith("__length"):
                continue
            if struct_dict[field]["type"] == "double":
                py_file.write("        self.%s=float(%s)\n" % (field, field))
            if struct_dict[field]["type"] in ["int", "short"]:
                py_file.write("        self.%s=int(%s)\n" % (field, field))
            if struct_dict[field]["type"] == "str":
                py_file.write("        self.%s=self._to_bytes(%s)\n" % (field, field))


def generate_interface():
    files = [
        "xoms_api_struct_temp.h",
        "xquote_api_struct_temp.h",
    ]
    for file in files:
        parse = Parse(file,USERAPI_STRUCT_FILE)

        # parse = Parse(USERAPI_DATA_FILE, USERAPI_STRUCT_FILE)
        # parse.parse_struct()
        # structure = parse.struct
        # struct_doc = parse.struct_doc
        # generate python
        py_file = codecs.open(GENERATE_FILE, "w", encoding="utf-8")

        py_file.write('# encoding=utf-8\n')
        py_file.write("import ctypes\n")
        py_file.write("from ctpwrapper.base import Base\n")
        py_file.write("\n" * 2)

        generate_struct(structure, struct_doc, py_file)

        py_file.close()


if __name__ == "__main__":
    generate_interface()
