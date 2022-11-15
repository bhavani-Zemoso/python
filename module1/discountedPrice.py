price = 250

if price >= 300:
    price -= (0.3 * price)
elif price >= 200 and price < 300:
    price -= (0.2 * price)
elif price >= 100 and price < 200:
    price -= (0.1 * price)
elif price > 0 and price < 100:
    price -= (0.05 * price)

print(price)
