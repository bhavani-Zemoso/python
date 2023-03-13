def buy_and_sell_stock_once(prices):
  curr_price = prices[0]
  max_profit = 0
  for price in prices:
    if(price < curr_price):
      curr_price = price
    max_profit = max(max_profit, price - curr_price)
  
  return max_profit

price_list = [100, 180, 260, 310, 40, 535, 695]
print(buy_and_sell_stock_once(price_list))