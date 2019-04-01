# encoding:utf-8
from enum import IntEnum, auto


class XTP_LOG_LEVEL(IntEnum):
    """
    XTP_LOG_LEVEL是日志输出级别类型
    """
    XTP_LOG_LEVEL_FATAL = 0  # 严重错误级别
    XTP_LOG_LEVEL_ERROR = auto()  # 错误级别
    XTP_LOG_LEVEL_WARNING = auto()  # 警告级别
    XTP_LOG_LEVEL_INFO = auto()  # info级别
    XTP_LOG_LEVEL_DEBUG = auto()  # debug级别
    XTP_LOG_LEVEL_TRACE = auto()  # trace级别


class XTP_PROTOCOL_TYPE(IntEnum):
    """
    XTP_PROTOCOL_TYPE是通讯传输协议方式
    """
    XTP_PROTOCOL_TCP = 1  # 采用TCP方式传输
    XTP_PROTOCOL_UDP = auto()  # 采用UDP方式传输(仅行情接口支持)


class XTP_EXCHANGE_TYPE(IntEnum):
    """
    XTP_EXCHANGE_TYPE是交易所类型
    """
    XTP_EXCHANGE_SH = 1  # 上证
    XTP_EXCHANGE_SZ = auto()  # 深证
    XTP_EXCHANGE_UNKNOWN = auto()  # 不存在的交易所类型


class XTP_MARKET_TYPE(IntEnum):
    """
    XTP_MARKET_TYPE市场类型
    """
    XTP_MKT_INIT = 0  # 初始化值或者未知
    XTP_MKT_SZ_A = 1  # 深圳A股
    XTP_MKT_SH_A = auto()  # 上海A股
    XTP_MKT_UNKNOWN = auto()  # 未知交易市场类型


class XTP_PRICE_TYPE(IntEnum):
    # XTP_PRICE_TYPE是价格类型
    XTP_PRICE_LIMIT = 1  # 限价单-沪 / 深 / 沪期权（除普通股票业务外，其余业务均使用此种类型）
    XTP_PRICE_BEST_OR_CANCEL = auto()  # 即时成交剩余转撤销，市价单-深 / 沪期权
    XTP_PRICE_BEST5_OR_LIMIT = auto()  # 最优五档即时成交剩余转限价，市价单-沪
    XTP_PRICE_BEST5_OR_CANCEL = auto()  # 最优5档即时成交剩余转撤销，市价单-沪深
    XTP_PRICE_ALL_OR_CANCEL = auto()  # 全部成交或撤销= auto()市价单-深 / 沪期权
    XTP_PRICE_FORWARD_BEST = auto()  # 本方最优，市价单-深
    XTP_PRICE_REVERSE_BEST_LIMIT = auto()  # 对方最优剩余转限价，市价单-深 / 沪期权
    XTP_PRICE_LIMIT_OR_CANCEL = auto()  # 期权限价申报FOK
    XTP_PRICE_TYPE_UNKNOWN = auto()  # 未知或者无效价格类型


class XTP_SIDE_TYPE(IntEnum):
    # 是买卖方向类型
    XTP_SIDE_BUY = 1  # 买（新股申购，ETF买，配股，信用交易中担保品买）

    XTP_SIDE_SELL = 2  # 卖（逆回购，ETF卖，信用交易中担保品卖）

    XTP_SIDE_PURCHASE = 7  # 申购

    XTP_SIDE_REDEMPTION = 8  # 赎回

    XTP_SIDE_SPLIT = 9  # 拆分

    XTP_SIDE_MERGE = 10  # 合并

    XTP_SIDE_COVER = 11  # 改版之后的side的备兑，暂不支持

    XTP_SIDE_FREEZE = 12  # 改版之后的side锁定（对应开平标识为开）/解锁（对应开平标识为平）

    XTP_SIDE_MARGIN_TRADE = 21  # 融资买入

    XTP_SIDE_SHORT_SELL = 22  # 融券卖出

    XTP_SIDE_REPAY_MARGIN = 23  # 卖券还款

    XTP_SIDE_REPAY_STOCK = 24  # 买券还券

    XTP_SIDE_CASH_REPAY_MARGIN = 25  # 现金还款

    XTP_SIDE_STOCK_REPAY_STOCK = 26  # 现券还券

    XTP_SIDE_UNKNOWN = 27  # 未知或者无效买卖方向


class XTP_POSITION_EFFECT_TYPE(IntEnum):
    # 是开平标识类型
    XTP_POSITION_EFFECT_INIT = 0  # 初始值或未知值开平标识，现货适用

    XTP_POSITION_EFFECT_OPEN = 1  # 开

    XTP_POSITION_EFFECT_CLOSE = 2  # 平

    XTP_POSITION_EFFECT_FORCECLOSE = 3  # 强平

    XTP_POSITION_EFFECT_CLOSETODAY = 4  # 平今

    XTP_POSITION_EFFECT_CLOSEYESTERDAY = 5  # 平昨

    XTP_POSITION_EFFECT_FORCEOFF = 6  # 强减

    XTP_POSITION_EFFECT_LOCALFORCECLOSE = 7  # 本地强平

    XTP_POSITION_EFFECT_UNKNOWN = 8  # 未知的开平标识类型


