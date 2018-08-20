import ctypes


class Base(ctypes.Structure):

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
            # if isinstance(_value, bytes):
            #     results[key] = _value.decode("gbk")
            # else:
            results[key] = _value
        return results

    def __repr__(self):
        """
        :return:
        """
        items = ["%s:%s" % (item, getattr(self, item)) for item, value in self._fields_]
        return "%s<%s>" % (self.__class__.__name__, ",".join(items))

class  XTPFundTransferReq(Base):

    _fields_ = [
        ('serial_id', ctypes.c_short),  # 序列系列号
        ('fund_account', ctypes.c_int),  # 序列号

        ('password',ctypes.c_char),
        ("amount",ctypes.c_double),
        ("transfer_type",ctypes.c_char)
    ]
    #
    # def __init__(self, SequenceSeries=0, SequenceNo=0):
    #     super(DisseminationField, self).__init__()
    #     self.SequenceSeries = int(SequenceSeries)
    #     self.SequenceNo = int(SequenceNo)
{
    ///资金内转编号，无需用户填写，类似于xtp_id
    uint64_t	serial_id;
	///资金账户代码
	char        fund_account[XTP_ACCOUNT_NAME_LEN];
	///资金账户密码
	char	    password[XTP_ACCOUNT_PASSWORD_LEN];
	///金额
	double	    amount;
	///内转类型
	XTP_FUND_TRANSFER_TYPE	transfer_type;

};