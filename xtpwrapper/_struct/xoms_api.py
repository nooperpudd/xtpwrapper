# encoding=utf-8
import ctypes
from ._struct import Base


class XTPOrderInsertInfo(Base):
    """
    新订单请求
    """
    _fields_ = [
        ('order_xtp_id', ctypes.c_uint64),  # XTP系统订单ID，无需用户填写，在XTP系统中唯一
        ('order_client_id', ctypes.c_uint32),  # 报单引用，由客户自定义
        ('ticker', ctypes.c_char * 16),  # 合约代码客户端请求不带空格，以'\0'结尾
        ('market', ctypes.c_int),  # 交易市场
        ('price', ctypes.c_double),  # 价格
        ('stop_price', ctypes.c_double),  # 止损价（保留字段）
        ('quantity', ctypes.c_int64),  # 数量(股票单位为股，逆回购单位为张)
        ('price_type', ctypes.c_int),  # 报单价格
        ('business_type', ctypes.c_int),  # 业务类型
    ]

    # def __init__(self, order_xtp_id='', order_client_id='', ticker='', price=0.0, stop_price=0.0, quantity=''):
    #     super(XTPOrderInsertInfo, self).__init__()
    #     self.order_xtp_id = int(order_xtp_id)
    #     self.order_client_id = int(order_client_id)
    #     self.ticker = self._to_bytes(ticker)
    #     self.price = float(price)
    #     self.stop_price = float(stop_price)
    #     self.quantity = int(quantity)


class XTPOrderCancelInfo(Base):
    """
    撤单失败响应消息
    """
    _fields_ = [
        ('order_cancel_xtp_id', ctypes.c_uint64),  # 撤单XTPID
        ('order_xtp_id', ctypes.c_uint64),  # 原始订单XTPID
    ]

    # def __init__(self, order_cancel_xtp_id='', order_xtp_id=''):
    #     super(XTPOrderCancelInfo, self).__init__()
    #     self.order_cancel_xtp_id = int(order_cancel_xtp_id)
    #     self.order_xtp_id = int(order_xtp_id)


class XTPOrderInfo(Base):
    """
    报单响应结构体
    """
    _fields_ = [
        ('order_xtp_id', ctypes.c_uint64),  # XTP系统订单ID，在XTP系统中唯一
        ('order_client_id', ctypes.c_uint32),  # 报单引用，用户自定义
        ('order_cancel_client_id', ctypes.c_uint32),  # 报单操作引用，用户自定义（暂未使用）
        ('order_cancel_xtp_id', ctypes.c_uint64),  # 撤单在XTP系统中的id，在XTP系统中唯一
        ('ticker', ctypes.c_char * 16),  # 合约代码
        ('market', ctypes.c_int),  # 交易市场
        ('price', ctypes.c_double),  # 价格
        ('quantity', ctypes.c_int64),  # 数量，此订单的报单数量
        ('price_type', ctypes.c_int),  # 报单价格条件
        ('business_type', ctypes.c_int),  # 业务类型
        ('qty_traded', ctypes.c_int64),  # 今成交数量，为此订单累计成交数量
        ('qty_left', ctypes.c_int64),  # 剩余数量，当撤单成功时，表示撤单数量
        ('insert_time', ctypes.c_int64),  # 委托时间，格式为YYYYMMDDHHMMSSsss
        ('update_time', ctypes.c_int64),  # 最后修改时间，格式为YYYYMMDDHHMMSSsss
        ('cancel_time', ctypes.c_int64),  # 撤销时间，格式为YYYYMMDDHHMMSSsss
        ('trade_amount', ctypes.c_double),  # 成交金额，为此订单的成交总金额
        ('order_local_id', ctypes.c_char * 11),  # 本地报单编号 OMS生成的单号，不等同于order_xtp_id，为服务器传到报盘的单号
        ('order_status', ctypes.c_int),  # 报单状态，订单响应中没有部分成交状态的推送，在查询订单结果中，会有部分成交状态
        ('order_submit_status', ctypes.c_int),  # 报单提交状态，OMS内部使用，用户无需关心
        ('order_type', ctypes.c_char),  # 报单类型
    ]

    # def __init__(self, order_xtp_id='', order_client_id='', order_cancel_client_id='', order_cancel_xtp_id='',
    #              ticker='', price=0.0, quantity='', qty_traded='', qty_left='', insert_time='', update_time='',
    #              cancel_time='', trade_amount=0.0, order_local_id='', order_type=''):
    #     super(XTPOrderInfo, self).__init__()
    #     self.order_xtp_id = int(order_xtp_id)
    #     self.order_client_id = int(order_client_id)
    #     self.order_cancel_client_id = int(order_cancel_client_id)
    #     self.order_cancel_xtp_id = int(order_cancel_xtp_id)
    #     self.ticker = self._to_bytes(ticker)
    #     self.price = float(price)
    #     self.quantity = int(quantity)
    #     self.qty_traded = int(qty_traded)
    #     self.qty_left = int(qty_left)
    #     self.insert_time = int(insert_time)
    #     self.update_time = int(update_time)
    #     self.cancel_time = int(cancel_time)
    #     self.trade_amount = float(trade_amount)
    #     self.order_local_id = self._to_bytes(order_local_id)
    #     self.order_type = self._to_bytes(order_type)


