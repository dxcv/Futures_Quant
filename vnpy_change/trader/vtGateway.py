#!/usr/bin/env python
# -*- coding: utf-8 -*-


from vnpy_change.event import *
from vnpy_change.trader.vtEvent import *

"""
通用事件儿
在主引擎中添加gateway的实例之后
实例的推送数据的接口
推送 tick order trade account position error log contract history
gateway 另外需要实现的connect, close qryAccount qryHistory qryPosition sendorder subscribe
qryhistory很少有gateway开放这个接口，如需查询历史数据，可查询本地数据库 或者网站 直接接口的很少
"""


########################################################################
class VtGateway(object):
    """交易接口"""

    #----------------------------------------------------------------------
    def __init__(self, eventEngine, gatewayName):
        """Constructor"""
        self.eventEngine = eventEngine
        self.gatewayName = gatewayName
        
    #----------------------------------------------------------------------
    def onTick(self, tick):
        """市场行情推送"""
        # 通用事件
        event1 = Event(type_=EVENT_TICK)
        event1.dict_['data'] = tick
        self.eventEngine.put(event1)
        
        # 特定合约代码的事件
        event2 = Event(type_=EVENT_TICK+tick.vtSymbol)
        event2.dict_['data'] = tick
        self.eventEngine.put(event2)

    # ----------------------------------------------------------------------
    def onOrder(self, order):
        """订单变化推送"""
        # 通用事件
        event1 = Event(type_=EVENT_ORDER)
        event1.dict_['data'] = order
        self.eventEngine.put(event1)

        # 特定订单编号的事件
        event2 = Event(type_=EVENT_ORDER + order.vtOrderID)
        event2.dict_['data'] = order
        self.eventEngine.put(event2)

    #----------------------------------------------------------------------
    def onTrade(self, trade):
        """成交信息推送"""
        # 通用事件
        event1 = Event(type_=EVENT_TRADE)
        event1.dict_['data'] = trade
        self.eventEngine.put(event1)
        
        # 特定合约的成交事件
        event2 = Event(type_=EVENT_TRADE+trade.vtSymbol)
        event2.dict_['data'] = trade
        self.eventEngine.put(event2)        

    #----------------------------------------------------------------------
    def onPosition(self, position):
        """持仓信息推送"""
        # 通用事件
        event1 = Event(type_=EVENT_POSITION)
        event1.dict_['data'] = position
        self.eventEngine.put(event1)
        
        # 特定合约代码的事件
        event2 = Event(type_=EVENT_POSITION+position.vtSymbol)
        event2.dict_['data'] = position
        self.eventEngine.put(event2)
    
    #----------------------------------------------------------------------
    def onAccount(self, account):
        """账户信息推送"""
        # 通用事件
        event1 = Event(type_=EVENT_ACCOUNT)
        event1.dict_['data'] = account
        self.eventEngine.put(event1)
        
        # 特定合约代码的事件
        event2 = Event(type_=EVENT_ACCOUNT+account.vtAccountID)
        event2.dict_['data'] = account
        self.eventEngine.put(event2)
    
    #----------------------------------------------------------------------
    def onError(self, error):
        """错误信息推送"""
        # 通用事件
        event1 = Event(type_=EVENT_ERROR)
        event1.dict_['data'] = error
        self.eventEngine.put(event1)    
        
    #----------------------------------------------------------------------
    def onLog(self, log):
        """日志推送"""
        # 通用事件
        event1 = Event(type_=EVENT_LOG)
        event1.dict_['data'] = log
        self.eventEngine.put(event1)
        
    #----------------------------------------------------------------------
    def onContract(self, contract):
        """合约基础信息推送"""
        # 通用事件
        event1 = Event(type_=EVENT_CONTRACT)
        event1.dict_['data'] = contract
        self.eventEngine.put(event1)        
    
    #----------------------------------------------------------------------
    def onHistory(self, history):
        """历史数据推送"""
        event = Event(EVENT_HISTORY)
        event.dict_['data'] = history
        self.eventEngine.put(event)
    
    #----------------------------------------------------------------------
    def connect(self):
        """连接"""
        pass
    
    #----------------------------------------------------------------------
    def subscribe(self, subscribeReq):
        """订阅行情"""
        pass
    
    #----------------------------------------------------------------------
    def sendOrder(self, orderReq):
        """发单"""
        pass
    
    #----------------------------------------------------------------------
    def cancelOrder(self, cancelOrderReq):
        """撤单"""
        pass
    
    #----------------------------------------------------------------------
    def qryAccount(self):
        """查询账户资金"""
        pass
    
    #----------------------------------------------------------------------
    def qryPosition(self):
        """查询持仓"""
        pass
    
    #----------------------------------------------------------------------
    def qryHistory(self, historyReq):
        """查询历史"""
        pass
    
    #----------------------------------------------------------------------
    def close(self):
        """关闭"""
        pass
    
    
    
    
    

    
    
    