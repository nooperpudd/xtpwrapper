import ctypes
from ._struct import Base

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