# encoding:utf-8
# distutils: language=c++
from cpython cimport PyObject
from libc.stdint cimport uint32_t, uint64_t
from libc.string cimport const_char
from libcpp cimport bool as cbool

from .headers.xoms_api_fund_struct cimport XTPFundTransferReq
from .headers.xoms_api_struct cimport (
    XTPOrderInsertInfo,
    XTPQueryOrderReq,
    XTPQueryOptionAuctionInfoReq,
    XTPQueryETFComponentReq,
    XTPQueryETFBaseReq,
    XTPQueryTraderReq,
    XTPQueryStructuredFundInfoReq,
    XTPQueryFundTransferLogReq,
    XTPOrderInfo,
    XTPTradeReport,
    XTPOrderCancelInfo,
    XTPQueryStkPositionRsp,
    XTPQueryAssetRsp,
    XTPStructuredFundInfo,
    XTPFundTransferNotice,
    XTPQueryETFBaseRsp,
    XTPQueryETFComponentRsp,
    XTPQueryIPOTickerRsp,
    XTPQueryIPOQuotaRsp,
    XTPQueryOptionAuctionInfoRsp,
    XTPQueryOrderRsp,
    XTPQueryTradeRsp
)
from .headers.xtp_api_data_type cimport XTP_PROTOCOL_TYPE, XTP_LOG_LEVEL, XTP_TE_RESUME_TYPE
from .headers.xtp_api_struct_common cimport XTPRI
from .headers.xtp_trader_api cimport TraderApi, CreateTraderApi, WrapperTraderSpi

import ctypes

from xtpwrapper.xtp_struct import XTPRspInfoStruct
from xtpwrapper.xtp_struct.xoms_struct import (XTPOrderInfoStruct,XTPFundTransferNoticeStruct,
                                               XTPQueryIPOQuotaRspStruct,XTPQueryIPOTickerRspStruct,
                                               XTPQueryETFComponentRspStruct,XTPQueryOptionAuctionInfoRspStruct,
                                               XTPQueryETFBaseRspStruct,XTPQueryAssetRspStruct,
                                               XTPOrderCancelInfoStruct,XTPQueryStkPositionRspStruct,
                                               XTPTradeReportStruct, XTPStructuredFundInfoStruct)
