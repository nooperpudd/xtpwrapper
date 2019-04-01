# encoding:utf-8
import ctypes

from xtpwrapper.xtp_enum import XTP_FUND_TRANSFER_TYPE
from . import StructBase


class XTPFundTransferReqStruct(StructBase):
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
    _enum_ = {
        "transfer_type": XTP_FUND_TRANSFER_TYPE
    }

    def __init__(self, serial_id, fund_account, password, amount,
                 transfer_type: XTP_FUND_TRANSFER_TYPE):
        super().__init__()
        self.serial_id = serial_id
        self.found_account = self._to_bytes(fund_account)
        self.password = self._to_bytes(password)
        self.amount = amount
        self.transfer_type = transfer_type
