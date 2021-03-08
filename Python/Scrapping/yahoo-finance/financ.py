import yfinance as yf
msft = yf.Ticker("MSFT")
petr = yf.Ticker("PETR")
print(petr.info)
print("MSFT = US$", msft.info['bid'])

"""
for i in msft.info.keys():
    a.append(i)
for j in msft.info.values():
    b.append(j)
for i in range(len(a)):
    print(a[i], "=", b[i])
"""