from cpython cimport PyObject
from libc.stdlib cimport malloc, free
from libc.string cimport const_char
from libcpp cimport bool as cbool

from .headers.xtp_api_struct_common cimport XTPRI
from .headers.xtp_quote_api cimport QuoteApi, WrapperQuoteSpi, CreateQuoteApi

import ctypes

from xtpwrapper._struct import XTPRspInfoStruct

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
        result = self._api.GetApiVersion()
        return result

    def GetApiLastError(self):
        cdef XTPRI *err
        cdef PyObject data
        if self._spi is not NULL:
            with nogil:
                err = self._api.GetApiLastError()
                data = XTPRspInfoStruct.from_address(<size_t> err)
            return data

    def SetUDPBufferSize(self, unsigned int buff_size):

        with nogil:
            self._api.SetUDPBufferSize(buff_size)

    def CreateQuote(self, unsigned char client_id, const_char *save_file_path,
                    int log_level):

        self._api = CreateQuoteApi(client_id, save_file_path, log_level)

        if not self._api:
            raise MemoryError()

    def Register(self):

        if self._api is not NULL:
            self._spi = new WrapperQuoteSpi(<PyObject *> self)

            if self._spi is not NULL:
                self._api.RegisterSpi(self._spi)
            else:
                raise MemoryError()

    def SetHeartBeatInterval(self, unsigned int interval):

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
                    result = self._api.SubscribeMarketData(ticker, <int> count, exchange_id)
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
                    result = self._api.UnSubscribeMarketData(ticker, <int> count, exchange_id)
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
                    result = self._api.SubscribeOrderBook(ticker, <int> count, exchange_id)
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
                    result = self._api.UnSubscribeOrderBook(ticker, <int> count, exchange_id)
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
                    result = self._api.SubscribeTickByTick(ticker, <int> count, exchange_id)
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
                    result = self._api.UnSubscribeTickByTick(ticker, <int> count, exchange_id)
            finally:
                free(ticker)
            return result

    def SubscribeAllMarketData(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllMarketData(exchange_id)
        return result

    def UnSubscribeAllMarketData(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllMarketData(exchange_id)
        return result

    def SubscribeAllOrderBook(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllOrderBook(exchange_id)
        return result

    def UnSubscribeAllOrderBook(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllOrderBook(exchange_id)
        return result

    def SubscribeAllTickByTick(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllTickByTick(exchange_id)
        return result

    def UnSubscribeAllTickByTick(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllTickByTick(exchange_id)
        return result

    def Login(self, const_char *ip, int port, const_char *user,
              const_char *password, int sock_type):

        cdef int result
        with nogil:
            result = self._api.Login(ip, port, user, password, sock_type)
        return result
    def Logout(self):
        cdef int result
        with nogil:
            result = self._api.Logout()
        return result

    def QueryAllTickers(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.QueryAllTickers(exchange_id)
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
                    result = self._api.QueryTickersPriceInfo(ticker, <int> count, exchange_id)
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
            result = self._api.SubscribeAllOptionMarketData(exchange_id)
        return result

    def UnSubscribeAllOptionMarketData(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllOptionMarketData(exchange_id)
        return result

    def SubscribeAllOptionOrderBook(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllOptionOrderBook(exchange_id)
        return result
    def UnSubscribeAllOptionOrderBook(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllOptionOrderBook(exchange_id)
        return result
    def SubscribeAllOptionTickByTick(self, int exchange_id):
        cdef int result
        with nogil:
            result = self._api.SubscribeAllOptionTickByTick(exchange_id)
        return result
    def UnSubscribeAllOptionTickByTick(self, int exchange_id):

        cdef int result
        with nogil:
            result = self._api.UnSubscribeAllOptionTickByTick(exchange_id)
        return result
