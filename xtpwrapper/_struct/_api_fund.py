import ctypes
from ._struct import Base


class XTPFundTransferReq(Base):
    """
    用户资金请求
    """
    _fields_ = [
        ('serial_id', ctypes.c_short),  # 资金内转编号，无需用户填写，类似于xtp_id
        ('fund_account', ctypes.c_char * 16),  # 资金账户代码

        ('password', ctypes.c_char * 64),  # 资金账户密码
        ("amount", ctypes.c_double),  # 金额
        ("transfer_type", ctypes.c_int)  # 内转类型 # todo fix enum type
    ]

    # def __init__(self,serial_id=0,fund_account="",password="",amount=0.0,transfer_type=0):
    #     super(XTPFundTransferReq,self).__init__()
    #     self.serial_id = serial_id
    #     self.fund_account = fund_account
    # def __init__(self, SequenceSeries=0, SequenceNo=0):
    #     super(DisseminationField, self).__init__()
    #     self.SequenceSeries = int(SequenceSeries)
    #     self.SequenceNo = int(SequenceNo)
