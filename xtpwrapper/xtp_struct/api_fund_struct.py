# encoding:utf-8
import ctypes

from . import Base


class XTPFundTransferReqStruct(Base):
    """
    用户资金请求

   """
    _fields_ = [
        ('serial_id', ctypes.c_uint64),  # 资金内转编号，无需用户填写，类似于xtp_id
        ('fund_account', ctypes.c_char * 16),  # 资金账户代码
        ('password', ctypes.c_char * 64),  # 资金账户密码
        ("amount", ctypes.c_double),  # 金额

        # XTP_FUND_TRANSFER_OUT = 0, 转出 从XTP转出到柜台
        # XTP_FUND_TRANSFER_IN,	转入从柜台转入XTP
        # XTP_FUND_TRANSFER_UNKNOWN	未知类型
        ("transfer_type", ctypes.c_int)  # 内转类型
    ]
