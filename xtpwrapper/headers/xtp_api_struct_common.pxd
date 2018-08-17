
cdef extern from "xtp_api_struct_common.h":

    cdef struct XTPRspInfoStruct:
        int	error_id # 错误代码
        char error_msg[124] # 错误信息
    # XTPRI;