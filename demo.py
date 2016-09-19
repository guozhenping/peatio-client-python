import time
import urllib2
from lib.client import Client, get_api_path

client = Client(access_key='your access key', secret_key='your secret key')

#demo of GET APIs

#get member info
print client.get(get_api_path('members'))  #获取 云币我的余额   ok

#get markets
markets =  client.get(get_api_path('markets')) #ok
print "markets:", markets

#get tickers of each market
#market should be specified in url
print 
print "tickers in markets"
for market in markets:            #获取 云币ETC市场的价格信息     ok
    print client.get(get_api_path('tickers') % market['id'])

#get orders of each market
#market should be specified in params
print 
print "orders in markets"     #获取 我的etc委托订单   ok
for market in markets:
    print client.get(get_api_path('orders'), {'market': market['id']})   
 
#get order book
print client.get(get_api_path('order_book'), params={'market': 'btccny'})   #获取 云币ETC的挂单信息   ok

#get tardes
print client.get(get_api_path('trades'), params={'market': 'btccny'}) #获得 云币ETC市场中最近的撮合订单

#get my trades
print client.get(get_api_path('my_trades'), params={'market': 'btccny'})   #获得 我的etc最近的撮合订单  ok

#get k line
print client.get(get_api_path('k'), params={'market': 'btccny'})


#demo of POST APIs
#DANGROUS, you better use test account to debug POST APIs

"""
markets =  client.get(get_api_path('markets'))
print markets

#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 10, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res

#buy 10 dogecoins at price 0.001
params = {'market': 'dogcny', 'side': 'buy', 'volume': 10, 'price': 0.001}
res = client.post(get_api_path('orders'), params)
print res

#clear all orders in all markets
res = client.post(get_api_path('clear'))   #ok  取消订单
print res
#delete a specific order by order_id

#first, let's create an sell order
#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 12, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res
order_id = res['id']

#delete this order
params = {"id": order_id}
res = client.post(get_api_path('delete_order'), params)
print res

#create multi orders
params = {'market': 'dogcny', 'orders': [{'side': 'buy', 'volume': 12, 'price': 0.0002}, {'side': 'sell', 'volume': 11, 'price': 0.01}]}
res = client.post(get_api_path('multi_orders'), params)
print res
"""