class XTPTradeReport(Base):
    """
    报单成交结构体
    """
    _fields_ = [
        ('order_xtp_id', ctypes.c_uint64),  # XTP系统订单ID，此成交回报相关的订单ID，在XTP系统中唯一
        ('order_client_id', ctypes.c_uint32),  # 报单引用
        ('ticker', ctypes.c_char * 16),  # 合约代码
        ('market', ctypes.c_int),  # 交易市场
        ('local_order_id', ctypes.c_uint64),  # 订单号，引入XTPID后，该字段实际和order_xtp_id重复。接口中暂时保留。
        ('exec_id', ctypes.c_char * 18),  # 成交编号，深交所唯一，上交所每笔交易唯一，当发现2笔成交回报拥有相同的exec_id，则可以认为此笔交易自成交
        ('price', ctypes.c_double),  # 价格，此次成交的价格
        ('quantity', ctypes.c_int64),  # 数量，此次成交的数量，不是累计数量
        ('trade_time', ctypes.c_int64),  # 成交时间，格式为YYYYMMDDHHMMSSsss
        ('trade_amount', ctypes.c_double),  # 成交金额，此次成交的总金额 = price*quantity
        ('report_index', ctypes.c_uint64),  # 成交序号 --回报记录号，每个交易所唯一,report_index+market字段可以组成唯一标识表示成交回报
        ('order_exch_id', ctypes.c_char * 17),  # 报单编号 --交易所单号，上交所为空，深交所有此字段
        ('trade_type', ctypes.c_char),  # 成交类型  --成交回报中的执行类型
        ('business_type', ctypes.c_int),  # 业务类型
        ('branch_pbu', ctypes.c_char * 7),  # 交易所交易员代码
    ]

    # def __init__(self, order_xtp_id='', order_client_id='', ticker='', local_order_id='', exec_id='', price=0.0,
    #              quantity='', trade_time='', trade_amount=0.0, report_index='', order_exch_id='', trade_type='',
    #              branch_pbu=''):
    #     super(XTPTradeReport, self).__init__()
    #     self.order_xtp_id = int(order_xtp_id)
    #     self.order_client_id = int(order_client_id)
    #     self.ticker = self._to_bytes(ticker)
    #     self.local_order_id = int(local_order_id)
    #     self.exec_id = self._to_bytes(exec_id)
    #     self.price = float(price)
    #     self.quantity = int(quantity)
    #     self.trade_time = int(trade_time)
    #     self.trade_amount = float(trade_amount)
    #     self.report_index = int(report_index)
    #     self.order_exch_id = self._to_bytes(order_exch_id)
    #     self.trade_type = self._to_bytes(trade_type)
    #     self.branch_pbu = self._to_bytes(branch_pbu)


