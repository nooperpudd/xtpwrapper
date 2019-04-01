# encoding=utf-8
import ctypes

from . import StructBase, UnionBase


class XTPSpecificTickerStruct(StructBase):
    """
    指定的合约
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('ticker', ctypes.c_char * 16),  # 合约代码（不包含交易所信息）例如"600000"，不带空格，以'\0'结尾
    ]


class _XTPMarketDataStockExData(StructBase):
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


class _XTPMarketDataOptionExData(StructBase):
    """
    期权额外数据
    """
    _fields_ = [
        ('auction_price', ctypes.c_double),  # 波段性中断参考价(SH)
        ('auction_qty', ctypes.c_int64),  # 波段性中断集合竞价虚拟匹配量(SH)
        ('last_enquiry_time', ctypes.c_int64),  # 最近询价时间(SH)
    ]


class _XTPMarketUion(UnionBase):
    """
    """
    _fields_ = [
        ("stk", _XTPMarketDataStockExData),
        ("opt", _XTPMarketDataOptionExData)
    ]


class XTPMarketDataStruct(StructBase):
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


class XTPQuoteStaticInfo(StructBase):
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


class OrderBookStruct(StructBase):
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


class _XTPTickByTickEntrust(StructBase):
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


class _XTPTickByTickTrade(StructBase):
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


class _XTPTickByTickUnion(UnionBase):
    _fields_ = [
        ("entrust", _XTPTickByTickEntrust),
        ("trade", _XTPTickByTickTrade)
    ]


class XTPTickByTickStruct(StructBase):
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


class XTPTickerPriceInfo(StructBase):
    """
    供查询的最新信息
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('ticker', ctypes.c_char * 16),  # 合约代码（不包含交易所信息），不带空格，以'\0'结尾
        ('last_price', ctypes.c_double),  # 最新价
    ]
