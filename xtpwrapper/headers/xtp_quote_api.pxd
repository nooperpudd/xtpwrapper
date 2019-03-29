# encoding:utf-8
# distutils: language=c++

from cpython cimport PyObject
from libc.stdint cimport uint32_t, uint8_t
from libc.string cimport const_char

from .xtp_api_data_type cimport (
    XTP_EXCHANGE_TYPE,
    XTP_PROTOCOL_TYPE,
    XTP_LOG_LEVEL
)
from .xtp_api_struct_common cimport XTPRI


cdef extern from "xtp_quote_api.h" namespace "XTP::API":
    cdef cppclass QuoteApi:
        #删除接口对象本身
        #@remark 不再使用本接口对象时,调用该函数删除接口对象
        void Release() nogil

        #获取当前交易日
        #@return 获取到的交易日
        #@remark 只有登录成功后,才能得到正确的交易日
        const_char *GetTradingDay() nogil

        #获取API的发行版本号
        #@return 返回api发行版本号
        const_char *GetApiVersion()  nogil

        #获取API的系统错误
        #@return 返回的错误信息，可以在Login、Logout、订阅、取消订阅失败时调用，获取失败的原因
        #@remark 可以在调用api接口失败时调用，例如login失败时
        XTPRI *GetApiLastError() nogil except +

        #设置采用UDP方式连接时的接收缓冲区大小
        #@remark 需要在Login之前调用，默认大小和最小设置均为64MB。此缓存大小单位为MB，请输入2的次方数，例如128MB请输入128。
        void SetUDPBufferSize(uint32_t buff_size) nogil except +

        #注册回调接口
        #@param spi 派生自回调接口类的实例，请在登录之前设定
        void RegisterSpi(WrapperQuoteSpi *spi) nogil except +

        #设置心跳检测时间间隔，单位为秒
        #@param interval 心跳检测时间间隔，单位为秒
        #@remark 此函数必须在Login之前调用
        void SetHeartBeatInterval(uint32_t interval) nogil except +

        #订阅行情，包括股票、指数和期权。
        #@return 订阅接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        #@param count 要订阅/退订行情的合约个数
        #@param exchange_id 交易所代码
        #@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情
        int SubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订行情，包括股票、指数和期权。
        #@return 取消订阅接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        #@param count 要订阅/退订行情的合约个数
        #@param exchange_id 交易所代码
        #@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅行情接口配套使用
        int UnSubscribeMarketData(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #订阅行情订单簿，包括股票、指数和期权。
        #@return 订阅行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        #@param count 要订阅/退订行情订单簿的合约个数
        #@param exchange_id 交易所代码
        #@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情(仅支持深交所)
        int SubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订行情订单簿，包括股票、指数和期权。
        #@return 取消订阅行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        #@param count 要订阅/退订行情订单簿的合约个数
        #@param exchange_id 交易所代码
        #@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅行情订单簿接口配套使用
        int UnSubscribeOrderBook(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #订阅逐笔行情，包括股票、指数和期权。
        #@return 订阅逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        #@param count 要订阅/退订行情订单簿的合约个数
        #@param exchange_id 交易所代码
        #@remark 可以一次性订阅同一证券交易所的多个合约，无论用户因为何种问题需要重新登录行情服务器，都需要重新订阅行情
        int SubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订逐笔行情，包括股票、指数和期权。
        #@return 取消订阅逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param ticker 合约ID数组，注意合约代码必须以'\0'结尾，不包含空格
        #@param count 要订阅/退订行情订单簿的合约个数
        #@param exchange_id 交易所代码
        #@remark 可以一次性取消订阅同一证券交易所的多个合约，需要与订阅逐笔行情接口配套使用
        int UnSubscribeTickByTick(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #订阅全市场的股票行情
        #@return 订阅全市场行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与全市场退订行情接口配套使用
        int SubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订全市场的股票行情
        #@return 退订全市场行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与订阅全市场行情接口配套使用
        int UnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #订阅全市场的股票行情订单簿
        #@return 订阅全市场行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与全市场退订行情订单簿接口配套使用
        int SubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订全市场的股票行情订单簿
        #@return 退订全市场行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与订阅全市场行情订单簿接口配套使用
        int UnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #订阅全市场的股票逐笔行情
        #@return 订阅全市场逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与全市场退订逐笔行情接口配套使用
        int SubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订全市场的股票逐笔行情
        #@return 退订全市场逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与订阅全市场逐笔行情接口配套使用
        int UnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #用户登录请求
        #@return 登录是否成功，“0”表示登录成功，“-1”表示连接服务器出错，此时用户可以调用GetApiLastError()来获取错误代码，“-2”表示已存在连接，不允许重复登录，如果需要重连，请先logout，“-3”表示输入有错误
        #@param ip 服务器ip地址，类似“127.0.0.1”
        #@param port 服务器端口号
        #@param user 登陆用户名
        #@param password 登陆密码
        #@param sock_type “1”代表TCP，“2”代表UDP
        #@remark 此函数为同步阻塞式，不需要异步等待登录成功，当函数返回即可进行后续操作，此api只能有一个连接
        int Login(const_char *ip, int port, const_char *user, const_char *password,
                  XTP_PROTOCOL_TYPE sock_type) nogil except +

        #登出请求
        #@return 登出是否成功，“0”表示登出成功，非“0”表示登出出错，此时用户可以调用GetApiLastError()来获取错误代码
        #@remark 此函数为同步阻塞式，不需要异步等待登出，当函数返回即可进行后续操作
        int Logout() nogil except +

        #获取当前交易日可交易合约
        #@return 查询是否成功，“0”表示查询成功，非“0”表示查询不成功
        #@param exchange_id 交易所代码
        int QueryAllTickers(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #获取合约的最新价格信息
        #@return 查询是否成功，“0”表示查询成功，非“0”表示查询不成功
        #@param exchange_id 交易所代码
        int QueryTickersPriceInfo(char *ticker[], int count, XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #获取所有合约的最新价格信息
        #@return 查询是否成功，“0”表示查询成功，非“0”表示查询不成功
        int QueryAllTickersPriceInfo() nogil except +

        #订阅全市场的期权行情
        #@return 订阅全市期权场行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与全市场退订期权行情接口配套使用
        int SubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订全市场的期权行情
        #@return 退订全市场期权行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与订阅全市场期权行情接口配套使用
        int UnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #订阅全市场的期权行情订单簿
        #@return 订阅全市场期权行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与全市场退订期权行情订单簿接口配套使用
        int SubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订全市场的期权行情订单簿
        #@return 退订全市场期权行情订单簿接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与订阅全市场期权行情订单簿接口配套使用
        int UnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #订阅全市场的期权逐笔行情
        #@return 订阅全市场期权逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与全市场退订期权逐笔行情接口配套使用
        int SubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id) nogil except +

        #退订全市场的期权逐笔行情
        #@return 退订全市场期权逐笔行情接口调用是否成功，“0”表示接口调用成功，非“0”表示接口调用出错
        #@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        #@remark 需要与订阅全市场期权逐笔行情接口配套使用
        int UnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id) nogil except +


cdef extern from "xtp_quote_api.h" namespace "XTP::API::QuoteApi":
    #创建QuoteApi
    #@param client_id （必须输入）用于区分同一用户的不同客户端，由用户自定义
    #@param save_file_path （必须输入）存贮订阅信息文件的目录，请设定一个有可写权限的真实存在的路径
    #@param log_level 日志输出级别
    #@return 创建出的UserApi
    #@remark 如果一个账户需要在多个客户端登录，请使用不同的client_id，系统允许一个账户同时登录多个客户端，
    # 但是对于同一账户，相同的client_id只能保持一个session连接，后面的登录在前一个session存续期间，无法连接
    QuoteApi *CreateQuoteApi(uint8_t client_id, const_char *save_file_path,
                             XTP_LOG_LEVEL log_level) nogil except +


cdef extern from 'quote_wrapper.h':
    cdef cppclass WrapperQuoteSpi:
        WrapperQuoteSpi(PyObject *obj)