class XTPQueryOrderReq(Base):
    """
    报单查询请求
    """
    _fields_ = [
        ('ticker', ctypes.c_char * 16),  # 证券代码，可以为空，如果为空，则默认查询时间段内的所有成交回报
        ('begin_time', ctypes.c_int64),  # 格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点
        ('end_time', ctypes.c_int64),  # 格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    ]

    def __init__(self, ticker='', begin_time='', end_time=''):
        super(XTPQueryOrderReq, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.begin_time = int(begin_time)
        self.end_time = int(end_time)


class XTPQueryReportByExecIdReq(Base):
    """
    查询成交报告请求-根据执行编号查询（保留字段）
    """
    _fields_ = [
        ('order_xtp_id', ctypes.c_uint64),  # XTP订单系统ID
        ('exec_id', ctypes.c_char * 18),  # 成交执行编号
    ]

    def __init__(self, order_xtp_id='', exec_id=''):
        super(XTPQueryReportByExecIdReq, self).__init__()
        self.order_xtp_id = int(order_xtp_id)
        self.exec_id = self._to_bytes(exec_id)


class XTPQueryTraderReq(Base):
    """
    查询成交回报请求-查询条件
    """
    _fields_ = [
        ('ticker', ctypes.c_char * 16),  # 证券代码，可以为空，如果为空，则默认查询时间段内的所有成交回报
        ('begin_time', ctypes.c_int64),  # 开始时间，格式为YYYYMMDDHHMMSSsss，为0则默认当前交易日0点
        ('end_time', ctypes.c_int64),  # 结束时间，格式为YYYYMMDDHHMMSSsss，为0则默认当前时间
    ]

    def __init__(self, ticker='', begin_time='', end_time=''):
        super(XTPQueryTraderReq, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.begin_time = int(begin_time)
        self.end_time = int(end_time)


class XTPQueryAssetRsp(Base):
    """
    账户资金查询响应结构体
    """
    _fields_ = [
        ('total_asset', ctypes.c_double),  # 总资产(=可用资金 + 证券资产（目前为0）+ 预扣的资金)
        ('buying_power', ctypes.c_double),  # 可用资金
        ('security_asset', ctypes.c_double),  # 证券资产（保留字段，目前为0）
        ('fund_buy_amount', ctypes.c_double),  # 累计买入成交证券占用资金
        ('fund_buy_fee', ctypes.c_double),  # 累计买入成交交易费用
        ('fund_sell_amount', ctypes.c_double),  # 累计卖出成交证券所得资金
        ('fund_sell_fee', ctypes.c_double),  # 累计卖出成交交易费用
        ('withholding_amount', ctypes.c_double),  # XTP系统预扣的资金（包括购买卖股票时预扣的交易资金+预扣手续费）
        ('account_type', ctypes.c_int),  # 账户类型
        ('frozen_margin', ctypes.c_double),  # 冻结的保证金
        ('frozen_exec_cash', ctypes.c_double),  # 行权冻结资金
        ('frozen_exec_fee', ctypes.c_double),  # 行权费用
        ('pay_later', ctypes.c_double),  # 垫付资金
        ('preadva_pay', ctypes.c_double),  # 预垫付资金
        ('orig_banlance', ctypes.c_double),  # 昨日余额
        ('banlance', ctypes.c_double),  # 当前余额
        ('deposit_withdraw', ctypes.c_double),  # 当天出入金
        ('trade_netting', ctypes.c_double),  # 当日交易资金轧差
        ('captial_asset', ctypes.c_double),  # 资金资产
        ('force_freeze_amount', ctypes.c_double),  # 强锁资金
        ('preferred_amount', ctypes.c_double),  # 可取资金
    ]

    def __init__(self, total_asset=0.0, buying_power=0.0, security_asset=0.0, fund_buy_amount=0.0, fund_buy_fee=0.0,
                 fund_sell_amount=0.0, fund_sell_fee=0.0, withholding_amount=0.0, frozen_margin=0.0,
                 frozen_exec_cash=0.0, frozen_exec_fee=0.0, pay_later=0.0, preadva_pay=0.0, orig_banlance=0.0,
                 banlance=0.0, deposit_withdraw=0.0, trade_netting=0.0, captial_asset=0.0, force_freeze_amount=0.0,
                 preferred_amount=0.0):
        super(XTPQueryAssetRsp, self).__init__()
        self.total_asset = float(total_asset)
        self.buying_power = float(buying_power)
        self.security_asset = float(security_asset)
        self.fund_buy_amount = float(fund_buy_amount)
        self.fund_buy_fee = float(fund_buy_fee)
        self.fund_sell_amount = float(fund_sell_amount)
        self.fund_sell_fee = float(fund_sell_fee)
        self.withholding_amount = float(withholding_amount)
        self.frozen_margin = float(frozen_margin)
        self.frozen_exec_cash = float(frozen_exec_cash)
        self.frozen_exec_fee = float(frozen_exec_fee)
        self.pay_later = float(pay_later)
        self.preadva_pay = float(preadva_pay)
        self.orig_banlance = float(orig_banlance)
        self.banlance = float(banlance)
        self.deposit_withdraw = float(deposit_withdraw)
        self.trade_netting = float(trade_netting)
        self.captial_asset = float(captial_asset)
        self.force_freeze_amount = float(force_freeze_amount)
        self.preferred_amount = float(preferred_amount)


class XTPQueryStkPositionRsp(Base):
    """
    查询股票持仓情况
    """
    _fields_ = [
        ('ticker', ctypes.c_char * 16),  # 证券代码
        ('ticker_name', ctypes.c_char * 64),  # 证券名称
        ('market', ctypes.c_int),  # 交易市场
        ('total_qty', ctypes.c_int64),  # 总持仓
        ('sellable_qty', ctypes.c_int64),  # 可卖持仓
        ('avg_price', ctypes.c_double),  # 持仓成本
        ('unrealized_pnl', ctypes.c_double),  # 浮动盈亏（保留字段）
        ('yesterday_position', ctypes.c_int64),  # 昨日持仓
        ('purchase_redeemable_qty', ctypes.c_int64),  # 今日申购赎回数量（申购和赎回数量不可能同时存在，因此可以共用一个字段）
        ('position_direction', ctypes.c_int),  # 持仓方向
        ('reserved1', ctypes.c_uint32),  # 保留字段1
        ('executable_option', ctypes.c_int64),  # 可行权合约
        ('lockable_position', ctypes.c_int64),  # 可锁定标的
        ('executable_underlying', ctypes.c_int64),  # 可行权标的
        ('locked_position', ctypes.c_int64),  # 已锁定标的
        ('usable_locked_position', ctypes.c_int64),  # 可用已锁定标的
    ]

    def __init__(self, ticker='', ticker_name='', total_qty='', sellable_qty='', avg_price=0.0, unrealized_pnl=0.0,
                 yesterday_position='', purchase_redeemable_qty='', reserved1='', executable_option='',
                 lockable_position='', executable_underlying='', locked_position='', usable_locked_position=''):
        super(XTPQueryStkPositionRsp, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.ticker_name = self._to_bytes(ticker_name)
        self.total_qty = int(total_qty)
        self.sellable_qty = int(sellable_qty)
        self.avg_price = float(avg_price)
        self.unrealized_pnl = float(unrealized_pnl)
        self.yesterday_position = int(yesterday_position)
        self.purchase_redeemable_qty = int(purchase_redeemable_qty)
        self.reserved1 = int(reserved1)
        self.executable_option = int(executable_option)
        self.lockable_position = int(lockable_position)
        self.executable_underlying = int(executable_underlying)
        self.locked_position = int(locked_position)
        self.usable_locked_position = int(usable_locked_position)


class XTPFundTransferNotice(Base):
    """
    资金内转流水通知
    """
    _fields_ = [
        ('serial_id', ctypes.c_uint64),  # 资金内转编号
        ('transfer_type', ctypes.c_int),  # 内转类型
        ('amount', ctypes.c_double),  # 金额
        ('oper_status', ctypes.c_int),  # 操作结果
        ('transfer_time', ctypes.c_uint64),  # 操作时间
    ]

    def __init__(self, serial_id='', amount=0.0, transfer_time=''):
        super(XTPFundTransferNotice, self).__init__()
        self.serial_id = int(serial_id)
        self.amount = float(amount)
        self.transfer_time = int(transfer_time)


class XTPQueryFundTransferLogReq(Base):
    """
    资金内转流水查询请求与响应
    """
    _fields_ = [
        ('serial_id', ctypes.c_uint64),  # 资金内转编号
    ]

    def __init__(self, serial_id=''):
        super(XTPQueryFundTransferLogReq, self).__init__()
        self.serial_id = int(serial_id)


class XTPQueryStructuredFundInfoReq(Base):
    """
    查询分级基金信息结构体
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码，不可为空
        ('sf_ticker', ctypes.c_char * 16),  # 分级基金母基金代码，可以为空，如果为空，则默认查询所有的分级基金
    ]

    def __init__(self, sf_ticker=''):
        super(XTPQueryStructuredFundInfoReq, self).__init__()
        self.sf_ticker = self._to_bytes(sf_ticker)


class XTPStructuredFundInfo(Base):
    """
    查询分级基金信息响应结构体
    """
    _fields_ = [
        ('exchange_id', ctypes.c_int),  # 交易所代码
        ('sf_ticker', ctypes.c_char * 16),  # 分级基金母基金代码
        ('sf_ticker_name', ctypes.c_char * 64),  # 分级基金母基金名称
        ('ticker', ctypes.c_char * 16),  # 分级基金子基金代码
        ('ticker_name', ctypes.c_char * 64),  # 分级基金子基金名称
        ('split_merge_status', ctypes.c_int),  # 基金允许拆分合并状态
        ('ratio', ctypes.c_uint32),  # 拆分合并比例
        ('min_split_qty', ctypes.c_uint32),  # 最小拆分数量
        ('min_merge_qty', ctypes.c_uint32),  # 最小合并数量
        ('net_price', ctypes.c_double),  # 基金净值
    ]

    def __init__(self, sf_ticker='', sf_ticker_name='', ticker='', ticker_name='', ratio='', min_split_qty='',
                 min_merge_qty='', net_price=0.0):
        super(XTPStructuredFundInfo, self).__init__()
        self.sf_ticker = self._to_bytes(sf_ticker)
        self.sf_ticker_name = self._to_bytes(sf_ticker_name)
        self.ticker = self._to_bytes(ticker)
        self.ticker_name = self._to_bytes(ticker_name)
        self.ratio = int(ratio)
        self.min_split_qty = int(min_split_qty)
        self.min_merge_qty = int(min_merge_qty)
        self.net_price = float(net_price)


class XTPQueryETFBaseReq(Base):
    """
    查询股票ETF合约基本情况--请求结构体,
    请求参数为多条件参数:1,不填则返回所有市场的ETF合约信息。
                     2,只填写market,返回该交易市场下结果
                     3,填写market及ticker参数,只返回该etf信息。
    """
    _fields_ = [
        ('market', ctypes.c_int),  # 交易市场
        ('ticker', ctypes.c_char * 16),  # ETF买卖代码
    ]

    def __init__(self, ticker=''):
        super(XTPQueryETFBaseReq, self).__init__()
        self.ticker = self._to_bytes(ticker)


class XTPQueryETFBaseRsp(Base):
    """
    查询股票ETF合约基本情况--响应结构体
    """
    _fields_ = [
        ('market', ctypes.c_int),  # 交易市场
        ('etf', ctypes.c_char * 16),  # etf代码,买卖,申赎统一使用该代码
        ('subscribe_redemption_ticker', ctypes.c_char * 16),  # etf代码,买卖,申赎统一使用该代码
        ('unit', ctypes.c_int32),  # 最小申购赎回单位对应的ETF份数,例如上证"50ETF"就是900000
        ('subscribe_status', ctypes.c_int32),  # 是否允许申购,1-允许,0-禁止
        ('redemption_status', ctypes.c_int32),  # 是否允许赎回,1-允许,0-禁止
        ('max_cash_ratio', ctypes.c_double),  # 最大现金替代比例,小于1的数值
        ('estimate_amount', ctypes.c_double),  # T日预估金额
        ('cash_component', ctypes.c_double),  # T-X日现金差额
        ('net_value', ctypes.c_double),  # 基金单位净值
        ('total_amount', ctypes.c_double),  # 最小申赎单位净值总金额
    ]

    def __init__(self, etf='', subscribe_redemption_ticker='', unit='', subscribe_status='', redemption_status='',
                 max_cash_ratio=0.0, estimate_amount=0.0, cash_component=0.0, net_value=0.0, total_amount=0.0):
        super(XTPQueryETFBaseRsp, self).__init__()
        self.etf = self._to_bytes(etf)
        self.subscribe_redemption_ticker = self._to_bytes(subscribe_redemption_ticker)
        self.unit = int(unit)
        self.subscribe_status = int(subscribe_status)
        self.redemption_status = int(redemption_status)
        self.max_cash_ratio = float(max_cash_ratio)
        self.estimate_amount = float(estimate_amount)
        self.cash_component = float(cash_component)
        self.net_value = float(net_value)
        self.total_amount = float(total_amount)


class XTPQueryETFComponentReq(Base):
    """
    查询股票ETF合约成分股信息--请求结构体,请求参数为:交易市场+ETF买卖代码
    """
    _fields_ = [
        ('market', ctypes.c_int),  # 交易市场
        ('ticker', ctypes.c_char * 16),  # ETF买卖代码
    ]

    def __init__(self, ticker=''):
        super(XTPQueryETFComponentReq, self).__init__()
        self.ticker = self._to_bytes(ticker)


class XTPQueryETFComponentRsp(Base):
    """
    查询股票ETF合约成分股信息--响应结构体
    """
    _fields_ = [
        ('market', ctypes.c_int),  # 交易市场
        ('ticker', ctypes.c_char * 16),  # ETF代码
        ('component_ticker', ctypes.c_char * 16),  # 成份股代码
        ('component_name', ctypes.c_char * 64),  # 成份股名称
        ('quantity', ctypes.c_int64),  # 成份股数量
        ('component_market', ctypes.c_int),  # 成份股交易市场
        ('replace_type', ctypes.c_int),  # 成份股替代标识
        ('premium_ratio', ctypes.c_double),  # 溢价比例
        ('amount', ctypes.c_double),  # 成分股替代标识为必须现金替代时候的总金额
    ]

    def __init__(self, ticker='', component_ticker='', component_name='', quantity='', premium_ratio=0.0, amount=0.0):
        super(XTPQueryETFComponentRsp, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.component_ticker = self._to_bytes(component_ticker)
        self.component_name = self._to_bytes(component_name)
        self.quantity = int(quantity)
        self.premium_ratio = float(premium_ratio)
        self.amount = float(amount)


class XTPQueryIPOTickerRsp(Base):
    """
    查询当日可申购新股信息
    """
    _fields_ = [
        ('market', ctypes.c_int),  # 交易市场
        ('ticker', ctypes.c_char * 16),  # 申购代码
        ('ticker_name', ctypes.c_char * 64),  # 申购股票名称
        ('price', ctypes.c_double),  # 申购价格
        ('unit', ctypes.c_int32),  # 申购单元
        ('qty_upper_limit', ctypes.c_int32),  # 最大允许申购数量
    ]

    def __init__(self, ticker='', ticker_name='', price=0.0, unit='', qty_upper_limit=''):
        super(XTPQueryIPOTickerRsp, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.ticker_name = self._to_bytes(ticker_name)
        self.price = float(price)
        self.unit = int(unit)
        self.qty_upper_limit = int(qty_upper_limit)


class XTPQueryIPOQuotaRsp(Base):
    """
    查询用户申购额度
    """
    _fields_ = [
        ('market', ctypes.c_int),  # 交易市场
        ('quantity', ctypes.c_int32),  # 可申购额度
    ]

    def __init__(self, quantity=''):
        super(XTPQueryIPOQuotaRsp, self).__init__()
        self.quantity = int(quantity)


class XTPQueryOptionAuctionInfoReq(Base):
    """
    查询期权竞价交易业务参考信息--请求结构体,请求参数为:交易市场+8位期权代码
    """
    _fields_ = [
        ('market', ctypes.c_int),  # 交易市场
        ('ticker', ctypes.c_char * 16),  # 8位期权合约代码
    ]

    def __init__(self, ticker=''):
        super(XTPQueryOptionAuctionInfoReq, self).__init__()
        self.ticker = self._to_bytes(ticker)


class XTPQueryOptionAuctionInfoRsp(Base):
    """
    查询期权竞价交易业务参考信息
    """
    _fields_ = [
        ('ticker', ctypes.c_char * 16),  # 合约编码，报单ticker采用本字段
        ('security_id_source', ctypes.c_int),  # 证券代码源
        ('symbol', ctypes.c_char * 64),  # 合约简称
        ('contract_id', ctypes.c_char * 64),  # 合约交易代码
        ('underlying_security_id', ctypes.c_char * 16),  # 基础证券代码
        ('underlying_security_id_source', ctypes.c_int),  # 基础证券代码源
        ('list_date', ctypes.c_uint32),  # 上市日期，格式为YYYYMMDD
        ('last_trade_date', ctypes.c_uint32),  # 最后交易日，格式为YYYYMMDD
        ('ticker_type', ctypes.c_int),  # 证券类别
        ('day_trading', ctypes.c_int32),  # 是否支持当日回转交易，1-允许，0-不允许
        ('call_or_put', ctypes.c_int),  # 认购或认沽
        ('delivery_day', ctypes.c_uint32),  # 行权交割日，格式为YYYYMMDD
        ('delivery_month', ctypes.c_uint32),  # 交割月份，格式为YYYYMM
        ('exercise_type', ctypes.c_int),  # 行权方式
        ('exercise_begin_date', ctypes.c_uint32),  # 行权起始日期，格式为YYYYMMDD
        ('exercise_end_date', ctypes.c_uint32),  # 行权结束日期，格式为YYYYMMDD
        ('exercise_price', ctypes.c_double),  # 行权价格
        ('qty_unit', ctypes.c_int64),  # 数量单位，对于某一证券申报的委托，其委托数量字段必须为该证券数量单位的整数倍
        ('contract_unit', ctypes.c_int64),  # 合约单位
        ('contract_position', ctypes.c_int64),  # 合约持仓量
        ('prev_close_price', ctypes.c_double),  # 合约前收盘价
        ('prev_clearing_price', ctypes.c_double),  # 合约前结算价
        ('lmt_buy_max_qty', ctypes.c_int64),  # 限价买最大量
        ('lmt_buy_min_qty', ctypes.c_int64),  # 限价买最小量
        ('lmt_sell_max_qty', ctypes.c_int64),  # 限价卖最大量
        ('lmt_sell_min_qty', ctypes.c_int64),  # 限价卖最小量
        ('mkt_buy_max_qty', ctypes.c_int64),  # 市价买最大量
        ('mkt_buy_min_qty', ctypes.c_int64),  # 市价买最小量
        ('mkt_sell_max_qty', ctypes.c_int64),  # 市价卖最大量
        ('mkt_sell_min_qty', ctypes.c_int64),  # 市价卖最小量
        ('price_tick', ctypes.c_double),  # 最小报价单位
        ('upper_limit_price', ctypes.c_double),  # 涨停价
        ('lower_limit_price', ctypes.c_double),  # 跌停价
        ('sell_margin', ctypes.c_double),  # 今卖开每张保证金
        ('margin_ratio_param1', ctypes.c_double),  # 交易所保证金比例计算参数一
        ('margin_ratio_param2', ctypes.c_double),  # 交易所保证金比例计算参数二
    ]

    def __init__(self, ticker='', symbol='', contract_id='', underlying_security_id='', list_date='',
                 last_trade_date='', day_trading='', delivery_day='', delivery_month='', exercise_begin_date='',
                 exercise_end_date='', exercise_price=0.0, qty_unit='', contract_unit='', contract_position='',
                 prev_close_price=0.0, prev_clearing_price=0.0, lmt_buy_max_qty='', lmt_buy_min_qty='',
                 lmt_sell_max_qty='', lmt_sell_min_qty='', mkt_buy_max_qty='', mkt_buy_min_qty='', mkt_sell_max_qty='',
                 mkt_sell_min_qty='', price_tick=0.0, upper_limit_price=0.0, lower_limit_price=0.0, sell_margin=0.0,
                 margin_ratio_param1=0.0, margin_ratio_param2=0.0):
        super(XTPQueryOptionAuctionInfoRsp, self).__init__()
        self.ticker = self._to_bytes(ticker)
        self.symbol = self._to_bytes(symbol)
        self.contract_id = self._to_bytes(contract_id)
        self.underlying_security_id = self._to_bytes(underlying_security_id)
        self.list_date = int(list_date)
        self.last_trade_date = int(last_trade_date)
        self.day_trading = int(day_trading)
        self.delivery_day = int(delivery_day)
        self.delivery_month = int(delivery_month)
        self.exercise_begin_date = int(exercise_begin_date)
        self.exercise_end_date = int(exercise_end_date)
        self.exercise_price = float(exercise_price)
        self.qty_unit = int(qty_unit)
        self.contract_unit = int(contract_unit)
        self.contract_position = int(contract_position)
        self.prev_close_price = float(prev_close_price)
        self.prev_clearing_price = float(prev_clearing_price)
        self.lmt_buy_max_qty = int(lmt_buy_max_qty)
        self.lmt_buy_min_qty = int(lmt_buy_min_qty)
        self.lmt_sell_max_qty = int(lmt_sell_max_qty)
        self.lmt_sell_min_qty = int(lmt_sell_min_qty)
        self.mkt_buy_max_qty = int(mkt_buy_max_qty)
        self.mkt_buy_min_qty = int(mkt_buy_min_qty)
        self.mkt_sell_max_qty = int(mkt_sell_max_qty)
        self.mkt_sell_min_qty = int(mkt_sell_min_qty)
        self.price_tick = float(price_tick)
        self.upper_limit_price = float(upper_limit_price)
        self.lower_limit_price = float(lower_limit_price)
        self.sell_margin = float(sell_margin)
        self.margin_ratio_param1 = float(margin_ratio_param1)
        self.margin_ratio_param2 = float(margin_ratio_param2)
