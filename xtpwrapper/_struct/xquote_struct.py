# encoding=utf-8
import ctypes
from ._struct import Base


class XTPSpecificTickerStruct(Base):
    """
    指定的合约
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('ticker', ctypes.c_char * 16),  # 合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
    ]

    def __init__(self, ticker=''):
        super(XTPSpecificTickerStruct, self).__init__()
        self.ticker = self._to_bytes(ticker)


class XTPMarketDataStockExData(Base):
    """
    股票、基金、债券等额外数据
    """
    _fields_ = [
        ('total_bid_qty', ctypes.c_int64),  # 委托买入总量(SH,SZ)
        ('total_ask_qty', ctypes.c_int64),  # 委托卖出总量(SH,SZ)
        ('ma_bid_price', ctypes.c_double),  # 加权平均委买价格(SH,SZ)
        ('ma_ask_price', ctypes.c_double),  # 加权平均委卖价格(SH,SZ)
        ('ma_bond_bid_price', ctypes.c_double),  # 债券加权平均委买价格(SH)
        ('ma_bond_ask_price', ctypes.c_double),  # 债券加权平均委卖价格(SH)
        ('yield_to_maturity', ctypes.c_double),  # 债券到期收益率(SH)
        ('iopv', ctypes.c_double),  # 基金实时参考净值(SH,SZ)
        ('etf_buy_count', ctypes.c_int32),  # ETF申购笔数(SH)
        ('etf_sell_count', ctypes.c_int32),  # ETF赎回笔数(SH)
        ('etf_buy_qty', ctypes.c_double),  # ETF申购数量(SH)
        ('etf_buy_money', ctypes.c_double),  # ETF申购金额(SH)
        ('etf_sell_qty', ctypes.c_double),  # ETF赎回数量(SH)
        ('etf_sell_money', ctypes.c_double),  # ETF赎回金额(SH)
        ('total_warrant_exec_qty', ctypes.c_double),  # 权证执行的总数量(SH)
        ('warrant_lower_price', ctypes.c_double),  # 权证跌停价格（元）(SH)
        ('warrant_upper_price', ctypes.c_double),  # 权证涨停价格（元）(SH)
        ('cancel_buy_count', ctypes.c_int32),  # 买入撤单笔数(SH)
        ('cancel_sell_count', ctypes.c_int32),  # 卖出撤单笔数(SH)
        ('cancel_buy_qty', ctypes.c_double),  # 买入撤单数量(SH)
        ('cancel_sell_qty', ctypes.c_double),  # 卖出撤单数量(SH)
        ('cancel_buy_money', ctypes.c_double),  # 买入撤单金额(SH)
        ('cancel_sell_money', ctypes.c_double),  # 卖出撤单金额(SH)
        ('total_buy_count', ctypes.c_int64),  # 买入总笔数(SH)
        ('total_sell_count', ctypes.c_int64),  # 卖出总笔数(SH)
        ('duration_after_buy', ctypes.c_int32),  # 买入委托成交最大等待时间(SH)
        ('duration_after_sell', ctypes.c_int32),  # 卖出委托成交最大等待时间(SH)
        ('num_bid_orders', ctypes.c_int32),  # 买方委托价位数(SH)
        ('num_ask_orders', ctypes.c_int32),  # 卖方委托价位数(SH)
        ('pre_iopv', ctypes.c_double),  # 基金T-1日净值(SZ)
        ('r1', ctypes.c_int64),  # 预留
        ('r2', ctypes.c_int64),  # 预留
    ]

    def __init__(self, total_bid_qty='', total_ask_qty='', ma_bid_price=0.0, ma_ask_price=0.0, ma_bond_bid_price=0.0,
                 ma_bond_ask_price=0.0, yield_to_maturity=0.0, iopv=0.0, etf_buy_count='', etf_sell_count='',
                 etf_buy_qty=0.0, etf_buy_money=0.0, etf_sell_qty=0.0, etf_sell_money=0.0, total_warrant_exec_qty=0.0,
                 warrant_lower_price=0.0, warrant_upper_price=0.0, cancel_buy_count='', cancel_sell_count='',
                 cancel_buy_qty=0.0, cancel_sell_qty=0.0, cancel_buy_money=0.0, cancel_sell_money=0.0,
                 total_buy_count='', total_sell_count='', duration_after_buy='', duration_after_sell='',
                 num_bid_orders='', num_ask_orders='', pre_iopv=0.0, r1='', r2=''):
        super(XTPMarketDataStockExData, self).__init__()
        self.total_bid_qty = int(total_bid_qty)
        self.total_ask_qty = int(total_ask_qty)
        self.ma_bid_price = float(ma_bid_price)
        self.ma_ask_price = float(ma_ask_price)
        self.ma_bond_bid_price = float(ma_bond_bid_price)
        self.ma_bond_ask_price = float(ma_bond_ask_price)
        self.yield_to_maturity = float(yield_to_maturity)
        self.iopv = float(iopv)
        self.etf_buy_count = int(etf_buy_count)
        self.etf_sell_count = int(etf_sell_count)
        self.etf_buy_qty = float(etf_buy_qty)
        self.etf_buy_money = float(etf_buy_money)
        self.etf_sell_qty = float(etf_sell_qty)
        self.etf_sell_money = float(etf_sell_money)
        self.total_warrant_exec_qty = float(total_warrant_exec_qty)
        self.warrant_lower_price = float(warrant_lower_price)
        self.warrant_upper_price = float(warrant_upper_price)
        self.cancel_buy_count = int(cancel_buy_count)
        self.cancel_sell_count = int(cancel_sell_count)
        self.cancel_buy_qty = float(cancel_buy_qty)
        self.cancel_sell_qty = float(cancel_sell_qty)
        self.cancel_buy_money = float(cancel_buy_money)
        self.cancel_sell_money = float(cancel_sell_money)
        self.total_buy_count = int(total_buy_count)
        self.total_sell_count = int(total_sell_count)
        self.duration_after_buy = int(duration_after_buy)
        self.duration_after_sell = int(duration_after_sell)
        self.num_bid_orders = int(num_bid_orders)
        self.num_ask_orders = int(num_ask_orders)
        self.pre_iopv = float(pre_iopv)
        self.r1 = int(r1)
        self.r2 = int(r2)


class XTPMarketDataOptionExData(Base):
    """
    期权额外数据
    """
    _fields_ = [
        ('auction_price', ctypes.c_double),  # 波段性中断参考价(SH)
        ('auction_qty', ctypes.c_int64),  # 波段性中断集合竞价虚拟匹配量(SH)
        ('last_enquiry_time', ctypes.c_int64),  # 最近询价时间(SH)
    ]

    def __init__(self, auction_price=0.0, auction_qty='', last_enquiry_time=''):
        super(XTPMarketDataOptionExData, self).__init__()
        self.auction_price = float(auction_price)
        self.auction_qty = int(auction_qty)
        self.last_enquiry_time = int(last_enquiry_time)


class _XTPMarketUion(ctypes.Union):
    """
    """
    _fields_ = [
        ("stk", XTPMarketDataStockExData),
        ("opt", XTPMarketDataOptionExData)
    ]


class XTPMarketDataStruct(Base):
    """
    行情
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('ticker', ctypes.c_char * 16),  # 合约代码（不包含交易所信息），不带空格，以'\0'结尾
        ('last_price', ctypes.c_double),  # 最新价
        ('pre_close_price', ctypes.c_double),  # 昨收盘
        ('open_price', ctypes.c_double),  # 今开盘
        ('high_price', ctypes.c_double),  # 最高价
        ('low_price', ctypes.c_double),  # 最低价
        ('close_price', ctypes.c_double),  # 今收盘
        ('pre_total_long_positon', ctypes.c_int64),  # 昨日持仓量(张)(目前未填写)
        ('total_long_positon', ctypes.c_int64),  # 持仓量(张)
        ('pre_settl_price', ctypes.c_double),  # 昨日结算价
        ('settl_price', ctypes.c_double),  # 今日结算价
        ('upper_limit_price', ctypes.c_double),  # 涨停价
        ('lower_limit_price', ctypes.c_double),  # 跌停价
        ('pre_delta', ctypes.c_double),  # 预留
        ('curr_delta', ctypes.c_double),  # 预留
        ('data_time', ctypes.c_int64),  # 时间类，格式为YYYYMMDDHHMMSSsss
        ('qty', ctypes.c_int64),  # 数量，为总成交量（单位股，与交易所一致）
        ('turnover', ctypes.c_double),  # 成交金额，为总成交金额（单位元，与交易所一致）
        ('avg_price', ctypes.c_double),  # 当日均价=(turnover/qty)
        ('bid', ctypes.c_double * 10),  # 十档申买价
        ('ask', ctypes.c_double * 10),  # 十档申卖价
        ('bid_qty', ctypes.c_int64 * 10),  # 十档申买量
        ('ask_qty', ctypes.c_int64 * 10),  # 十档申卖量
        ('trades_count', ctypes.c_int64),  # 成交笔数
        ('ticker_status', ctypes.c_char * 8),  # 当前交易状态说明
        ('data_type', ctypes.c_int),  # 决定了union是哪种数据类型
        ('r4', ctypes.c_int32),  # 预留

        ("_u", _XTPMarketUion)
    ]
    _anonymous_ = ("_u",)

    def __init__(self, ticker='', last_price=0.0, pre_close_price=0.0, open_price=0.0, high_price=0.0, low_price=0.0,
                 close_price=0.0, pre_total_long_positon='', total_long_positon='', pre_settl_price=0.0,
                 settl_price=0.0, upper_limit_price=0.0, lower_limit_price=0.0, pre_delta=0.0, curr_delta=0.0,
                 data_time='', qty='', turnover=0.0, avg_price=0.0, bid=0.0, ask=0.0, bid_qty='', ask_qty='',
                 trades_count='', ticker_status='', r4=''):
        super(XTPMarketDataStruct, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.last_price = float(last_price)
        self.pre_close_price = float(pre_close_price)
        self.open_price = float(open_price)
        self.high_price = float(high_price)
        self.low_price = float(low_price)
        self.close_price = float(close_price)
        self.pre_total_long_positon = int(pre_total_long_positon)
        self.total_long_positon = int(total_long_positon)
        self.pre_settl_price = float(pre_settl_price)
        self.settl_price = float(settl_price)
        self.upper_limit_price = float(upper_limit_price)
        self.lower_limit_price = float(lower_limit_price)
        self.pre_delta = float(pre_delta)
        self.curr_delta = float(curr_delta)
        self.data_time = int(data_time)
        self.qty = int(qty)
        self.turnover = float(turnover)
        self.avg_price = float(avg_price)
        self.bid = float(bid)
        self.ask = float(ask)
        self.bid_qty = int(bid_qty)
        self.ask_qty = int(ask_qty)
        self.trades_count = int(trades_count)
        self.ticker_status = self._to_bytes(ticker_status)
        self.r4 = int(r4)


class XTPQuoteStaticInfo(Base):
    """
    股票行情静态信息
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('ticker', ctypes.c_char * 16),  # 合约代码（不包含交易所信息），不带空格，以'\0'结尾
        ('ticker_name', ctypes.c_char * 64),  # 合约名称
        ('ticker_type', ctypes.c_int),  # 合约类型
        ('pre_close_price', ctypes.c_double),  # 昨收盘
        ('upper_limit_price', ctypes.c_double),  # 涨停板价
        ('lower_limit_price', ctypes.c_double),  # 跌停板价
        ('price_tick', ctypes.c_double),  # 最小变动价位
        ('buy_qty_unit', ctypes.c_int32),  # 合约最小交易量(买)
        ('sell_qty_unit', ctypes.c_int32),  # 合约最小交易量(卖)
    ]

    # def __init__(self, ticker='', ticker_name='', pre_close_price=0.0, upper_limit_price=0.0, lower_limit_price=0.0,
    #              price_tick=0.0, buy_qty_unit='', sell_qty_unit=''):
    #     super(XTPQuoteStaticInfo, self).__init__()
    #     self.ticker = self._to_bytes(ticker)
    #     self.ticker_name = self._to_bytes(ticker_name)
    #     self.pre_close_price = float(pre_close_price)
    #     self.upper_limit_price = float(upper_limit_price)
    #     self.lower_limit_price = float(lower_limit_price)
    #     self.price_tick = float(price_tick)
    #     self.buy_qty_unit = int(buy_qty_unit)
    #     self.sell_qty_unit = int(sell_qty_unit)


class OrderBookStruct(Base):
    """
    定单薄
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('ticker', ctypes.c_char * 16),  # 合约代码（不包含交易所信息），不带空格，以'\0'结尾
        ('last_price', ctypes.c_double),  # 最新价
        ('qty', ctypes.c_int64),  # 数量，为总成交量
        ('turnover', ctypes.c_double),  # 成交金额，为总成交金额
        ('trades_count', ctypes.c_int64),  # 成交笔数
        ('bid', ctypes.c_double * 10),  # 十档申买价
        ('ask', ctypes.c_double * 10),  # 十档申卖价
        ('bid_qty', ctypes.c_int64 * 10),  # 十档申买量
        ('ask_qty', ctypes.c_int64 * 10),  # 十档申卖量
        ('data_time', ctypes.c_int64),  # 时间类
    ]

    def __init__(self, ticker='', last_price=0.0, qty='', turnover=0.0, trades_count='', bid=0.0, ask=0.0, bid_qty='',
                 ask_qty='', data_time=''):
        super(OrderBookStruct, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.last_price = float(last_price)
        self.qty = int(qty)
        self.turnover = float(turnover)
        self.trades_count = int(trades_count)
        self.bid = float(bid)
        self.ask = float(ask)
        self.bid_qty = int(bid_qty)
        self.ask_qty = int(ask_qty)
        self.data_time = int(data_time)


class XTPTickByTickEntrust(Base):
    """
    逐笔委托(仅适用深交所)
    """
    _fields_ = [
        ('channel_no', ctypes.c_int32),  # 频道代码
        ('seq', ctypes.c_int64),  # 委托序号(在同一个channel_no内唯一，从1开始连续)
        ('price', ctypes.c_double),  # 委托价格
        ('qty', ctypes.c_int64),  # 委托数量
        ('side', ctypes.c_char),  # '1':买; '2':卖; 'G':借入; 'F':出借
        ('ord_type', ctypes.c_char),  # 订单类别: '1': 市价; '2': 限价; 'U': 本方最优
    ]

    def __init__(self, channel_no='', seq='', price=0.0, qty='', side='', ord_type=''):
        super(XTPTickByTickEntrust, self).__init__()
        self.channel_no = int(channel_no)
        self.seq = int(seq)
        self.price = float(price)
        self.qty = int(qty)
        self.side = self._to_bytes(side)
        self.ord_type = self._to_bytes(ord_type)


class XTPTickByTickTrade(Base):
    """
    逐笔成交
    """
    _fields_ = [
        ('channel_no', ctypes.c_int32),  # 频道代码
        ('seq', ctypes.c_int64),  # 委托序号(在同一个channel_no内唯一，从1开始连续)
        ('price', ctypes.c_double),  # 成交价格
        ('qty', ctypes.c_int64),  # 成交量
        ('money', ctypes.c_double),  # 成交金额(仅适用上交所)
        ('bid_no', ctypes.c_int64),  # 买方订单号
        ('ask_no', ctypes.c_int64),  # 卖方订单号
        ('trade_flag', ctypes.c_char),  # SH: 内外盘标识('B':主动买; 'S':主动卖; 'N':未知) SZ: 成交标识('4':撤; 'F':成交)
    ]

    def __init__(self, channel_no='', seq='', price=0.0, qty='', money=0.0, bid_no='', ask_no='', trade_flag=''):
        super(XTPTickByTickTrade, self).__init__()
        self.channel_no = int(channel_no)
        self.seq = int(seq)
        self.price = float(price)
        self.qty = int(qty)
        self.money = float(money)
        self.bid_no = int(bid_no)
        self.ask_no = int(ask_no)
        self.trade_flag = self._to_bytes(trade_flag)


class _XTPTickByTickUnion(ctypes.Union):
    _fields_ = [
        ("entrust", XTPTickByTickEntrust),
        ("trade", XTPTickByTickTrade)
    ]


class XTPTickByTickStruct(Base):
    """
    逐笔数据信息
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('ticker', ctypes.c_char * 16),  # 合约代码（不包含交易所信息），不带空格，以'\0'结尾
        ('seq', ctypes.c_int64),  # 预留
        ('data_time', ctypes.c_int64),  # 委托时间or成交时间
        ('type', ctypes.c_int),  # 委托or成交
        ("_u", _XTPTickByTickUnion)
    ]
    _anonymous_ = ("_u",)

    def __init__(self, ticker='', seq='', data_time=''):
        super(XTPTickByTickStruct, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.seq = int(seq)
        self.data_time = int(data_time)


class XTPTickerPriceInfo(Base):
    """
    供查询的最新信息
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('ticker', ctypes.c_char * 16),  # 合约代码（不包含交易所信息），不带空格，以'\0'结尾
        ('last_price', ctypes.c_double),  # 最新价
    ]

    def __init__(self, ticker='', last_price=0.0):
        super(XTPTickerPriceInfo, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.last_price = float(last_price)
