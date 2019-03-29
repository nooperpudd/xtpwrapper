#ifndef QUOTE_WRAPPER
#define QUOTE_WRAPPER

#include "Python.h"
#include "pythread.h"
#include "xtp_quote_api.h"

using namespace XTP::API;

static inline int QuoteSpi_OnDisconnected(PyObject *, int);
static inline int QuoteSpi_OnError(PyObject *, XTPRI *);

static inline int QuoteSpi_OnSubMarketData(PyObject *, XTPST *, XTPRI *, bool);
static inline int QuoteSpi_OnUnSubMarketData(PyObject *, XTPST *, XTPRI *, bool);
static inline int QuoteSpi_OnDepthMarketData(PyObject *, XTPMD *, int64_t[], int32_t, int32_t, int64_t[], int32_t, int32_t);

static inline int QuoteSpi_OnSubOrderBook(PyObject *, XTPST *, XTPRI *, bool);
static inline int QuoteSpi_OnUnSubOrderBook(PyObject *, XTPST *, XTPRI *, bool);
static inline int QuoteSpi_OnOrderBook(PyObject *, XTPOB *);

static inline int QuoteSpi_OnSubTickByTick(PyObject *, XTPST *, XTPRI *, bool);
static inline int QuoteSpi_OnUnSubTickByTick(PyObject *, XTPST *, XTPRI *, bool);
static inline int QuoteSpi_OnTickByTick(PyObject *, XTPTBT *);

static inline int QuoteSpi_OnSubscribeAllMarketData(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);
static inline int QuoteSpi_OnUnSubscribeAllMarketData(PyObject *, XTP_EXCHANGE_TYPE , XTPRI *);

static inline int QuoteSpi_OnSubscribeAllOrderBook(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);
static inline int QuoteSpi_OnUnSubscribeAllOrderBook(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);

static inline int QuoteSpi_OnSubscribeAllTickByTick(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);
static inline int QuoteSpi_OnUnSubscribeAllTickByTick(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);

static inline int QuoteSpi_OnQueryAllTickers(PyObject *, XTPQSI *, XTPRI *, bool);
static inline int QuoteSpi_OnQueryTickersPriceInfo(PyObject *, XTPTPI *, XTPRI *, bool);

static inline int QuoteSpi_OnSubscribeAllOptionMarketData(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);
static inline int QuoteSpi_OnUnSubscribeAllOptionMarketData(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);

static inline int QuoteSpi_OnSubscribeAllOptionOrderBook(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);
static inline int QuoteSpi_OnUnSubscribeAllOptionOrderBook(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);

static inline int QuoteSpi_OnSubscribeAllOptionTickByTick(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);
static inline int QuoteSpi_OnUnSubscribeAllOptionTickByTick(PyObject *, XTP_EXCHANGE_TYPE, XTPRI *);


#define Python_GIL(func) \
	do { \
		PyGILState_STATE gil_state = PyGILState_Ensure(); \
		if ((func) == -1) PyErr_Print();  \
		PyGILState_Release(gil_state); \
	} while (false)


class WrapperQuoteSpi: public QuoteSpi {

    public:
        WrapperQuoteSpi(PyObject *obj):self(obj) {};

	    virtual ~WrapperQuoteSpi(){};
        ///当客户端与行情后台通信连接断开时，该方法被调用。
        ///@param reason 错误原因，请与错误代码表对应
        ///@remark api不会自动重连，当断线发生时，请用户自行选择后续操作。可以在此函数中调用Login重新登录。注意用户重新登录后，需要重新订阅行情
        virtual void OnDisconnected(int reason) {
            Python_GIL(QuoteSpi_OnDisconnected(self, reason));
        };