cdef class TraderWrapper:
    cdef TraderApi *_api
    cdef WrapperTraderSpi *_spi

    def __cinit__(self):
        self._api = NULL
        self._spi = NULL

    def __dealloc__(self):
        self.Release()

    def Release(self):

        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

    def CreateTrader(self, client_id, save_file_path, log_level):
        """
        如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，
        但是对于同一账户，相同的client_id只能保持一个session连接，
        后面的登录在前一个session存续期间，无法连接。系统不支持过夜，请确保每天开盘前重新启动
        :param client_id: （必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义
        :param save_file_path: （必须输入）存贮订阅信息文件的目录，请设定一个真实存在的有可写权限的路径
        :param log_level: 日志输出级别
        :return:
        """
        self._api = CreateTraderApi(client_id, save_file_path, <XTP_LOG_LEVEL> log_level)

        if self._api is not NULL:

            self._spi = new WrapperTraderSpi(<PyObject *> self)
            if self._spi is not NULL:
                self._api.RegisterSpi(self._spi)
            else:
                raise MemoryError("spi memory error")
        else:
            raise MemoryError("api memory error")

    def Release(self):
        """
        # 删除接口对象本身
        # @remark 不再使用本接口对象时,调用该函数删除接口对象
        :return:
        """

        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

    def GetTradingDay(self):
        """
        # 获取当前交易日
        # @return 获取到的交易日
        # @remark 只有登录成功后,才能得到正确的交易日
        :return:
        """
        cdef const_char *result

        if self._spi is not NULL:
            with nogil:
                result = self._api.GetTradingDay()
            return result

    def GetApiLastError(self):
        """
        # 获取API的系统错误
        # @return 返回的错误信息，可以在Login、InsertOrder、CancelOrder返回值为0时调用，获取失败的原因
        # @remark 可以在调用api接口失败时调用，例如login失败时
        :return:
        """
        cdef XTPRI *err
        if self._spi is not NULL:
            with nogil:
                err = self._api.GetApiLastError()
            return XTPRspInfoStruct.from_address(<size_t> err)

    def GetApiVersion(self):
        """
        # 获取API的发行版本号
        # @return 返回api发行版本号
        :return:
        """
        cdef const_char *result
        if self._api is not NULL:
            result = self._api.GetApiVersion()
            return result

    def GetClientIDByXTPID(self, uint64_t order_xtp_id):
        """
        # 通过报单在xtp系统中的ID获取下单的客户端id
        # @return 返回客户端id，可以用此方法过滤自己下的订单
        # @param order_xtp_id 报单在xtp系统中的ID
        # @remark 由于系统允许同一用户在不同客户端上登录操作，每个客户端通过不同的client_id进行区分
        :param order_xtp_id:
        :return:
        """
        cdef unsigned char result

        if self._spi is not NULL:
            with nogil:
                result = self._api.GetClientIDByXTPID(order_xtp_id)
            return result

    def GetAccountByXTPID(self, uint64_t order_xtp_id):
        """
        # 通过报单在xtp系统中的ID获取相关资金账户名
        # @return 返回资金账户名
        # @param order_xtp_id 报单在xtp系统中的ID
        # @remark 只有资金账户登录成功后,才能得到正确的信息
        :param order_xtp_id:
        :return:
        """
        cdef const_char *result

        if self._spi is not NULL:
            with nogil:
                result = self._api.GetAccountByXTPID(order_xtp_id)
            return result

    def SubscribePublicTopic(self, XTP_TE_RESUME_TYPE resume_type):
        """
        # 订阅公共流。
        # @param resume_type 公共流（订单响应、成交回报）重传方式
        #        XTP_TERT_RESTART:从本交易日开始重传
        #        XTP_TERT_RESUME:(self,保留字段，此方式暂未支持)从上次收到的续传
        #        XTP_TERT_QUICK:只传送登录后公共流的内容
        # @remark 该方法要在Login方法前调用。若不调用则不会收到公共流的数据。注意在用户断线后，如果不登出就login(self,)，公共流订阅方式不会起作用。用户只会收到断线后的所有消息。如果先logout(self,)再login(self,)，那么公共流订阅方式会起作用，用户收到的数据会根据用户的选择方式而定。

        :param resume_type:
        :return:
        """
        if self._spi is not NULL:
            with nogil:
                self._api.SubscribePublicTopic(resume_type)

    def SetSoftwareVersion(self, const_char *version):
        """
        # 设置软件开发版本号
        # @param version 用户开发软件版本号，非api发行版本号，长度不超过15位，以'\0'结尾
        # @remark 此函数必须在Login之前调用，标识的是客户端版本号，而不是API的版本号，由用户自定义
        :param version:
        :return:
        """
        if self._spi is not NULL:
            with nogil:
                self._api.SetSoftwareVersion(version)

    def SetSoftwareKey(self, const_char *key):
        """
        # 设置软件开发Key
        # @param key 用户开发软件Key，用户申请开户时给予，以'\0'结尾
        # @remark 此函数必须在Login之前调用
        :param key:
        :return:
        """
        if self._spi is not NULL:
            with nogil:
                self._api.SetSoftwareKey(key)

    def SetHeartBeatInterval(self, uint32_t erval):
        """
        # 设置心跳检测时间间隔，单位为秒
        # @param erval 心跳检测时间间隔，单位为秒
        # @remark 此函数必须在Login之前调用
        :param erval:
        :return:
        """
        if self._spi is not NULL:
            with nogil:
                self._api.SetHeartBeatInterval(erval)

    def Login(self, const_char *ip, int port, const_char *user,
              const_char *password, XTP_PROTOCOL_TYPE sock_type):
        """
        # 用户登录请求
        # @return session_id表明此资金账号登录是否成功，“0”表示登录失败，可以调用GetApiLastError(self,)来获取错误代码，非“0”表示登录成功，此时需要记录下这个返回值session_id，与登录的资金账户对应
        # @param ip 服务器地址，类似“127.0.0.1”
        # @param port 服务器端口号
        # @param user 登录用户名
        # @param password 登录密码
        # @param sock_type “1”代表TCP，“2”代表UDP，目前暂时只支持TCP
        # @remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api可支持多个账户连接，但是同一个账户同一个client_id只能有一个session连接，后面的登录在前一个session存续期间，无法连接

        :param ip:
        :param port:
        :param user:
        :param password:
        :param sock_type:
        :return:
        """
        cdef uint64_t result

        if self._spi is not NULL:
            with nogil:
                result = self._api.Login(ip, port, user, password, sock_type)
            return result

    def Logout(self, uint64_t session_id):
        """

        # 登出请求
        # @return 登出是否成功，“0”表示登出成功，“-1”表示登出失败
        # @param session_id 资金账户对应的session_id,登录时得到
        :param session_id:
        :return:
        """
        cdef int result
        if self._spi is not NULL:
            with nogil:
                result = self._api.Logout(session_id)
            return result

    def InsertOrder(self, order, uint64_t session_id):
        """
        # 报单录入请求
        # @return 报单在XTP系统中的ID,如果为‘0’表示报单发送失败，此时用户可以调用GetApiLastError(self,)来获取错误代码，非“0”表示报单发送成功，用户需要记录下返回的order_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
        # @param order 报单录入信息，其中order.order_client_id字段是用户自定义字段，用户输入什么值，订单响应OnOrderEvent(self,)返回时就会带回什么值，类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，order.ticker必须不带空格，以'\0'结尾
        # @param session_id 资金账户对应的session_id,登录时得到
        # @remark 交易所接收订单后，会在报单响应函数OnOrderEvent(self,)中返回报单未成交的状态，之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回

        :param order:
        :param session_id:
        :return:
        """
        cdef uint64_t result
        cdef size_t address

        if self._spi is not NULL:
            address = ctypes.addressof(order)
            with nogil:
                result = self._api.InsertOrder(<XTPOrderInsertInfo *> address, session_id)
            return result

    def CancelOrder(self, const uint64_t order_xtp_id, uint64_t session_id):
        """
        # 报单操作请求
        # @return 撤单在XTP系统中的ID,如果为‘0’表示撤单发送失败，此时用户可以调用GetApiLastError(self,)来获取错误代码，非“0”表示撤单发送成功，用户需要记录下返回的order_cancel_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
        # @param order_xtp_id 需要撤销的委托单在XTP系统中的ID
        # @param session_id 资金账户对应的session_id,登录时得到
        # @remark 如果撤单成功，会在报单响应函数OnOrderEvent(self,)里返回原单部撤或者全撤的消息，如果不成功，会在OnCancelOrderError(self,)响应函数中返回错误原因

        :param order_xtp_id:
        :param session_id:
        :return:
        """
        cdef uint64_t result
        if self._spi is not NULL:
            with nogil:
                result = self._api.CancelOrder(order_xtp_id, session_id)
            return result

    def QueryOrderByXTPID(self, const uint64_t order_xtp_id, uint64_t session_id, int request_id):
        """
        # 根据报单ID请求查询报单
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param order_xtp_id 需要查询的报单在xtp系统中的ID，即InsertOrder(self,)成功时返回的order_xtp_id
        # @param session_id 资金账户对应的session_id，登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        :param order_xtp_id:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result

        if self._spi is not NULL:
            with nogil:
                result = self._api.QueryOrderByXTPID(order_xtp_id, session_id, request_id)
            return result

    def QueryOrders(self, query_param, uint64_t session_id, int request_id):
        """
        # 请求查询报单
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param query_param 需要查询的订单相关筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
        # @param session_id 资金账户对应的session_id，登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        # @remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有报单，否则查询时间段内所有跟股票代码相关的报单，此函数查询出的结果可能对应多个查询结果响应

        :param query_param:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result
        cdef size_t address

        if self._spi is not NULL:
            address = ctypes.addressof(query_param)
            with nogil:
                result = self._api.QueryOrders(<XTPQueryOrderReq *> query_param, session_id, request_id)
            return result

    def QueryTradesByXTPID(self, const uint64_t order_xtp_id, uint64_t session_id, int request_id):
        """
        # 根据委托编号请求查询相关成交
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param order_xtp_id 需要查询的委托编号，即InsertOrder(self,)成功时返回的order_xtp_id
        # @param session_id 资金账户对应的session_id，登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        # @remark 此函数查询出的结果可能对应多个查询结果响应
        :param order_xtp_id:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result

        if self._spi is not NULL:
            with nogil:
                result = self._api.QueryTradesByXTPID(order_xtp_id, session_id, request_id)
            return result

    def QueryTrades(self, query_param, uint64_t session_id, int request_id):
        """
        # 请求查询已成交
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param query_param 需要查询的成交回报筛选条件，其中合约代码可以为空，则默认所有存在的合约代码，如果不为空，请不带空格，并以'\0'结尾，其中起始时间格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点，结束时间格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        # @remark 该方法支持分时段查询，如果股票代码为空，则默认查询时间段内的所有成交回报，否则查询时间段内所有跟股票代码相关的成交回报，此函数查询出的结果可能对应多个查询结果响应

        :param query_param:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result
        cdef size_t address

        if self._spi is not NULL:
            address = ctypes.addressof(query_param)
            with nogil:
                result = self._api.QueryTrades(<XTPQueryTraderReq *> address, session_id, request_id)
            return result

    def QueryPosition(self, const_char *ticker, uint64_t session_id, int request_id):
        """
        # 请求查询投资者持仓
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param ticker 需要查询的持仓合约代码，可以为空，如果不为空，请不带空格，并以'\0'结尾
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        # @remark 该方法如果用户提供了合约代码，则会查询此合约的持仓信息，如果合约代码为空，则默认查询所有持仓信息
        :param ticker:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result

        if self._spi is not NULL:
            with nogil:
                result = self._api.QueryPosition(ticker, session_id, request_id)
            return result

    def QueryAsset(self, uint64_t session_id, int request_id):
        """   # 请求查询资产
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义"""
        cdef int result

        if self._spi is not NULL:
            with nogil:
                result = self._api.QueryAsset(session_id, request_id)
            return result

    def QueryStructuredFund(self, query_param, uint64_t session_id, int request_id):
        """
        # 请求查询分级基金
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param query_param 需要查询的分级基金筛选条件，其中母基金代码可以为空，则默认所有存在的母基金，如果不为空，请不带空格，并以'\0'结尾，其中交易市场不能为空
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        # @remark 此函数查询出的结果可能对应多个查询结果响应
        :param query_param:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(query_param)
            with nogil:
                result = self._api.QueryStructuredFund(<XTPQueryStructuredFundInfoReq *> address, session_id, request_id)
            return result

    def FundTransfer(self, fund_transfer, uint64_t session_id):
        """
        # 资金划拨请求
        # @return 资金划拨订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError(self,)来获取错误代码，非“0”表示消息发送成功，用户需要记录下返回的serial_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
        # @param session_id 资金账户对应的session_id,登录时得到
        :param fund_transfer:
        :param session_id:
        :return:
        """
        cdef uint64_t result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(fund_transfer)
            with nogil:
                result = self._api.FundTransfer(<XTPFundTransferReq *> address, session_id)
            return result

    def QueryFundTransfer(self, query_param, uint64_t session_id, int request_id):
        """
        # 请求查询资金划拨
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param query_param 需要查询的资金划拨订单筛选条件，其中serial_id可以为0，则默认所有资金划拨订单，如果不为0，则请求特定的资金划拨订单
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        :param query_param:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(query_param)
            with nogil:
                result = self._api.QueryFundTransfer(<XTPQueryFundTransferLogReq *> address, session_id, request_id)
            return result

    def QueryETF(self, query_param, uint64_t session_id, int request_id):
        """
        # 请求查询ETF清单文件
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param query_param 需要查询的ETF清单文件的筛选条件，其中合约代码可以为空，则默认所有存在的ETF合约代码，market字段也可以为初始值，则默认所有市场的ETF合约
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        :param query_param:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(query_param)
            with nogil:
                result = self._api.QueryETF(<XTPQueryETFBaseReq *> address, session_id, request_id)
            return result

    def QueryETFTickerBasket(self, query_param, uint64_t session_id, int request_id):
        """
        # 请求查询ETF股票篮
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param query_param 需要查询股票篮的的ETF合约，其中合约代码不可以为空，market字段也必须指定
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        :param query_param:
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(query_param)
            with nogil:
                result = self._api.QueryETFTickerBasket(<XTPQueryETFComponentReq *> address, session_id, request_id)
            return result

    def QueryIPOInfoList(self, uint64_t session_id, int request_id):
        """
        请求查询今日新股申购信息列表

        :param session_id: 资金账户对应的session_id,登录时得到
        :param request_id: 用于用户定位查询响应的ID，由用户自定义
        :return: 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        """
        cdef int result

        if self._spi is not NULL:
            with nogil:
                result = self._api.QueryIPOInfoList(session_id, request_id)
            return result

    def QueryIPOQuotaInfo(self, uint64_t session_id, int request_id):
        """
        # 请求查询用户新股申购额度信息
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        :param session_id:
        :param request_id:
        :return:
        """
        cdef int result

        if self._spi is not NULL:
            with nogil:
                result = self._api.QueryIPOQuotaInfo(session_id, request_id)
            return result

    def QueryOptionAuctionInfo(self, query_param, uint64_t session_id, int request_id):
        """
        请求查询期权合约

        :param query_param: 需要查询的期权合约的筛选条件，可以为NULL（为NULL表示查询所有的期权合约）
        :param session_id: 资金账户对应的session_id,登录时得到
        :param request_id: 用于用户定位查询响应的ID，由用户自定义
        :return: 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        """
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(query_param)
            with nogil:
                result = self._api.QueryOptionAuctionInfo(<XTPQueryOptionAuctionInfoReq *> address, session_id, request_id)
            return result

cdef extern int TraderSpi_OnDisconnected(self, uint64_t session_id, int reason) except -1:
    self.OnDisconnected(session_id, reason)

cdef extern int TraderSpi_OnError(self, XTPRI *error_info) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    self.OnError(error_info_obj)

cdef extern int TraderSpi_OnOrderEvent(self, XTPOrderInfo *order_info, XTPRI *error_info,
                                       uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if order_info is NULL:
        order_info_obj = None
    else:
        order_info_obj = XTPOrderInfoStruct.from_address(<size_t> order_info)

    self.OnOrderEvent(order_info_obj, error_info_obj, session_id)

cdef extern int TraderSpi_OnTradeEvent(self, XTPTradeReport *trade_info, uint64_t session_id) except -1:
    if trade_info is NULL:
        trade_info_obj = None
    else:
        trade_info_obj = XTPTradeReportStruct.from_address(<size_t> trade_info)
    self.OnTradeEvent(trade_info_obj, session_id)

cdef extern int TraderSpi_OnCancelOrderError(self, XTPOrderCancelInfo *cancel_info, XTPRI *error_info,
                                             uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    if cancel_info is NULL:
        cancel_info_obj = None
    else:
        cancel_info_obj = XTPOrderCancelInfoStruct.from_address(<size_t> cancel_info)

    self.OnCancelOrderError(cancel_info_obj, error_info_obj, session_id)

cdef extern int TraderSpi_OnQueryOrder(self, XTPQueryOrderRsp *order_info, XTPRI *error_info, int request_id,
                                       cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    if order_info is NULL:
        order_info_obj = None
    else:
        order_info_obj = XTPOrderInfoStruct.from_address(<size_t> order_info)

    self.OnQueryOrder(order_info_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnQueryTrade(self, XTPQueryTradeRsp *trade_info, XTPRI *error_info, int request_id,
                                       cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if trade_info is NULL:
        trade_info_obj = None
    else:
        trade_info_obj = XTPTradeReportStruct.from_address(<size_t> trade_info)

    self.OnQueryTrade(trade_info_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnQueryPosition(self, XTPQueryStkPositionRsp *position, XTPRI *error_info, int request_id,
                                          cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    if position is NULL:
        position_obj = None
    else:
        position_obj = XTPQueryStkPositionRspStruct.from_address(<size_t> position)

    self.OnQueryPosition(position_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnQueryAsset(self, XTPQueryAssetRsp *asset, XTPRI *error_info, int request_id, cbool is_last,
                                       uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    if asset is NULL:
        asset_obj = None
    else:
        asset_obj = XTPQueryAssetRspStruct.from_address(<size_t> asset)
    self.OnQueryAsset(asset_obj, error_info_obj, request_id, is_last, session_id)
cdef extern int TraderSpi_OnQueryStructuredFund(self, XTPStructuredFundInfo *fund_info, XTPRI *error_info,
                                                int request_id, cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    if fund_info is NULL:
        fund_info_obj = None
    else:
        fund_info_obj = XTPStructuredFundInfoStruct.from_address(<size_t> fund_info)

    self.OnQueryStructuredFund(fund_info_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnQueryFundTransfer(self, XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info,
                                              int request_id, cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if fund_transfer_info is NULL:
        fund_transfer_info_obj = None
    else:
        fund_transfer_info_obj = XTPFundTransferNoticeStruct.from_address(<size_t> fund_transfer_info)

    self.OnQueryFundTransfer(fund_transfer_info_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnFundTransfer(self, XTPFundTransferNotice *fund_transfer_info, XTPRI *error_info,
                                         uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if fund_transfer_info is NULL:
        fund_transfer_info_obj = None
    else:
        fund_transfer_info_obj = XTPFundTransferNoticeStruct.from_address(<size_t> fund_transfer_info)

    self.OnFundTransfer(fund_transfer_info_obj, error_info_obj, session_id)
cdef extern int TraderSpi_OnQueryETF(self, XTPQueryETFBaseRsp *etf_info, XTPRI *error_info, int request_id,
                                     cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if etf_info is NULL:
        etf_info_obj = None
    else:
        etf_info_obj = XTPQueryETFBaseRspStruct.from_address(<size_t> etf_info)

    self.OnQueryETF(etf_info_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnQueryETFBasket(self, XTPQueryETFComponentRsp *etf_component_info, XTPRI *error_info,
                                           int request_id, cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if etf_component_info is NULL:
        etf_component_info_obj = None
    else:
        etf_component_info_obj = XTPQueryETFComponentRspStruct.from_address(<size_t> etf_component_info)
    self.OnQueryETFBasket(etf_component_info_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnQueryIPOInfoList(self, XTPQueryIPOTickerRsp *ipo_info, XTPRI *error_info, int request_id,
                                             cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if ipo_info is NULL:
        ipo_info_obj = None
    else:
        ipo_info_obj = XTPQueryIPOTickerRspStruct.from_address(<size_t> ipo_info)
    self.OnQueryIPOInfoList(ipo_info_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnQueryIPOQuotaInfo(self, XTPQueryIPOQuotaRsp *quota_info, XTPRI *error_info, int request_id,
                                              cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if quota_info is NULL:
        quota_info_obj = None
    else:
        quota_info_obj = XTPQueryIPOQuotaRspStruct.from_address(<size_t> quota_info)

    self.OnQueryIPOQuotaInfo(quota_info_obj, error_info_obj, request_id, is_last, session_id)

cdef extern int TraderSpi_OnQueryOptionAuctionInfo(self, XTPQueryOptionAuctionInfoRsp *option_info, XTPRI *error_info,
                                                   int request_id, cbool is_last, uint64_t session_id) except -1:
    if error_info is NULL:
        error_info_obj = None
    else:
        error_info_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    if option_info is NULL:
        option_info_obj = None
    else:
        option_info_obj = XTPQueryOptionAuctionInfoRspStruct.from_address(<size_t> option_info)

    self.OnQueryOptionAuctionInfo(option_info_obj, error_info_obj, request_id, is_last, session_id)
