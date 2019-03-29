# encoding:utf-8

from .trader_api import TraderWrapper
from .xtp_enum import XTP_TE_RESUME_TYPE, XTP_LOG_LEVEL
from .xtp_struct.api_fund_struct import XTPFundTransferReqStruct
from .xtp_struct.xoms_struct import (XTPOrderInsertInfoStruct,
                                     XTPQueryOrderReqStruct,
                                     XTPQueryTraderReqStruct,
                                     XTPQueryStructuredFundInfoReqStruct,
                                     XTPQueryFundTransferLogReqStruct,
                                     XTPQueryETFBaseReqStruct,
                                     XTPQueryETFComponentReqStruct,
                                     XTPQueryOptionAuctionInfoReqStruct)


class TraderApi(TraderWrapper):

    def CreateTrader(self, client_id: int, save_file_path: str,
                     log_level: XTP_LOG_LEVEL = XTP_LOG_LEVEL.XTP_LOG_LEVEL_INFO):
        """
        如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，
        但是对于同一账户，相同的client_id只能保持一个session连接，
        后面的登录在前一个session存续期间，无法连接。系统不支持过夜，请确保每天开盘前重新启动
        :param client_id: （必须输入）客户端id，用于区分同一用户的不同客户端，由用户自定义
        :param save_file_path: （必须输入）存贮订阅信息文件的目录，请设定一个真实存在的有可写权限的路径
        :param log_level: 日志输出级别
        :return:
        """
        super().CreateTrader(client_id, save_file_path.encode(), log_level)

    def Release(self):
        """
        # 删除接口对象本身
        # @remark 不再使用本接口对象时,调用该函数删除接口对象
        :return:
        """
        super().Release()

    def GetTradingDay(self):
        """
        # 获取当前交易日
        # @return 获取到的交易日
        # @remark 只有登录成功后,才能得到正确的交易日
        :return:
        """
        return super().GetTradingDay().decode()

    def GetApiLastError(self):
        """
        # 获取API的系统错误
        # @return 返回的错误信息，可以在Login、InsertOrder、CancelOrder返回值为0时调用，获取失败的原因
        # @remark 可以在调用api接口失败时调用，例如login失败时
        :return:
        """
        return super().GetApiLastError()

    def GetApiVersion(self):
        """
        # 获取API的发行版本号
        # @return 返回api发行版本号
        :return:
        """
        return super().GetApiVersion().decode()

    def GetClientIDByXTPID(self, order_xtp_id: int):
        """
        # 通过报单在xtp系统中的ID获取下单的客户端id
        # @remark 由于系统允许同一用户在不同客户端上登录操作，每个客户端通过不同的client_id进行区分
        :param order_xtp_id: 报单在xtp系统中的ID
        :return: 返回客户端id，可以用此方法过滤自己下的订单
        """
        return super().GetClientIDByXTPID(order_xtp_id)

    def GetAccountByXTPID(self, order_xtp_id: int):
        """
        # 通过报单在xtp系统中的ID获取相关资金账户名

        # @remark 只有资金账户登录成功后,才能得到正确的信息
        :param order_xtp_id: 报单在xtp系统中的ID
        :return: 返回资金账户名
        """
        return super().GetAccountByXTPID(order_xtp_id)

    def SubscribePublicTopic(self, resume_type: XTP_TE_RESUME_TYPE = XTP_TE_RESUME_TYPE.XTP_TERT_QUICK):
        """
        # 订阅公共流。

        # @remark 该方法要在Login方法前调用。若不调用则不会收到公共流的数据。注意在用户断线后，如果不登出就login(self,)，公共流订阅方式不会起作用。用户只会收到断线后的所有消息。如果先logout(self,)再login(self,)，那么公共流订阅方式会起作用，用户收到的数据会根据用户的选择方式而定。

        :param resume_type: 公共流（订单响应、成交回报）重传方式
        #        XTP_TERT_RESTART:从本交易日开始重传
        #        XTP_TERT_RESUME:(self,保留字段，此方式暂未支持)从上次收到的续传
        #        XTP_TERT_QUICK:只传送登录后公共流的内容
        :return:
        """
        super().SubscribePublicTopic(resume_type)

    def SetSoftwareVersion(self, version: str):
        """
        # 设置软件开发版本号

        # @remark 此函数必须在Login之前调用，标识的是客户端版本号，而不是API的版本号，由用户自定义
        :param version: 用户开发软件版本号，非api发行版本号，长度不超过15位，以'\0'结尾
        :return:
        """
        super().SetSoftwareVersion(version.encode())

    def SetSoftwareKey(self, key: str):
        """
        # 设置软件开发Key

        # @remark 此函数必须在Login之前调用
        :param key: 用户开发软件Key，用户申请开户时给予，以'\0'结尾
        :return:
        """
        super().SetSoftwareKey(key.encode())

    def SetHeartBeatInterval(self, erval: int):
        """
        # 设置心跳检测时间间隔，单位为秒

        # @remark 此函数必须在Login之前调用
        :param erval: 心跳检测时间间隔，单位为秒
        :return:
        """
        super().SetHeartBeatInterval(erval)

    def Login(self, ip: str, port: int, user: str, password: str, sock_type: int = 1):
        """
        # 用户登录请求
        # @return session_id表明此资金账号登录是否成功，“0”表示登录失败，
        可以调用GetApiLastError(self,)来获取错误代码，非“0”表示登录成功，此时需要记录下这个返回值session_id，与登录的资金账户对应

        # @remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api可支持多个账户连接，但是同一个账户同一个client_id只能有一个session连接，后面的登录在前一个session存续期间，无法连接

        :param ip: 服务器地址，类似“127.0.0.1”
        :param port: 服务器端口号
        :param user: 登录用户名
        :param password: 登录密码
        :param sock_type: “1”代表TCP，“2”代表UDP，目前暂时只支持TCP
        :return:
        """
        return super().Login(ip.encode(), port, user.encode(), password.encode(), sock_type)

    def Logout(self, session_id: int):
        """

        # 登出请求
        # @return
        # @param session_id
        :param session_id: 资金账户对应的session_id,登录时得到
        :return: 登出是否成功，“0”表示登出成功，“-1”表示登出失败
        """
        return super().Logout(session_id)

    def InsertOrder(self, order: XTPOrderInsertInfoStruct, session_id: int):
        """
        # 报单录入请求

        # @remark 交易所接收订单后，会在报单响应函数OnOrderEvent(self,)中返回报单未成交的状态，
        之后所有的订单状态改变（除了部成状态）都会通过报单响应函数返回

        :param order: 报单录入信息，其中order.order_client_id字段是用户自定义字段，
                用户输入什么值，订单响应OnOrderEvent(self,)返回时就会带回什么值，
                类似于备注，方便用户自己定位订单。当然，如果你什么都不填，也是可以的。order.order_xtp_id字段无需用户填写，
                order.ticker必须不带空格，以'\0'结尾
        :param session_id: 资金账户对应的session_id,登录时得到
        :return: 报单在XTP系统中的ID,如果为‘0’表示报单发送失败，此时用户可以调用GetApiLastError(self,)
        来获取错误代码，非“0”表示报单发送成功，用户需要记录下返回的order_xtp_id，
        它保证一个交易日内唯一，不同的交易日不保证唯一性
        """
        return super().InsertOrder(order, session_id)

    def CancelOrder(self, order_xtp_id: int, session_id: int):
        """
        # 报单操作请求
        # @return
        # @param order_xtp_id
        # @param session_id
        # @remark 如果撤单成功，会在报单响应函数OnOrderEvent(self,)里返回原单部撤或者全撤的消息，如果不成功，会在OnCancelOrderError(self,)响应函数中返回错误原因

        :param order_xtp_id: 需要撤销的委托单在XTP系统中的ID
        :param session_id: 资金账户对应的session_id,登录时得到
        :return: 撤单在XTP系统中的ID,如果为‘0’表示撤单发送失败，此时用户可以调用GetApiLastError(self,)
        来获取错误代码，非“0”表示撤单发送成功，用户需要记录下返回的order_cancel_xtp_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
        """
        return super().CancelOrder(order_xtp_id, session_id)

    def QueryOrderByXTPID(self, order_xtp_id: int, session_id: int, request_id: int):
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
        return super().QueryOrderByXTPID(order_xtp_id, session_id, request_id)

    def QueryOrders(self, query_param: XTPQueryOrderReqStruct,
                    session_id: int, request_id: int):
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
        return super().QueryOrders(query_param, session_id, request_id)

    def QueryTradesByXTPID(self, order_xtp_id: int, session_id: int, request_id: int):
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
        return super().QueryTradesByXTPID(order_xtp_id, session_id, request_id)

    def QueryTrades(self, query_param: XTPQueryTraderReqStruct, session_id: int, request_id: int):
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
        return super().QueryTrades(query_param, session_id, request_id)

    def QueryPosition(self, ticker: str, session_id: int, request_id: int):
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
        return super().QueryPosition(ticker, session_id, request_id)

    def QueryAsset(self, session_id: int, request_id: int):
        """
        # 请求查询资产
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义"""
        return super().QueryAsset(session_id, request_id)

    def QueryStructuredFund(self, query_param: XTPQueryStructuredFundInfoReqStruct,
                            session_id: int, request_id: int):
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
        return super().QueryStructuredFund(query_param, session_id, request_id)

    def FundTransfer(self, fund_transfer: XTPFundTransferReqStruct, session_id: int):
        """
        # 资金划拨请求
        # @return 资金划拨订单在XTP系统中的ID,如果为‘0’表示消息发送失败，此时用户可以调用GetApiLastError(self,)来获取错误代码，非“0”表示消息发送成功，用户需要记录下返回的serial_id，它保证一个交易日内唯一，不同的交易日不保证唯一性
        # @param session_id 资金账户对应的session_id,登录时得到
        :param fund_transfer:
        :param session_id:
        :return:
        """
        return super().FundTransfer(fund_transfer, session_id)

    def QueryFundTransfer(self, query_param: XTPQueryFundTransferLogReqStruct, session_id: int, request_id: int):
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
        return super().QueryFundTransfer(query_param, session_id, request_id)

    def QueryETF(self, query_param: XTPQueryETFBaseReqStruct, session_id: int, request_id: int):
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
        return super().QueryETF(query_param, session_id, request_id)

    def QueryETFTickerBasket(self, query_param: XTPQueryETFComponentReqStruct, session_id: int, request_id: int):
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
        return super().QueryETFTickerBasket(query_param, session_id, request_id)

    def QueryIPOInfoList(self, session_id: int, request_id: int):
        """
        请求查询今日新股申购信息列表

        :param session_id: 资金账户对应的session_id,登录时得到
        :param request_id: 用于用户定位查询响应的ID，由用户自定义
        :return: 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        """
        return super().QueryIPOInfoList(session_id, request_id)

    def QueryIPOQuotaInfo(self, session_id: int, request_id: int):
        """
        # 请求查询用户新股申购额度信息
        # @return 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        # @param session_id 资金账户对应的session_id,登录时得到
        # @param request_id 用于用户定位查询响应的ID，由用户自定义
        :param session_id:
        :param request_id:
        :return:
        """
        return super().QueryIPOQuotaInfo(session_id, request_id)

    def QueryOptionAuctionInfo(self, query_param: XTPQueryOptionAuctionInfoReqStruct,
                               session_id: int, request_id: int):
        """
        请求查询期权合约

        :param query_param: 需要查询的期权合约的筛选条件，可以为NULL（为NULL表示查询所有的期权合约）
        :param session_id: 资金账户对应的session_id,登录时得到
        :param request_id: 用于用户定位查询响应的ID，由用户自定义
        :return: 查询是否成功，“0”表示成功，非“0”表示出错，此时用户可以调用GetApiLastError(self,)来获取错误代码
        """
        return super().QueryOptionAuctionInfo(query_param, session_id, request_id)

    def OnDisconnected(self, session_id, reason):
        """
        当客户端的某个连接与交易后台通信连接断开时，该方法被调用。
        @param reason 错误原因，请与错误代码表对应
        @param session_id 资金账户对应的session_id，登录时得到
        @remark 用户主动调用logout导致的断线，不会触发此函数。api不会自动重连，当断线发生时，请用户自行选择后续操作，可以在此函数中调用Login重新登录，并更新session_id，此时用户收到的数据跟断线之前是连续的

        :param session_id: 
        :param reason: 
        :return: 
        """
        pass

    def OnError(self, error_info):
        """
        错误应答

        @remark 此函数只有在服务器发生错误时才会调用，一般无需用户处理

        :param error_info: 当服务器响应发生错误时的具体的错误代码和错误信息,当error_info为空，
        或者error_info.error_id为0时，表明没有错误
        :return: 
        """
        pass

    def OnOrderEvent(self, order_info, error_info, session_id):
        """
        报单通知
        @remark 每次订单状态更新时，都会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线，在订单未成交、全部成交、全部撤单、部分撤单、已拒绝这些状态时会有响应，对于部分成交的情况，请由订单的成交回报来自行确认。所有登录了此用户的客户端都将收到此用户的订单响应

        :param order_info: 订单响应具体信息，用户可以通过order_info.
                    order_xtp_id来管理订单，通过GetClientIDByXTPID() ==
                    client_id来过滤自己的订单，order_info.qty_left字段在订单为未成交、
                    部成、全成、废单状态时，表示此订单还没有成交的数量，在部撤、全撤状态时，
                    表示此订单被撤的数量。order_info.order_cancel_xtp_id为其所对应的撤单ID，
                    不为0时表示此单被撤成功
        :param error_info: 
        :param session_id: 
        :return: 
        """
        pass

    def OnTradeEvent(self, trade_info, session_id):
        """
        成交通知
        @remark 订单有成交发生的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线。所有登录了此用户的客户端都将收到此用户的成交回报。相关订单为部成状态，需要用户通过成交回报的成交数量来确定，OnOrderEvent()不会推送部成状态。

        :param trade_info: 成交回报的具体信息，用户可以通过trade_info.order_xtp_id
                        来管理订单，通过GetClientIDByXTPID() == client_id来过滤自己的订单。对于上交所，
                        exec_id可以唯一标识一笔成交。当发现2笔成交回报拥有相同的exec_id，
                        则可以认为此笔交易自成交了。对于深交所，exec_id是唯一的，暂时无此判断机制。
                        report_index+market字段可以组成唯一标识表示成交回报。
        :param session_id: 
        :return: 
        """
        pass

    def OnCancelOrderError(self, cancel_info, error_info, session_id):
        """
        撤单出错响应
        @remark 此响应只会在撤单发生错误时被回调

        :param cancel_info: 撤单具体信息，包括撤单的order_cancel_xtp_id和待撤单的order_xtp_id
        :param error_info: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryOrder(self, order_info, error_info, request_id, is_last, session_id):
        """
        请求查询报单响应
        @remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param order_info: 查询到的一个报单
        :param error_info: 
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryTrade(self, trade_info, error_info, request_id, is_last, session_id):
        """
        请求查询成交响应
        @remark 由于支持分时段查询，一个查询请求可能对应多个响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param trade_info: 查询到的一个成交回报
        :param error_info: 
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryPosition(self, position, error_info, request_id, is_last, session_id):
        """
        请求查询投资者持仓响应

        @remark 由于用户可能持有多个股票，一个查询请求可能对应多个响应，
        需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param position: 查询到的一只股票的持仓情况
        :param error_info: 
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryAsset(self, asset, error_info, request_id, is_last, session_id):
        """
        请求查询资金账户响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param asset: 查询到的资金账户情况
        :param error_info:
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryStructuredFund(self, fund_info, error_info, request_id, is_last, session_id):
        """
        请求查询分级基金信息响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param fund_info: 查询到的分级基金情况
        :param error_info: 
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryFundTransfer(self, fund_transfer_info, error_info, request_id, is_last, session_id):
        """
        请求查询资金划拨订单响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param fund_transfer_info: 查询到的资金账户情况
        :param error_info: 
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnFundTransfer(self, fund_transfer_info, error_info, session_id):
        """
        资金划拨通知

        @remark 当资金划拨订单有状态变化的时候，会被调用，需要快速返回，否则会堵塞后续消息，当堵塞严重时
        ，会触发断线。所有登录了此用户的客户端都将收到此用户的资金划拨通知。

        :param fund_transfer_info: 资金划拨通知的具体信息，用户可以通过
                                    fund_transfer_info.serial_id来管理订单，
                                    通过GetClientIDByXTPID() == client_id来过滤自己的订单。
        :param error_info: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryETF(self, etf_info, error_info, request_id, is_last, session_id):
        """
        请求查询ETF清单文件的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param etf_info: 查询到的ETF清单文件情况
        :param error_info: 
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryETFBasket(self, etf_component_info, error_info, request_id, is_last, session_id):
        """
        请求查询ETF股票篮的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param etf_component_info: 查询到的ETF合约的相关成分股信息
        :param error_info: 
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryIPOInfoList(self, ipo_info, error_info, request_id, is_last, session_id):
        """
        请求查询今日新股申购信息列表的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        @remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ipo_info: 查询到的今日新股申购的一只股票信息
        :param error_info: 查询今日新股申购信息列表发生错误时返回的错误信息
        :param request_id: 当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 此消息响应函数是否为request_id这条请求所对应的最后一个响应，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :param session_id:
        :return: 
        """
        pass

    def OnQueryIPOQuotaInfo(self, quota_info, error_info, request_id, is_last, session_id):
        """
        请求查询用户新股申购额度信息的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param quota_info: 查询到的用户某个市场的今日新股申购额度信息
        :param error_info: 查查询用户新股申购额度信息发生错误时返回的错误信息,当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param request_id: 此消息响应函数对应的请求ID
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass

    def OnQueryOptionAuctionInfo(self, option_info, error_info, request_id, is_last, session_id):
        """
        请求查询期权合约的响应，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param option_info: 查询到的期权合约情况
        :param error_info: 
        :param request_id: 
        :param is_last: 
        :param session_id: 
        :return: 
        """
        pass
