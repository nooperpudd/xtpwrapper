# encoding:utf-8
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
        ("transfer_type", ctypes.c_int)  # 内转类型
    ]
