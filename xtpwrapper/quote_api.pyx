# encoding:utf-8
# distutils: language=c++

from cpython cimport PyObject
from libc.stdlib cimport malloc, free
from libc.stdint cimport uint8_t,uint32_t,int64_t,int32_t
from libc.string cimport const_char
from libcpp cimport bool as cbool

from .headers.xtp_api_struct_common cimport XTPRI
from .headers.xtp_quote_api cimport QuoteApi, WrapperQuoteSpi, CreateQuoteApi
from .headers.xtp_api_data_type cimport XTP_EXCHANGE_TYPE, XTP_PROTOCOL_TYPE, XTP_LOG_LEVEL
from .headers.xquote_api_struct cimport XTPST, XTPMD, XTPOB, XTPTBT, XTPTPI, XTPQSI

from xtpwrapper._struct import XTPRspInfoStruct
from xtpwrapper._struct import xquote_struct

cdef class QuoteWrapper:
    cdef QuoteApi *_api
    cdef WrapperQuoteSpi *_spi

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

    def GetTradingDay(self):
        cdef const_char *result

        if self._spi is not NULL:
            with nogil:
                result = self._api.GetTradingDay()
            return result

    def GetApiVersion(self):

        cdef const_char *result
        if self._api is not NULL:
            result = self._api.GetApiVersion()
            return result

    def GetApiLastError(self):

        cdef XTPRI *err
        if self._spi is not NULL:
            with nogil:
                err = self._api.GetApiLastError()
            return XTPRspInfoStruct.from_address(<size_t> err)

    def CreateQuote(self, uint8_t client_id, const_char *save_file_path,
                    int log_level):

        self._api = CreateQuoteApi(client_id, save_file_path, <XTP_LOG_LEVEL> log_level)

        if self._api is not NULL:

            self._spi = new WrapperQuoteSpi(<PyObject *> self)

            if self._spi is not NULL:
                self._api.RegisterSpi(self._spi)
            else:
                raise MemoryError()
        else:
            raise MemoryError()

    def SetUDPBufferSize(self, uint32_t buff_size):

        if self._api is not NULL:
            with nogil:
                self._api.SetUDPBufferSize(buff_size)

    def SetHeartBeatInterval(self, uint32_t interval):

        if self._api is not NULL:
            with nogil:
                self._api.SetHeartBeatInterval(interval)

    def SubscribeMarketData(self, ticks, int exchange_id):

        cdef Py_ssize_t count
        cdef int result
        cdef char ** ticker

        if self._spi is not NULL:
            count = len(ticks)
            ticker = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    ticker[i] = ticks[i]
                with nogil:
                    result = self._api.SubscribeMarketData(ticker, <int> count, <XTP_EXCHANGE_TYPE> exchange_id)
            finally:
                free(ticker)
            return result

    def UnSubscribeMarketData(self, ticks, int exchange_id):

        cdef Py_ssize_t count
        cdef int result
        cdef char ** ticker

        if self._spi is not NULL:
            count = len(ticks)
            ticker = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    ticker[i] = ticks[i]
                with nogil:
                    result = self._api.UnSubscribeMarketData(ticker, <int> count, <XTP_EXCHANGE_TYPE> exchange_id)
            finally:
                free(ticker)
            return result

    def SubscribeOrderBook(self, ticks, int exchange_id):

        cdef Py_ssize_t count
        cdef int result
        cdef char ** ticker

        if self._spi is not NULL:
            count = len(ticks)
            ticker = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    ticker[i] = ticks[i]
                with nogil:
                    result = self._api.SubscribeOrderBook(ticker, <int> count, <XTP_EXCHANGE_TYPE> exchange_id)
            finally:
                free(ticker)
            return result

    def UnSubscribeOrderBook(self, ticks, int exchange_id):
        cdef Py_ssize_t count
        cdef int result
        cdef char ** ticker

        if self._spi is not NULL:
            count = len(ticks)
            ticker = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    ticker[i] = ticks[i]
                with nogil:
                    result = self._api.UnSubscribeOrderBook(ticker, <int> count, <XTP_EXCHANGE_TYPE> exchange_id)
            finally:
                free(ticker)
            return result

    def SubscribeTickByTick(self, ticks, int exchange_id):
        cdef Py_ssize_t count
        cdef int result
        cdef char ** ticker

        if self._spi is not NULL:
            count = len(ticks)
            ticker = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    ticker[i] = ticks[i]
                with nogil:
                    result = self._api.SubscribeTickByTick(ticker, <int> count, <XTP_EXCHANGE_TYPE> exchange_id)
            finally:
                free(ticker)
            return result

    def UnSubscribeTickByTick(self, ticks, int exchange_id):
        cdef Py_ssize_t count
        cdef int result
        cdef char ** ticker

        if self._spi is not NULL:
            count = len(ticks)
            ticker = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    ticker[i] = ticks[i]
                with nogil:
                    result = self._api.UnSubscribeTickByTick(ticker, <int> count, <XTP_EXCHANGE_TYPE> exchange_id)
            finally:
                free(ticker)
            return result

    def SubscribeAllMarketData(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllMarketData(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def UnSubscribeAllMarketData(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllMarketData(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def SubscribeAllOrderBook(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllOrderBook(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def UnSubscribeAllOrderBook(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllOrderBook(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def SubscribeAllTickByTick(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllTickByTick(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def UnSubscribeAllTickByTick(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllTickByTick(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def Login(self, const_char *ip, int port, const_char *user,
              const_char *password, int sock_type):

        cdef int result
        with nogil:
            result = self._api.Login(ip, port, user, password, <XTP_PROTOCOL_TYPE> sock_type)
        return result
    def Logout(self):
        cdef int result
        with nogil:
            result = self._api.Logout()
        return result

    def QueryAllTickers(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.QueryAllTickers(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def QueryTickersPriceInfo(self, ticks, int exchange_id):
        cdef Py_ssize_t count
        cdef int result
        cdef char ** ticker

        if self._spi is not NULL:
            count = len(ticks)
            ticker = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    ticker[i] = ticks[i]
                with nogil:
                    result = self._api.QueryTickersPriceInfo(ticker, <int> count, <XTP_EXCHANGE_TYPE> exchange_id)
            finally:
                free(ticker)
            return result

    def QueryAllTickersPriceInfo(self):
        cdef int result
        with nogil:
            result = self._api.QueryAllTickersPriceInfo()
        return result

    def SubscribeAllOptionMarketData(self, int exchange_id):

        cdef int result
        with nogil:
            result = self._api.SubscribeAllOptionMarketData(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def UnSubscribeAllOptionMarketData(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllOptionMarketData(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

    def SubscribeAllOptionOrderBook(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllOptionOrderBook(<XTP_EXCHANGE_TYPE> exchange_id)
        return result
    def UnSubscribeAllOptionOrderBook(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllOptionOrderBook(<XTP_EXCHANGE_TYPE> exchange_id)
        return result
    def SubscribeAllOptionTickByTick(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllOptionTickByTick(<XTP_EXCHANGE_TYPE> exchange_id)
        return result
    def UnSubscribeAllOptionTickByTick(self, int exchange_id):

        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllOptionTickByTick(<XTP_EXCHANGE_TYPE> exchange_id)
        return result

cdef extern int QuoteSpi_OnDisconnected(self, int reason) except -1:
    self.OnDisconnected(reason)
    return 0

cdef extern int QuoteSpi_OnError(self, XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    self.OnError(err_obj)
    return 0

cdef extern int QuoteSpi_OnSubMarketData(self, XTPST *ticker, XTPRI *error_info, cbool is_last) except -1:
    ticker_obj = xquote_struct.XTPSpecificTickerStruct.from_address(<size_t> ticker)
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    self.OnSubMarketData(ticker_obj, err_obj, is_last)
    return 0

cdef extern int QuoteSpi_OnUnSubMarketData(self, XTPST *ticker, XTPRI *error_info, cbool is_last) except -1:
    ticker_obj = xquote_struct.XTPSpecificTickerStruct.from_address(<size_t> ticker)
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnUnSubMarketData(ticker_obj, err_obj, is_last)
    return 0

cdef extern int QuoteSpi_OnDepthMarketData(self, XTPMD *market_data,
                                           int64_t bid1_qty[], int32_t bid1_count, int32_t max_bid1_count,
                                           int64_t ask1_qty[], int32_t ask1_count, int32_t max_ask1_count) except -1:

    market_data_obj = xquote_struct.XTPMarketDataStruct.from_address(<size_t> market_data)

    cdef Py_ssize_t count_bid = sizeof(bid1_qty)
    cdef Py_ssize_t count_ask = sizeof(ask1_qty)

    bid1_qty_obj = list()
    ask1_qty_obj = list()

    for i from 0 <= i < count_bid:
        bid1_qty_obj.append(bid1_qty[i])

    for i from 0 <= i < count_ask:
        ask1_qty_obj.append(ask1_qty[i])

    self.OnDepthMarketData(market_data_obj,
                           bid1_qty_obj, bid1_count, max_bid1_count,
                           ask1_qty_obj, ask1_count, max_ask1_count)
    return 0

cdef extern int QuoteSpi_OnSubOrderBook(self, XTPST *ticker, XTPRI *error_info,
                                        cbool is_last) except -1:
    ticker_obj = xquote_struct.XTPSpecificTickerStruct.from_address(<size_t> ticker)
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    self.OnSubOrderBook(ticker_obj, err_obj, is_last)
    return 0
cdef extern int QuoteSpi_OnUnSubOrderBook(self, XTPST *ticker, XTPRI *error_info,
                                          cbool is_last) except -1:
    ticker_obj = xquote_struct.XTPSpecificTickerStruct.from_address(<size_t> ticker)
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnUnSubOrderBook(ticker_obj, err_obj, is_last)
    return 0
cdef extern int QuoteSpi_OnOrderBook(self, XTPOB *order_book) except -1:
    order_book_obj = xquote_struct.OrderBookStruct.from_address(<size_t> order_book)

    self.OnOrderBook(order_book_obj)
    return 0

cdef extern int QuoteSpi_OnSubTickByTick(self, XTPST *ticker, XTPRI *error_info, cbool is_last) except -1:
    ticker_obj = xquote_struct.XTPSpecificTickerStruct.from_address(<size_t> ticker)
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    self.OnSubTickByTick(ticker_obj, err_obj, is_last)
    return 0
cdef extern int QuoteSpi_OnUnSubTickByTick(self, XTPST *ticker, XTPRI *error_info, cbool is_last) except -1:
    ticker_obj = xquote_struct.XTPSpecificTickerStruct.from_address(<size_t> ticker)
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    self.OnUnSubTickByTick(ticker_obj, err_obj, is_last)
    return 0
cdef extern int QuoteSpi_OnTickByTick(self, XTPTBT *tbt_data) except -1:
    tbt_data_obj = xquote_struct.XTPTickByTickStruct.from_address(<size_t> tbt_data)
    self.OnTickByTick(tbt_data_obj)
    return 0

cdef extern int QuoteSpi_OnSubscribeAllMarketData(self, XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)

    self.OnSubscribeAllMarketData(exchange_id, err_obj)
    return 0
cdef extern int QuoteSpi_OnUnSubscribeAllMarketData(self, XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnUnSubscribeAllMarketData(exchange_id, err_obj)
    return 0

cdef extern int QuoteSpi_OnSubscribeAllOrderBook(self, XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnSubscribeAllOrderBook(exchange_id, err_obj)
    return 0
cdef extern int QuoteSpi_OnUnSubscribeAllOrderBook(self, XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnUnSubscribeAllOrderBook(exchange_id, err_obj)
    return 0

cdef extern int QuoteSpi_OnSubscribeAllTickByTick(self, XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnSubscribeAllTickByTick(exchange_id, err_obj)
    return 0

cdef extern int QuoteSpi_OnUnSubscribeAllTickByTick(self, XTP_EXCHANGE_TYPE exchange_id, XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnUnSubscribeAllTickByTick(exchange_id, err_obj)
    return 0

cdef extern int QuoteSpi_OnQueryAllTickers(self, XTPQSI*ticker_info, XTPRI *error_info, cbool is_last) except -1:
    ticker_info_obj = xquote_struct.XTPQuoteStaticInfo.from_address(<size_t> ticker_info)

    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnQueryAllTickers(ticker_info_obj, err_obj, is_last)
    return 0
cdef extern int QuoteSpi_OnQueryTickersPriceInfo(self, XTPTPI*ticker_info, XTPRI *error_info, cbool is_last) except -1:
    ticker_info_obj = xquote_struct.XTPQuoteStaticInfo.from_address(<size_t> ticker_info)
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnQueryTickersPriceInfo(ticker_info_obj, err_obj, is_last)
    return 0

cdef extern int QuoteSpi_OnSubscribeAllOptionMarketData(self, XTP_EXCHANGE_TYPE exchange_id,
                                                        XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnSubscribeAllOptionMarketData(exchange_id, err_obj)
    return 0
cdef extern int QuoteSpi_OnUnSubscribeAllOptionMarketData(self, XTP_EXCHANGE_TYPE exchange_id,
                                                          XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnUnSubscribeAllOptionMarketData(exchange_id, err_obj)
    return 0

cdef extern int QuoteSpi_OnSubscribeAllOptionOrderBook(self, XTP_EXCHANGE_TYPE exchange_id,
                                                       XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnSubscribeAllOptionOrderBook(exchange_id, err_obj)
    return 0
cdef extern int QuoteSpi_OnUnSubscribeAllOptionOrderBook(self, XTP_EXCHANGE_TYPE exchange_id,
                                                         XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnUnSubscribeAllOptionOrderBook(exchange_id, err_obj)
    return 0

cdef extern int QuoteSpi_OnSubscribeAllOptionTickByTick(self, XTP_EXCHANGE_TYPE exchange_id,
                                                        XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnSubscribeAllOptionTickByTick(exchange_id, err_obj)
    return 0
cdef extern int QuoteSpi_OnUnSubscribeAllOptionTickByTick(self, XTP_EXCHANGE_TYPE exchange_id,
                                                          XTPRI *error_info) except -1:
    err_obj = XTPRspInfoStruct.from_address(<size_t> error_info)
    self.OnUnSubscribeAllOptionTickByTick(exchange_id, err_obj)
    return 0