class XTP_ORDER_ACTION_STATUS_TYPE(IntEnum):
    """
    XTP_ORDER_ACTION_STATUS_TYPE是报单操作状态类型
    """
    XTP_ORDER_ACTION_STATUS_SUBMITTED = 1  # 已经提交
    XTP_ORDER_ACTION_STATUS_ACCEPTED = auto()  # 已经接受
    XTP_ORDER_ACTION_STATUS_REJECTED = auto()  # 已经被拒绝


class XTP_ORDER_STATUS_TYPE(IntEnum):
    """
    XTP_ORDER_STATUS_TYPE是报单状态类型
    """
    XTP_ORDER_STATUS_INIT = 0  # 初始化
    XTP_ORDER_STATUS_ALLTRADED = 1  # 全部成交
    XTP_ORDER_STATUS_PARTTRADEDQUEUEING = auto()  # 部分成交
    XTP_ORDER_STATUS_PARTTRADEDNOTQUEUEING = auto()  # 部分撤单
    XTP_ORDER_STATUS_NOTRADEQUEUEING = auto()  # 未成交
    XTP_ORDER_STATUS_CANCELED = auto()  # 已撤单
    XTP_ORDER_STATUS_REJECTED = auto()  # 已拒绝
    XTP_ORDER_STATUS_UNKNOWN = auto()  # 未知订单状态


class XTP_ORDER_SUBMIT_STATUS_TYPE(IntEnum):
    """
    XTP_ORDER_SUBMIT_STATUS_TYPE是报单提交状态类型
    """
    XTP_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED = 1  # 订单已经提交
    XTP_ORDER_SUBMIT_STATUS_INSERT_ACCEPTED = auto()  # 订单已经被接受
    XTP_ORDER_SUBMIT_STATUS_INSERT_REJECTED = auto()  # 订单已经被拒绝
    XTP_ORDER_SUBMIT_STATUS_CANCEL_SUBMITTED = auto()  # 撤单已经提交
    XTP_ORDER_SUBMIT_STATUS_CANCEL_REJECTED = auto()  # 撤单已经被拒绝
    XTP_ORDER_SUBMIT_STATUS_CANCEL_ACCEPTED = auto()  # 撤单已经被接受


class XTP_TE_RESUME_TYPE(IntEnum):
    """
    XTP_TE_RESUME_TYPE是公有流（订单响应、成交回报）重传方式
    """

    XTP_TERT_RESTART = 0  # 从本交易日开始重传
    XTP_TERT_RESUME = auto()  # 从从上次收到的续传（暂未支持）
    XTP_TERT_QUICK = auto()  # 只传送登录后公有流（订单响应、成交回报）的内容


class ETF_REPLACE_TYPE(IntEnum):
    """
    ETF_REPLACE_TYPE现金替代标识定义
    """
    ERT_CASH_FORBIDDEN = 0  # 禁止现金替代
    ERT_CASH_OPTIONAL = auto()  # 可以现金替代
    ERT_CASH_MUST = auto()  # 必须现金替代
    ERT_CASH_RECOMPUTE_INTER_SZ = auto()  # 深市退补现金替代
    ERT_CASH_MUST_INTER_SZ = auto()  # 深市必须现金替代
    ERT_CASH_RECOMPUTE_INTER_OTHER = auto()  # 非沪深市场成分证券退补现金替代
    ERT_CASH_MUST_INTER_OTHER = auto()  # 表示非沪深市场成份证券必须现金替代
    EPT_INVALID = auto()  # 无效值


class XTP_TICKER_TYPE(IntEnum):
    """
    XTP_TICKER_TYPE证券类型
    """
    XTP_TICKER_TYPE_STOCK = 0  # 普通股票
    XTP_TICKER_TYPE_INDEX = auto()  # 指数
    XTP_TICKER_TYPE_FUND = auto()  # 基金
    XTP_TICKER_TYPE_BOND = auto()  # 债券
    XTP_TICKER_TYPE_OPTION = auto()  # 期权
    XTP_TICKER_TYPE_UNKNOWN = auto()  # 未知类型