        ///错误应答
        ///@param error_info 当服务器响应发生错误时的具体的错误代码和错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 此函数只有在服务器发生错误时才会调用，一般无需用户处理
        virtual void OnError(XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnError(self, error_info));
        };

        ///订阅行情应答，包括股票、指数和期权
        ///@param ticker 详细的合约订阅情况
        ///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        ///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) {
             Python_GIL(QuoteSpi_OnSubMarketData(self, ticker, error_info, is_last));
        };

        ///退订行情应答，包括股票、指数和期权
        ///@param ticker 详细的合约取消订阅情况
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        ///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnUnSubMarketData(XTPST *ticker, XTPRI *error_info, bool is_last) {
             Python_GIL(QuoteSpi_OnUnSubMarketData(self, ticker, error_info, is_last));
        };

        ///深度行情通知，包含买一卖一队列
        ///@param market_data 行情数据
        ///@param bid1_qty 买一队列数据
        ///@param bid1_count 买一队列的有效委托笔数
        ///@param max_bid1_count 买一队列总委托笔数
        ///@param ask1_qty 卖一队列数据
        ///@param ask1_count 卖一队列的有效委托笔数
        ///@param max_ask1_count 卖一队列总委托笔数
        ///@remark 需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnDepthMarketData(XTPMD *market_data, int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count,
        int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) {
             Python_GIL(QuoteSpi_OnDepthMarketData(self, market_data,
                                                   bid1_qty, bid1_count, max_bid1_count,
                                                   ask1_qty, ask1_count, max_ask1_count));
        };

        ///订阅行情订单簿应答，包括股票、指数和期权
        ///@param ticker 详细的合约订阅情况
        ///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        ///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) {
             Python_GIL(QuoteSpi_OnSubOrderBook(self, ticker, error_info, is_last));
        };

        ///退订行情订单簿应答，包括股票、指数和期权
        ///@param ticker 详细的合约取消订阅情况
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        ///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnUnSubOrderBook(XTPST *ticker, XTPRI *error_info, bool is_last) {
             Python_GIL(QuoteSpi_OnUnSubOrderBook(self, ticker, error_info, is_last));
        };

        ///行情订单簿通知，包括股票、指数和期权
        ///@param order_book 行情订单簿数据，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnOrderBook(XTPOB *order_book) {
             Python_GIL(QuoteSpi_OnOrderBook(self,order_book));
        };

        ///订阅逐笔行情应答，包括股票、指数和期权
        ///@param ticker 详细的合约订阅情况
        ///@param error_info 订阅合约发生错误时的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@param is_last 是否此次订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        ///@remark 每条订阅的合约均对应一条订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) {
             Python_GIL(QuoteSpi_OnSubTickByTick(self,ticker,error_info,is_last));
        };

        ///退订逐笔行情应答，包括股票、指数和期权
        ///@param ticker 详细的合约取消订阅情况
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@param is_last 是否此次取消订阅的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        ///@remark 每条取消订阅的合约均对应一条取消订阅应答，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnUnSubTickByTick(XTPST *ticker, XTPRI *error_info, bool is_last) {
             Python_GIL(QuoteSpi_OnUnSubTickByTick(self, ticker, error_info, is_last));
        };

        ///逐笔行情通知，包括股票、指数和期权
        ///@param tbt_data 逐笔行情数据，包括逐笔委托和逐笔成交，此为共用结构体，需要根据type来区分是逐笔委托还是逐笔成交，需要快速返回，否则会堵塞后续消息，当堵塞严重时，会触发断线
        virtual void OnTickByTick(XTPTBT *tbt_data) {
             Python_GIL(QuoteSpi_OnTickByTick(self, tbt_data));
        };

        ///订阅全市场的股票行情应答
        ///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnSubscribeAllMarketData(self, exchange_id, error_info));
        };

        ///退订全市场的股票行情应答
        ///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnUnSubscribeAllMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnUnSubscribeAllMarketData(self, exchange_id, error_info));
        };

        ///订阅全市场的股票行情订单簿应答
        ///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnSubscribeAllOrderBook(self, exchange_id, error_info));
        };

        ///退订全市场的股票行情订单簿应答
        ///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnUnSubscribeAllOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnUnSubscribeAllOrderBook(self, exchange_id, error_info));
        };

        ///订阅全市场的股票逐笔行情应答
        ///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnSubscribeAllTickByTick(self, exchange_id, error_info));
        };

        ///退订全市场的股票逐笔行情应答
        ///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnUnSubscribeAllTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnUnSubscribeAllTickByTick(self, exchange_id, error_info));
        };


        ///查询可交易合约的应答
        ///@param ticker_info 可交易合约信息
        ///@param error_info 查询可交易合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@param is_last 是否此次查询可交易合约的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        virtual void OnQueryAllTickers(XTPQSI* ticker_info, XTPRI *error_info, bool is_last) {
             Python_GIL(QuoteSpi_OnQueryAllTickers(self, ticker_info, error_info, is_last));
        };

        ///查询合约的最新价格信息应答
        ///@param ticker_info 合约的最新价格信息
        ///@param error_info 查询合约的最新价格信息时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@param is_last 是否此次查询的最后一个应答，当为最后一个的时候为true，如果为false，表示还有其他后续消息响应
        virtual void OnQueryTickersPriceInfo(XTPTPI* ticker_info, XTPRI *error_info, bool is_last) {
             Python_GIL(QuoteSpi_OnQueryTickersPriceInfo(self, ticker_info, error_info, is_last));
        };

        ///订阅全市场的期权行情应答
        ///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnSubscribeAllOptionMarketData(self, exchange_id, error_info));
        };

        ///退订全市场的期权行情应答
        ///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnUnSubscribeAllOptionMarketData(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnUnSubscribeAllOptionMarketData(self, exchange_id, error_info));
        };

        ///订阅全市场的期权行情订单簿应答
        ///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnSubscribeAllOptionOrderBook(self, exchange_id, error_info));
        };

        ///退订全市场的期权行情订单簿应答
        ///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnUnSubscribeAllOptionOrderBook(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnUnSubscribeAllOptionOrderBook(self, exchange_id, error_info));
        };

        ///订阅全市场的期权逐笔行情应答
        ///@param exchange_id 表示当前全订阅的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnSubscribeAllOptionTickByTick(self, exchange_id, error_info));
        };

        ///退订全市场的期权逐笔行情应答
        ///@param exchange_id 表示当前退订的市场，如果为XTP_EXCHANGE_UNKNOWN，表示沪深全市场，XTP_EXCHANGE_SH表示为上海全市场，XTP_EXCHANGE_SZ表示为深圳全市场
        ///@param error_info 取消订阅合约时发生错误时返回的错误信息，当error_info为空，或者error_info.error_id为0时，表明没有错误
        ///@remark 需要快速返回
        virtual void OnUnSubscribeAllOptionTickByTick(XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) {
             Python_GIL(QuoteSpi_OnUnSubscribeAllOptionTickByTick(self, exchange_id, error_info));
        };

    private:
	    PyObject *self;
};

#endif /* QUOTE_WRAPPER */