# encoding:utf-8
from xtpwrapper.quote_api import QuoteWrapper
from .xtp_enum import XTP_EXCHANGE_TYPE
from .xtp_enum import XTP_LOG_LEVEL


class QuoteAPI(QuoteWrapper):

    def CreateQuote(self, client_id: int, save_file_path: str, log_level: XTP_LOG_LEVEL):
        """
        创建QuoteApi
        如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，但是对于同一账户，
        相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接

        :param client_id: (必须输入）用于区分同一用户的不同客户端，由用户自定义
        :param save_file_path: （必须输入）存贮订阅信息文件的目录，请设定一个有可写权限的真实存在的路径
        :param log_level: 日志输出级别
        :return:
        """
        super().CreateQuote(client_id, save_file_path.encode(), log_level)

    def Release(self):
        """
        删除接口对象本身
        不再使用本接口对象时,调用该函数删除接口对象
        :return: None
        """
        super().Release()

    def GetTradingDay(self):
        """
        获取当前交易日
        只有登录成功后,才能得到正确的交易日
        :return: 获取到的交易日
        """
        day = super().GetTradingDay()
        return day.decode()

    def GetApiVersion(self):
        """
        获取API的发行版本号
        :return: 返回api发行版本号
        """
        version = super().GetApiVersion()
        return version.decode()

    def GetApiLastError(self):
        """
        获取API的系统错误
        可以在调用api接口失败时调用，例如login失败时

        :return: 返回的错误信息，可以在Login、Logout、订阅、取消订阅失败时调用，获取失败的原因
        """
        return super().GetApiLastError()

    def SetUDPBufferSize(self, buff_size: int):
        """
        设置采用UDP方式连接时的接收缓冲区大小
        需要在Login之前调用，默认大小和最小设置均为64MB。此缓存大小单位为MB，请输入2的次方数，例如128MB请输入128。
        :param buff_size: int
        :return: None
        """
        super().SetUDPBufferSize(buff_size)

    def SetHeartBeatInterval(self, interval: int):
        """
        设置心跳检测时间间隔，单位为秒
        此函数必须在Login之前调用
        :param interval: 心跳检测时间间隔，单位为秒
        :return:
        """
        super().SetHeartBeatInterval(interval)

    def SubscribeMarketData(self, ticks: list, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅行情，包括股票、指数和期权。
        可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情

        :param ticks: 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        :param exchange_id: 交易所代码
        :return: int 订阅接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super().SubscribeMarketData(ticks, exchange_id)

    def UnSubscribeMarketData(self, ticks: list, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订行情，包括股票、指数和期权。

        @remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅行情接口配套使用

        :param ticks: 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        :param exchange_id: 交易所代码
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super().UnSubscribeMarketData(ticks, exchange_id)

    def SubscribeOrderBook(self, ticks: list, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅行情订单簿，包括股票、指数和期权。

        @remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情(仅支持深交所)

        :param ticks: 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        :param exchange_id: 交易所代码
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super().SubscribeOrderBook(ticks, exchange_id)

    def UnSubscribeOrderBook(self, ticks: list, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订行情订单簿，包括股票、指数和期权。

        @remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅行情订单簿接口配套使用

        :param ticks: 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        :param exchange_id: 交易所代码
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super().UnSubscribeOrderBook(ticks, exchange_id)

    def SubscribeTickByTick(self, ticks: list, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅逐笔行情，包括股票、指数和期权。

        @remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情

        :param ticks: 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        :param exchange_id: 交易所代码
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super().SubscribeTickByTick(ticks, exchange_id)

    def UnSubscribeTickByTick(self, ticks: list, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订逐笔行情，包括股票、指数和期权。
        @remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅逐笔行情接口配套使用

        :param ticks: 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        :param exchange_id: 交易所代码
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super().UnSubscribeTickByTick(ticks, exchange_id)

    def SubscribeAllMarketData(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅全市场的股票行情
        @remark 需要与全市场退订行情接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().SubscribeAllMarketData(exchange_id)

    def UnSubscribeAllMarketData(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订全市场的股票行情
        @remark 需要与订阅全市场行情接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().UnSubscribeAllMarketData(exchange_id)

    def SubscribeAllOrderBook(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅全市场的股票行情订单簿
        @remark 需要与全市场退订行情订单簿接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().SubscribeAllOrderBook(exchange_id)

    def UnSubscribeAllOrderBook(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订全市场的股票行情订单簿
        @remark 需要与订阅全市场行情订单簿接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().UnSubscribeAllOrderBook(exchange_id)

    def SubscribeAllTickByTick(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅全市场的股票逐笔行情
        @remark 需要与全市场退订逐笔行情接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().SubscribeAllTickByTick(exchange_id)

    def UnSubscribeAllTickByTick(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订全市场的股票逐笔行情
        @remark 需要与订阅全市场逐笔行情接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().UnSubscribeAllTickByTick(exchange_id)

    def Login(self, ip: str, port: int, user: str, password: str, sock_type: int = 1):
        """
        用户登录请求
        “0”表示登录成功，“-1”表示连接服务器出错，此时用户可以调用GetApiLastError()来获取错误代码，“-2”表示已存在连接，不允许重复登录，如果需要重连，请先logout，“-3”表示输入有错误
        @remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只能有一个连接

        :param ip: 服务器ip地址，类似“127.0.0.1”
        :param port: 服务器端口号
        :param user: 登陆用户名
        :param password: 登陆密码
        :param sock_type: “1”代表TCP，“2”代表UDP
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """

        return super().Login(ip.encode("utf-8"), port, user.encode("utf-8"),
                             password.encode("utf-8"), sock_type)

    def Logout(self):
        """
        登出请求
        “0”表示登出成功，非“0”表示登出出错，此时用户可以调用GetApiLastError()来获取错误代码
        @remark 此函数为同步阻塞式，不需要异步等待登出，当函数返回即可进行后续操作

        :return:
        """
        return super().Logout()

    def QueryAllTickers(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        获取当前交易日可交易合约

        :param exchange_id: 交易所代码
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().QueryAllTickers(exchange_id)

    def QueryTickersPriceInfo(self, ticks: list, exchange_id: XTP_EXCHANGE_TYPE):
        """
        获取合约的最新价格信息

        :param ticks:
        :param exchange_id: 交易所代码
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]

        return super().QueryTickersPriceInfo(ticks, exchange_id)

    def QueryAllTickersPriceInfo(self):
        """
        获取所有合约的最新价格信息

        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().QueryAllTickersPriceInfo()

    def SubscribeAllOptionMarketData(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅全市场的期权行情
        @remark 需要与全市场退订期权行情接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().SubscribeAllOptionMarketData(exchange_id)

    def UnSubscribeAllOptionMarketData(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订全市场的期权行情
        @remark 需要与订阅全市场期权行情接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().UnSubscribeAllOptionMarketData(exchange_id)

    def SubscribeAllOptionOrderBook(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅全市场的期权行情订单簿
        @remark 需要与全市场退订期权行情订单簿接口配套使用

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().SubscribeAllOptionOrderBook(exchange_id)

    def UnSubscribeAllOptionOrderBook(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订全市场的期权行情订单簿
        @remark 需要与订阅全市场期权行情订单簿接口配套使用

        :param exchange_id: exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: “0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().UnSubscribeAllOptionOrderBook(exchange_id)

    def SubscribeAllOptionTickByTick(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        订阅全市场的期权逐笔行情
        @remark 需要与全市场退订期权逐笔行情接口配套使用
        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: 订阅全市场期权逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().SubscribeAllOptionTickByTick(exchange_id)

    def UnSubscribeAllOptionTickByTick(self, exchange_id: XTP_EXCHANGE_TYPE):
        """
        退订全市场的期权逐笔行情
        @remark 需要与订阅全市场期权逐笔行情接口配套使用

        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :return: 退订全市场期权逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        """
        return super().UnSubscribeAllOptionTickByTick(exchange_id)

    def OnDisconnected(self, reason):
        """
        当客户端与行情后台通信连接断开时，该方法被调用。
        @remark api不会自动重连，当断线发生时，请用户自行选择后续操作。可以在此函数中调用Login重新登录。注意用户重新登录后，需要重新订阅行情
        :param reason: 错误原因，请与错误代码表对应
        :return:
        """
        pass

    def OnError(self, error_info):
        """
        错误应答
        @param error_info 当服务器响应发生错误时的具体的错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        @remark 此函数只有在服务器发生错误时才会调用，一般无需用户处理
        :param error_info:
        :return:
        """
        pass

    def OnSubMarketData(self, ticker, error_info, is_last):
        """
        订阅行情应答，包括股票、指数和期权

        @remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :param ticker: 详细的合约订阅情况
        :param error_info: 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnUnSubMarketData(self, ticker, error_info, is_last):
        """
        退订行情应答，包括股票、指数和期权

        @remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :param ticker: 详细的合约取消订阅情况
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnDepthMarketData(self, market_data, bid1_qty, bid1_count, max_bid1_count, ask1_qty, ask1_count,
                          max_ask1_count):
        """
        深度行情通知，包含买一卖一队列
        @remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :param market_data: 行情数据
        :param bid1_qty: 买一队列数据
        :param bid1_count: 买一队列的有效委托笔数
        :param max_bid1_count: 买一队列总委托笔数
        :param ask1_qty: 卖一队列数据
        :param ask1_count: 卖一队列的有效委托笔数
        :param max_ask1_count: 卖一队列总委托笔数
        :return:
        """
        pass

    def OnSubOrderBook(self, ticker, error_info, is_last):
        """
        订阅行情订单簿应答，包括股票、指数和期权

        @remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ticker: 详细的合约订阅情况
        :param error_info: 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnUnSubOrderBook(self, ticker, error_info, is_last):
        """
        退订行情订单簿应答，包括股票、指数和期权

        @remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ticker: 详细的合约取消订阅情况
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnOrderBook(self, order_book):
        """
        行情订单簿通知，包括股票、指数和期权

        :param order_book: 行情订单簿数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :return:
        """
        pass

    def OnSubTickByTick(self, ticker, error_info, is_last):
        """
        订阅逐笔行情应答，包括股票、指数和期权

        @remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ticker: 详细的合约订阅情况
        :param error_info: 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnUnSubTickByTick(self, ticker, error_info, is_last):
        """
        退订逐笔行情应答，包括股票、指数和期权

        @remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线

        :param ticker: 详细的合约取消订阅情况
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnTickByTick(self, tbt_data):
        """
        逐笔行情通知，包括股票、指数和期权

        需要根据type来区分是逐笔委托还是逐笔成交，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        :param tbt_data: 逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，
        :return:
        """
        pass

    def OnSubscribeAllMarketData(self, exchange_id, error_info):
        """
        订阅全市场的股票行情应答

        @remark 需要快速返回

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，
                            XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllMarketData(self, exchange_id, error_info):
        """
        退订全市场的股票行情应答

        @remark 需要快速返回

        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnSubscribeAllOrderBook(self, exchange_id, error_info):
        """
        订阅全市场的股票行情订单簿应答

        @remark 需要快速返回

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllOrderBook(self, exchange_id, error_info):
        """
        退订全市场的股票行情订单簿应答

        @remark 需要快速返回

        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnSubscribeAllTickByTick(self, exchange_id, error_info):
        """
        订阅全市场的股票逐笔行情应答

        @remark 需要快速返回
        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllTickByTick(self, exchange_id, error_info):
        """
        退订全市场的股票逐笔行情应答

        @remark 需要快速返回
        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnQueryAllTickers(self, ticker_info, error_info, is_last):
        """
        查询可交易合约的应答

        :param ticker_info: 可交易合约信息
        :param error_info: 查询可交易合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次查询可交易合约的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnQueryTickersPriceInfo(self, ticker_info, error_info, is_last):
        """
        查询合约的最新价格信息应答

        :param ticker_info: 合约的最新价格信息
        :param error_info: 查询合约的最新价格信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :param is_last: 是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        :return:
        """
        pass

    def OnSubscribeAllOptionMarketData(self, exchange_id, error_info):
        """
        订阅全市场的期权行情应答

        @remark 需要快速返回

        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllOptionMarketData(self, exchange_id, error_info):
        """
        退订全市场的期权行情应答

        @remark 需要快速返回

        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnSubscribeAllOptionOrderBook(self, exchange_id, error_info):
        """
        订阅全市场的期权行情订单簿应答

        @remark 需要快速返回
        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllOptionOrderBook(self, exchange_id, error_info):
        """
        退订全市场的期权行情订单簿应答

        @remark 需要快速返回
        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnSubscribeAllOptionTickByTick(self, exchange_id, error_info):
        """
        订阅全市场的期权逐笔行情应答

        @remark 需要快速返回
        :param exchange_id: 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass

    def OnUnSubscribeAllOptionTickByTick(self, exchange_id, error_info):
        """
        退订全市场的期权逐笔行情应答

        @remark 需要快速返回
        :param exchange_id: 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        :param error_info: 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        :return:
        """
        pass