class XTP_BUSINESS_TYPE(IntEnum):
    """
    XTP_BUSINESS_TYPE证券业务类型
    """
    XTP_BUSINESS_TYPE_CASH = 0  # 普通股票业务（股票买卖，ETF买卖等）
    XTP_BUSINESS_TYPE_IPOS = auto()  # 新股申购业务（对应的price type需选择限价类型）
    XTP_BUSINESS_TYPE_REPO = auto()  # 回购业务(对应的price type填为限价，side填为卖)
    XTP_BUSINESS_TYPE_ETF = auto()  # ETF申赎业务
    XTP_BUSINESS_TYPE_MARGIN = auto()  # 融资融券业务（暂未支持）
    XTP_BUSINESS_TYPE_DESIGNATION = auto()  # 转托管（未支持）
    XTP_BUSINESS_TYPE_ALLOTMENT = auto()  # 配股业务（对应的price type需选择限价类型= auto()side填为买）
    XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = auto()  # 分级基金申赎业务
    XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = auto()  # 分级基金拆分合并业务
    XTP_BUSINESS_TYPE_MONEY_FUND = auto()  # 货币基金业务（暂未支持）
    XTP_BUSINESS_TYPE_OPTION = auto()  # 期权业务
    XTP_BUSINESS_TYPE_EXECUTE = auto()  # 行权
    XTP_BUSINESS_TYPE_FREEZE = auto()  # 锁定解锁，暂不支持
    XTP_BUSINESS_TYPE_UNKNOWN = auto()  # 未知类型


class XTP_ACCOUNT_TYPE(IntEnum):
    """
    XTP_ACCOUNT_TYPE账户类型
    """
    XTP_ACCOUNT_NORMAL = 0  # 普通账户
    XTP_ACCOUNT_CREDIT = auto()  # 信用账户
    XTP_ACCOUNT_DERIVE = auto()  # 衍生品账户
    XTP_ACCOUNT_UNKNOWN = auto()  # 未知账户类型


class XTP_FUND_TRANSFER_TYPE(IntEnum):
    """
    XTP_FUND_TRANSFER_TYPE是资金流转方向类型
    """
    XTP_FUND_TRANSFER_OUT = 0  # 转出从XTP转出到柜台
    XTP_FUND_TRANSFER_IN = auto()  # 转入从柜台转入XTP
    XTP_FUND_TRANSFER_UNKNOWN = auto()  # 未知类型


class XTP_FUND_OPER_STATUS(IntEnum):
    """
    XTP_FUND_OPER_STATUS柜台资金操作结果
    """
    XTP_FUND_OPER_PROCESSING = 0  # XOMS已收到，正在处理中
    XTP_FUND_OPER_SUCCESS = auto()  # 成功
    XTP_FUND_OPER_FAILED = auto()  # 失败
    XTP_FUND_OPER_SUBMITTED = auto()  # 已提交到集中柜台处理
    XTP_FUND_OPER_UNKNOWN = auto()  # 未知


class XTP_SPLIT_MERGE_STATUS(IntEnum):
    """
    XTP_SPLIT_MERGE_STATUS是一个基金当天拆分合并状态类型
    """

    XTP_SPLIT_MERGE_STATUS_ALLOW = 0  # 允许拆分和合并
    XTP_SPLIT_MERGE_STATUS_ONLY_SPLIT = auto()  # 只允许拆分，不允许合并
    XTP_SPLIT_MERGE_STATUS_ONLY_MERGE = auto()  # 只允许合并，不允许拆分
    XTP_SPLIT_MERGE_STATUS_FORBIDDEN = auto()  # 不允许拆分合并


class XTP_TBT_TYPE(IntEnum):
    """
    XTP_TBT_TYPE是一个逐笔回报类型
    """
    XTP_TBT_ENTRUST = 1  # 逐笔委托
    XTP_TBT_TRADE = 2  # 逐笔成交


class XTP_OPT_CALL_OR_PUT_TYPE(IntEnum):
    """
    XTP_OPT_CALL_OR_PUT_TYPE是一个认沽或认购类型
    """
    XTP_OPT_CALL = 1  # 认购
    XTP_OPT_PUT = 2  # 认沽


class XTP_OPT_EXERCISE_TYPE_TYPE(IntEnum):
    """
    XTP_OPT_EXERCISE_TYPE_TYPE是一个行权方式类型
    """
    XTP_OPT_EXERCISE_TYPE_EUR = 1  # 欧式
    XTP_OPT_EXERCISE_TYPE_AME = 2  # 美式


class XTP_POSITION_DIRECTION_TYPE(IntEnum):
    """
    XTP_POSITION_DIRECTION_TYPE是一个持仓方向类型
    """

    XTP_POSITION_DIRECTION_NET = 0  # 净
    XTP_POSITION_DIRECTION_LONG = auto()  # 多（期权则为权利方）
    XTP_POSITION_DIRECTION_SHORT = auto()  # 空（期权则为义务方）
    XTP_POSITION_DIRECTION_COVERED = auto()  # 备兑（期权则为备兑义务方）


class XTP_MARKETDATA_TYPE(IntEnum):
    """

    """
    XTP_MARKETDATA_ACTUAL = 0  # 现货(股票 / 基金 / 债券等)
    XTP_MARKETDATA_OPTION = 1  # 期权

########################/
# TXTPTradeTypeType是成交类型类型
########################/
# typedef
# char
# TXTPTradeTypeType;

# 普通成交
# define XTP_TRDT_COMMON '0'
# 现金替代
# define XTP_TRDT_CASH '1'
# 一级市场成交
# define XTP_TRDT_PRIMARY '2'
