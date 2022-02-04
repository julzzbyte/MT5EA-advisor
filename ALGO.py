import MetaTrader5 as mt5
import pandas as pd
from datetime import time
import datetime
import asyncio
import schedule
import time

mt5.initialize()

login= '5000239894'
password = 'ggijz5bu'
server = 'MetaQuotes-Demo'

accnt_inf = mt5.account_info()
print(accnt_inf)

asks = mt5.symbol_info("EURUSD").ask
bids = asks = mt5.symbol_info("EURUSD").bid
profit =mt5.account_info().profit
pos_total = mt5.positions_total()
symbol_info = mt5.symbol_info("EURUSD")
pos_total = mt5.positions_total()
#print(asks, bids, profit)

curr_price = mt5.symbol_info_tick("EURUSD")
print(curr_price)

equity =  mt5.account_info().equity
balance = mt5.account_info().balance
pos_total = mt5.positions_total()
profit =mt5.account_info().profit

equity =  mt5.account_info().equity
balance = mt5.account_info().balance
pos_total = mt5.positions_total()
profit =mt5.account_info().profit

async def decoy():
    await asyncio.sleep(20)
    if pos_total == 0:
        request = {

            "action"    : mt5.TRADE_ACTION_DEAL,
            "symbol"    : "EURUSD",
            "volume"    : 0.01,
            "type"      : mt5.ORDER_TYPE_BUY,
            "price"     : mt5.symbol_info("EURUSD").ask,
            "sl"        : 0.0,
            "tp"        : 0.0,
            "comment"   : "python script",
            "type_time" : mt5.ORDER_TIME_GTC,
            "type_filling" : mt5.ORDER_FILLING_IOC,
        }
    fakess = mt5.order_send(request)
    print(fakess)

equity =  mt5.account_info().equity
balance = mt5.account_info().balance
    

async def real_trade_by():
    while True:
        await asyncio.sleep(70)
        if equity > balance:
                request = {
                    "action"    : mt5.TRADE_ACTION_DEAL,
                    "symbol"    : "EURUSD",
                    "volume"    : 0.05,
                    "type"      : mt5.ORDER_TYPE_BUY,
                    "price"     : mt5.symbol_info("EURUSD").ask,
                    "sl"        : 0.0,
                    "tp"        : 0.0,
                    "comment"   : "python script",
                    "type_time" : mt5.ORDER_TIME_GTC,
                    "type_filling" : mt5.ORDER_FILLING_IOC,   
                }
                n = mt5.order_send(request)
                print(n)

equity =  mt5.account_info().equity
balance = mt5.account_info().balance
    

async def real_trade_sell():
    while True:
        await asyncio.sleep(60)   
        if balance > equity:
            
                request = {

                    "action"    : mt5.TRADE_ACTION_DEAL,
                    "symbol"    : "EURUSD",
                    "volume"    : 0.05,
                    "type"      : mt5.ORDER_TYPE_SELL,
                    "price"     : mt5.symbol_info("EURUSD").bid,
                    "sl"        : 0.0,
                    "tp"        : 0.0,
                    "comment"   : "python script",
                    "type_time" : mt5.ORDER_TIME_GTC,
                    "type_filling" : mt5.ORDER_FILLING_IOC,
                }
                o = mt5.order_send(request)
                print(o)

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(decoy())
    asyncio.ensure_future(real_trade_by()) 
    asyncio.ensure_future(real_trade_sell())
    
except KeyboardInterrupt:
    pass
finally:
    print("initaiting trade...")
    print(equity, balance)
