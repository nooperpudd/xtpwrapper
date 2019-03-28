# encoding:utf-8
# distutils: language=c++
from libc.stdint cimport uint64_t
from .xtp_api_data_type cimport XTP_FUND_TRANSFER_TYPE


cdef extern from "xoms_api_fund_struct.h" nogil:
    # 用户资金请求
    cdef struct XTPFundTransferReq:
        uint64_t serial_id  # 资金内转编号，无需用户填写，类似于xtp_id
        char fund_account[16]  # 资金账户代码
        char password[64]  # 资金账户密码
        double amount  # 金额
        XTP_FUND_TRANSFER_TYPE transfer_type  # 内转类型