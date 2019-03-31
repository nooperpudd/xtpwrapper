import ctypes


class Base(ctypes.Structure):

    _enum_ = {}

    def _to_bytes(self, value):
        """
        :return:
        """
        if isinstance(value, bytes):
            return value
        else:
            return bytes(str(value), encoding="utf-8")

    @classmethod
    def from_dict(cls, obj):
        """
        :return:
        """
        return cls(**obj)

    def to_dict(self):
        """
        :return:
        """
        results = {}
        for key, _ in self._fields_:
            _value = getattr(self, key)
            if isinstance(_value, bytes):
                results[key] = _value.decode("utf-8")
            else:
                results[key] = _value
        return results

    def __repr__(self):
        """
        :return:
        """
        items = ["%s:%s" % (item, getattr(self, item)) for item, value in self._fields_]
        return "%s<%s>" % (self.__class__.__name__, ",".join(items))

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
            if isinstance(value, ctypes.Array):
                return [enum_cls(x) for x in value]
            else:
                return enum_cls(value)
        else:

            return value


class XTPRspInfoStruct(Base):
    _fields_ = [
        ("error_id", ctypes.c_int32),
        ("error_msg", ctypes.c_char * 124)
    ]
