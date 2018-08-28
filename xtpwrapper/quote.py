from xtpwrapper.quote_api import QuoteWrapper


class Quote(QuoteWrapper):

    def CreateQuote(self, client_id, save_file_path, log_level: int):
        """

        :param client_id:
        :param save_file_path:
        :param log_level:
        :return:
        """
        super(Quote, self).CreateQuote(client_id,
                                       save_file_path.encode(), log_level)

    def Release(self):
        """
        :return:
        """
        super(Quote,self).Release()

    def GetTradingDay(self):
        """

        :return:
        """
        day = super(Quote, self).GetTradingDay()
        return day.decode()

    def GetApiVersion(self):
        """

        :return:
        """
        return super(Quote, self).GetApiVersion()

    def GetApiLastError(self):
        """
        :return:
        """
        return super(Quote, self).GetApiLastError()

    def SetUDPBufferSize(self, buff_size):
        """

        :param buff_size:
        :return: None
        """
        super(Quote, self).SetUDPBufferSize(buff_size)

    # def Register(self):
    #     """
    #     :return:
    #     """
    #     super(Quote, self).Register()

    def SetHeartBeatInterval(self, interval):
        """

        :param interval:
        :return:
        """
        super(Quote, self).SetHeartBeatInterval(interval)

    def SubscribeMarketData(self, ticks, exchange_id):
        """

        :param ticks:
        :param exchange_id:
        :return:
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super(Quote, self).SubscribeAllMarketData(ticks, exchange_id)

    def UnSubscribeMarketData(self, ticks, exchange_id):
        """

        :param ticks:
        :param exchange_id:
        :return:
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super(Quote, self).UnSubscribeMarketData(ticks, exchange_id)

    def SubscribeOrderBook(self, ticks, exchange_id):
        """

        :param ticks:
        :param exchange_id:
        :return:
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super(Quote, self).SubscribeOrderBook(ticks, exchange_id)

    def UnSubscribeOrderBook(self, ticks, exchange_id):
        """

        :param ticks:
        :param exchange_id:
        :return:
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super(Quote, self).UnSubscribeOrderBook(ticks, exchange_id)

    def SubscribeTickByTick(self, ticks, exchange_id):
        """

        :param ticks:
        :param exchange_id:
        :return:
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super(Quote, self).SubscribeTickByTick(ticks, exchange_id)

    def UnSubscribeTickByTick(self, ticks, exchange_id):
        """

        :param ticks:
        :param exchange_id:
        :return:
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]
        return super(Quote, self).UnSubscribeTickByTick(ticks, exchange_id)

    def SubscribeAllMarketData(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).SubscribeAllMarketData(exchange_id)

    def UnSubscribeAllMarketData(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).UnSubscribeAllMarketData(exchange_id)

    def SubscribeAllOrderBook(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).SubscribeAllOrderBook(exchange_id)

    def UnSubscribeAllOrderBook(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).UnSubscribeAllOrderBook(exchange_id)

    def SubscribeAllTickByTick(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).SubscribeAllTickByTick(exchange_id)

    def UnSubscribeAllTickByTick(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).UnSubscribeAllTickByTick(exchange_id)

    def Login(self, ip, port, user, password, sock_type):
        """

        :param ip:
        :param port:
        :param user:
        :param password:
        :param sock_type:
        :return:
        """
        return super(Quote, self).Login(ip, port, user, password, sock_type)

    def Logout(self):
        """

        :return:
        """
        return super(Quote, self).Logout()

    def QueryAllTickers(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).QueryAllTickers(exchange_id)

    def QueryTickersPriceInfo(self, ticks, exchange_id):
        """

        :param ticks:
        :param exchange_id:
        :return:
        """
        ticks = [bytes(item, encoding="utf-8") for item in ticks]

        return super(Quote, self).QueryAllTickersPriceInfo(ticks, exchange_id)

    def QueryAllTickersPriceInfo(self):
        """

        :return:
        """
        return super(Quote, self).QueryAllTickersPriceInfo()

    def SubscribeAllOptionMarketData(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).SubscribeAllOptionMarketData(exchange_id)

    def UnSubscribeAllOptionMarketData(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).UnSubscribeAllOptionMarketData(exchange_id)

    def SubscribeAllOptionOrderBook(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).SubscribeAllOptionOrderBook(exchange_id)

    def UnSubscribeAllOptionOrderBook(self, exchange_id):
        """
        :param exchange_id:
        :return:
        """
        return super(Quote, self).UnSubscribeAllOptionOrderBook(exchange_id)

    def SubscribeAllOptionTickByTick(self, exchange_id):
        """
        :param exchange_id:
        :return:
        """
        return super(Quote, self).SubscribeAllOptionTickByTick(exchange_id)

    def UnSubscribeAllOptionTickByTick(self, exchange_id):
        """

        :param exchange_id:
        :return:
        """
        return super(Quote, self).UnSubscribeAllOptionTickByTick(exchange_id)



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

    #  订阅行情订单簿应答，包括股票、指数和期权
    #  @param ticker 详细的合约订阅情况
    #  @param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    #  @remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    def OnSubOrderBook(self, ticker, error_info, is_last):
        """

        :param ticker:
        :param error_info:
        :param is_last:
        :return:
        """
        pass

    #  退订行情订单簿应答，包括股票、指数和期权
    #  @param ticker 详细的合约取消订阅情况
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    #  @remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    def OnUnSubOrderBook(self, ticker, error_info, is_last):
        """

        :param ticker:
        :param error_info:
        :param is_last:
        :return:
        """
        pass

    #  行情订单簿通知，包括股票、指数和期权
    #  @param order_book 行情订单簿数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    def OnOrderBook(self, order_book):
        """

        :param order_book:
        :return:
        """
        pass

    #  订阅逐笔行情应答，包括股票、指数和期权
    #  @param ticker 详细的合约订阅情况
    #  @param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    #  @remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    def OnSubTickByTick(self, ticker, error_info, is_last):
        """

        :param ticker:
        :param error_info:
        :param is_last:
        :return:
        """
        pass

    #  退订逐笔行情应答，包括股票、指数和期权
    #  @param ticker 详细的合约取消订阅情况
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    #  @remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    def OnUnSubTickByTick(self, ticker, error_info, is_last):
        """

        :param ticker:
        :param error_info:
        :param is_last:
        :return:
        """
        pass

    #  逐笔行情通知，包括股票、指数和期权
    #  @param tbt_data 逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，
    #  需要根据type来区分是逐笔委托还是逐笔成交，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
    def OnTickByTick(self, tbt_data):
        """

        :param tbt_data:
        :return:
        """
        pass

    #  订阅全市场的股票行情应答
    #  @param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnSubscribeAllMarketData(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  退订全市场的股票行情应答
    #  @param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnUnSubscribeAllMarketData(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  订阅全市场的股票行情订单簿应答
    #  @param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnSubscribeAllOrderBook(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  退订全市场的股票行情订单簿应答
    #  @param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnUnSubscribeAllOrderBook(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  订阅全市场的股票逐笔行情应答
    #  @param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnSubscribeAllTickByTick(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  退订全市场的股票逐笔行情应答
    #  @param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnUnSubscribeAllTickByTick(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  查询可交易合约的应答
    #  @param ticker_info 可交易合约信息
    #  @param error_info 查询可交易合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @param is_last 是否此次查询可交易合约的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    def OnQueryAllTickers(self, ticker_info, error_info, is_last):
        """

        :param ticker_info:
        :param error_info:
        :param is_last:
        :return:
        """
        pass

    #  查询合约的最新价格信息应答
    #  @param ticker_info 合约的最新价格信息
    #  @param error_info 查询合约的最新价格信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @param is_last 是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
    def OnQueryTickersPriceInfo(self, ticker_info, error_info, is_last):
        """

        :param ticker_info:
        :param error_info:
        :param is_last:
        :return:
        """
        pass

    #  订阅全市场的期权行情应答
    #  @param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnSubscribeAllOptionMarketData(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  退订全市场的期权行情应答
    #  @param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnUnSubscribeAllOptionMarketData(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  订阅全市场的期权行情订单簿应答
    #  @param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnSubscribeAllOptionOrderBook(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  退订全市场的期权行情订单簿应答
    #  @param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnUnSubscribeAllOptionOrderBook(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  订阅全市场的期权逐笔行情应答
    #  @param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnSubscribeAllOptionTickByTick(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass

    #  退订全市场的期权逐笔行情应答
    #  @param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
    #  @param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
    #  @remark 需要快速返回
    def OnUnSubscribeAllOptionTickByTick(self, exchange_id, error_info):
        """

        :param exchange_id:
        :param error_info:
        :return:
        """
        pass
