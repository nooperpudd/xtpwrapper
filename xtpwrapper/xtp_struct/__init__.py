import ctypes


class Mixin(object):
    """
    """

    def to_dict(self):
        """
        :return:
        """
        results = {}
        for key, _ in self._fields_:
            value = getattr(self, key)
            if isinstance(value, bytes):
                results[key] = value.decode("utf-8")
            elif isinstance(value, ctypes.Array):
                results[key] = [x for x in value]
            elif isinstance(value, (ctypes.Union, ctypes.Structure)):
                results[key] = value.to_dict()
            else:
                results[key] = value
        return results

    def __repr__(self):
        """
        :return:
        """
        items = []
        for item, value in self._fields_:
            if issubclass(value, (ctypes.Union, ctypes.Structure)):
                items.append(item + ":" + repr(getattr(self, item)))
            if issubclass(value, ctypes.Array) and not isinstance(getattr(self, item), bytes):
                items.append("%s:(%s)" % (item, ",".join([str(x) for x in getattr(self, item)])))
            else:
                items.append("%s:%s" % (item, getattr(self, item)))
        return "<%s>" % (",".join(items))


class StructBase(ctypes.Structure, Mixin):
    _enum_ = {}

    def _to_bytes(self, value):
        """
        :return:
        """
        if isinstance(value, bytes):
            return value
        else:
            return bytes(str(value), encoding="utf-8")

    def __getattribute__(self, name):
        """
        set attribute with enum
        :param name:
        :return:
        """
        _enum = ctypes.Structure.__getattribute__(self, '_enum_')
        value = ctypes.Structure.__getattribute__(self, name)

        if name in _enum:
            enum_cls = _enum[name]
            return enum_cls(value)
        else:

            return value


class UnionBase(ctypes.Union, Mixin):
    """
    """
    pass


class XTPRspInfoStruct(StructBase):
    _fields_ = [
        ("error_id", ctypes.c_int32),
        ("error_msg", ctypes.c_char * 124)
    ]
